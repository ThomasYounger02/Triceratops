#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import statsmodels.formula.api as smf
import statsmodels.api as sm
from itertools import combinations
import pandas as pd
import numpy as np
import warnings
from scipy import stats
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor
import time


class AutomatedAssessment(object):
    def __init__(self):
        pass

    @staticmethod
    def stepwise_selection_for_single(data,
                                      response,
                                      initial_list=[],
                                      full_feature=[],
                                      threshold_in=0.01,
                                      threshold_out=0.05,
                                      verbose=True,
                                      max_iteration=1000
                                      ):
        """

        :param data: input data for regression, a data frame
        :param response: response variable
        :param initial_list: initial feature list
        :param full_feature: all feature can be selected
        :param threshold_in: the max p value for add feature
        :param threshold_out: the min p value for drop feature
        :param verbose: boolean, if print drop/add process
        :param max_iteration: The maximum number of iterations
        :return:
            remain feature list
        """
        included = initial_list
        full_feature = full_feature
        iteration = 1
        while iteration < max_iteration:
            changed = False
            # forward step
            excluded = list(set(full_feature) - set(included))
            p_values = pd.Series(index=excluded)
            for feature in excluded:
                formula = '{} ~ {} + 1'.format(response, '+'.join(included + [feature]))
                model = smf.ols(formula=formula, data=data).fit()
                p_values[feature] = model.pvalues[feature]
            min_p_value = p_values.min()
            if min_p_value < threshold_in:
                best_feature = p_values.argmin()
                included.append(best_feature)
                changed = True
                if verbose:
                    print('Step-{}: Add  {} with p-value {:.4%}'.format(iteration, best_feature, min_p_value))

            # backward step
            formula = '{} ~ {} + 1'.format(response, '+'.join(included))
            model = smf.ols(formula=formula, data=data).fit()
            p_values = model.pvalues.iloc[1:]
            max_p_value = p_values.max()
            if max_p_value > threshold_out:
                changed = True
                worst_feature = p_values.argmax()
                included.remove(worst_feature)
                if verbose:
                    print('Step-{}: Drop {} with p-value {:.4%}'.format(iteration, worst_feature, max_p_value))
            if not changed:
                break
            iteration += 1
        if iteration >= max_iteration:
            msg = 'the method has been iterated {} times, but it has not converge. The method returns the features ' \
                  'from the last iteration (not the best one)'.format(iteration)
            warnings.warn(msg)

        return included

    @staticmethod
    def stepwise_selection_for_group(data,
                                     response,
                                     initial_list=[],
                                     full_feature=[],
                                     threshold_in=0.01,
                                     threshold_out=0.05,
                                     verbose=True,
                                     max_iteration=1000
                                     ):
        """

        :param data: input data for regression, a data frame
        :param response: response variable
        :param initial_list: initial feature list
        :param full_feature: all feature can be selected
        :param threshold_in: the max p value for add feature
        :param threshold_out: the min p value for drop feature
        :param verbose: boolean, if print drop/add process
        :param max_iteration: The maximum number of iterations, default 1000
        :return:
            remain feature list
        """
        included = initial_list
        full_feature = full_feature
        iteration = 1
        while iteration < max_iteration:
            changed = False
            # forward step,
            excluded = list(set(full_feature) - set(included))
            if len(excluded) == 0:
                break
            p_values = pd.Series(index=excluded)
            for feature in excluded:
                formula = '{} ~ {} + 1'.format(response, '+'.join(included + [feature]))
                print(formula)
                model = smf.ols(formula=formula, data=data).fit()
                #             p_values[feature] = model.pvalues[feature],
                df_anova = sm.stats.anova_lm(model, typ=1)
                p_values[feature] = df_anova.loc[feature]['PR(>F)']
                min_p_value = p_values.min()
            if min_p_value < threshold_in:
                best_feature = p_values.idxmin()
                included.append(best_feature)
                changed = True
                if verbose:
                    print('Step-{}: Add  {} with p-value {:.4%}'.format(iteration, best_feature, min_p_value))
            # backward step,
            formula = '{} ~ {} + 1'.format(response, '+'.join(included))
            model = smf.ols(formula=formula, data=data).fit()
            df_anova = sm.stats.anova_lm(model, typ=1)
            p_values = df_anova['PR(>F)']
            max_p_value = p_values.max()
            if max_p_value > threshold_out:
                changed = True
                worst_feature = p_values.idxmax()
                included.remove(worst_feature)
                if verbose:
                    print('Step-{}: Drop {} with p-value {:.4%}'.format(iteration, worst_feature, max_p_value))
            if not changed:
                break
            iteration += 1
        if iteration >= max_iteration:
            msg = 'the method has been iterated {} times, but it has not converge. The method returns the features ' \
                  'from the last iteration (not the best one)'.format(iteration)
            warnings.warn(msg)
        return included

    @staticmethod
    def random_group_id(data, sample_size=50, seed=None):
        """
        :param data: input data, must be data frame
        :param sample_size: sample size per group
        :param seed:
        :return:
            a series about random group_id
        """
        np.random.seed(seed)
        group_num = int(np.ceil(data.shape[0] / sample_size))
        arr_index = np.tile(np.arange(group_num), sample_size)[:data.shape[0]]
        np.random.shuffle(arr_index)
        return pd.Series(arr_index, index=data.index)


class RCBAutomatedAssessment(AutomatedAssessment):
    def __init__(self):
        self.sample_size = 0
        self.__CLEAR_DATA = False
        self.blocking_factor_p_value = pd.DataFrame()
        self.bias_factor_p_value = pd.DataFrame()
        self.blocking_factor_list = []
        self.bias_factor_dict = {}
        self.feature = []

    def set_true_clear_data(self):
        self.__CLEAR_DATA = True

    def get_clear_data(self):
        self.__warning_for_clear_data()
        return self.__CLEAR_DATA

    def pre_processing(self):
        self.set_true_clear_data()

    def sample_size_calculation(self, mu, sigma, MDE, alpha=0.05, beta=0.8):
        self.sample_size = 2 * (sigma ** 2) * ((stats.norm.ppf(1 - alpha / 2) -
                                               stats.norm.ppf(1 - beta)) ** 2) /((mu * MDE) ** 2)
        return

    def __get_group_data(self, data, column_name_for_group, group_list, exp_column, func_dict, sample_size=50,
                         seed=None):
        """
        :param data: input data, must be data frame
        :param column_name_for_group: set column name for group in group data
        :param group_list: factor to be grouping
        :param exp_column: the column name of treatment
        :param func_dict: aggregate function dict
        :param sample_size: sample size per group
        :param seed: //
        :return:
        group_data: a data frame after grouping
        """
        sup = super(RCBAutomatedAssessment, self)
        if type(group_list) != list:
            try:
                group_list = list(group_list)
            except BaseException as e:
                raise BaseException(e)
        group_list = group_list + [exp_column]
        group_id = data.groupby(group_list).apply(
            lambda df: sup.random_group_id(df, sample_size=sample_size, seed=seed))
        group_id.index = group_id.index.droplevel(list(range(len(group_list))))
        data[column_name_for_group] = group_id
        data_with_group_id = data.copy(deep=True)
        group_list = group_list + [column_name_for_group]
        group_data = data_with_group_id.groupby(group_list).agg(
            func_dict)
        return group_data.reset_index()

    @staticmethod
    def norm_test_response(response):
        try:
            shapiro = stats.shapiro(response)[1]
        except:
            shapiro = 0
        try:
            normal_test = stats.normaltest(response)[1]
        except:
            normal_test = 0
        return pd.Series([shapiro, normal_test],  # name=response.name,
                         index=['shapiro', 'normal_test'])

    def select_blocking_factor(self, data, response, blocking_factor_list, p_value=0.05):
        """
        select blocking factor from blocking_factor_list
        :param data: regression data
        :param response: response variable
        :param blocking_factor_list: //
        :param p_value: set max p_value for F test about independent variable, default 0.05
        :return:
        blocking_factor_p_value: a DataFrame, include blocking_factor and corresponding p_value
        blocking_factor_list: remaining variables
        """
        self.__warning_for_clear_data()
        for factor in blocking_factor_list:
            formula = '{} ~ C({})'.format(response, factor)
            model_block = smf.ols(formula=formula, data=data)
            results_block = model_block.fit()
            anova = sm.stats.anova_lm(results_block, typ=3)
            self.blocking_factor_p_value = pd.concat([self.blocking_factor_p_value, anova], axis=0)
        self.blocking_factor_p_value = self.blocking_factor_p_value[
            ~self.blocking_factor_p_value.index.isin(['Residual', 'Intercept'])]
        self.blocking_factor_list = self.blocking_factor_p_value[self.blocking_factor_p_value['PR(>F)'] < p_value].index
        # Converting from float to percentage
        self.blocking_factor_p_value['PR(>F)'] = self.blocking_factor_p_value['PR(>F)'].apply(
            lambda x: format(x, '.2%'))
        self.blocking_factor_list = [i[2: -1] for i in self.blocking_factor_list]

    @staticmethod
    def __list_find_str(str1, list1):
        for i in list1:
            if i.find(str1):
                return True
        return False

    def select_bias_factor(self, data, response, bias_factor_dict, p_value=0.05):
        """
        select bias factor from bias_factor_dict.keys()
        :param data: regression data
        :param response: response variable
        :param bias_factor_dict: a dictionary, e.g. {'bias_factor_1': 1}, if the key is continuous, value=1, else 0
        :param p_value: 0.05
        :return:
        bias_factor_p_value: a DataFrame, include bias_factor and corresponding p_value
        bias_factor_dict: remaining variables
        """
        self.__warning_for_clear_data()
        for key in bias_factor_dict:
            formula_scheme = '{} ~ C({})' if bias_factor_dict[key] == 0 else '{} ~ {}'
            formula = formula_scheme.format(response, key)
            model_bias = smf.ols(formula=formula, data=data)
            results_bias = model_bias.fit()
            anova = sm.stats.anova_lm(results_bias, typ=3)
            self.bias_factor_p_value = pd.concat([self.bias_factor_p_value, anova], axis=0)
        self.bias_factor_p_value = self.bias_factor_p_value[
            ~self.bias_factor_p_value.index.isin(['Residual', 'Intercept'])]
        bias_factor_list = self.bias_factor_p_value[self.bias_factor_p_value['PR(>F)'] < p_value].index
        # Converting from float to percentage
        self.bias_factor_p_value['PR(>F)'] = self.bias_factor_p_value['PR(>F)'].apply(lambda x: format(x, '.2%'))
        self.bias_factor_dict = {key: bias_factor_dict[key] for key in bias_factor_dict if
                                 self.__list_find_str(key, bias_factor_list)}

    # 待完善
    @staticmethod
    def multi_col_linearity_test(data, formula, vif_score):
        y, x = dmatrices(formula_like=formula, data=data, return_type='dataframe')
        vif = pd.DataFrame()
        vif["VIF Factor"] = [variance_inflation_factor(x.values, i) for i in range(x.shape[1])]
        vif["features"] = x.columns
        vif = vif[vif['VIF Factor'] > vif_score]
        if vif.shape[0] == 0:
            print('No multi col linearity')
        else:
            msg = 'Have multi col linearity'
            warnings.warn(msg)
            print(vif)

    def __warning_for_clear_data(self):
        msg = 'The program found that the data pre-processing failed, please confirm. ' \
              'If you have already done so please use the set_true_clear_data method first.'
        if self.__CLEAR_DATA is False:
            warnings.warn(msg)

    def stepwise_selection(self,
                           data,
                           response,
                           select_type,
                           initial_list=[],
                           full_feature=[],
                           threshold_in=0.01,
                           threshold_out=0.05,
                           verbose=False,
                           max_iteration=1000
                           ):
        """
        Liner model designed by forward selection for RCB
        :param data: input data for regression, a data frame
        :param response: response variable
        :param select_type: single or group, stepwise add/drop feature type. For dummy variables, If select_type=single,
                            the method adds or removes features based on the p-value of each feature after get_dummy.
                            If type=group, the method adds or removes features based on F_test for dummy variables.
        :param initial_list: initial feature list
        :param full_feature: all feature can be selected
        :param threshold_in: the max p value for add feature
        :param threshold_out: the min p value for drop feature
        :param verbose: boolean, if print drop/add process
        :param max_iteration: The maximum number of iterations
        :return: remain feature
        Examples
        ------------
        >>> data = pd.Dataframe()
        >>>feature = ['C(exp_group)', 'C(city_id)', 'C(exp_group):C(city_id)']
        >>> stepwise_selection(data=data, response=gmv, full_feature=feature, verbose=True)

        Step-1: Add  C(city_id) with p-value 0.0000%

        self.feature = ['C(city_id)']
        ------------
        """
        if select_type == 'single':
            included = super().stepwise_selection_for_single(data=data,
                                                             response=response,
                                                             initial_list=initial_list,
                                                             full_feature=full_feature,
                                                             threshold_in=threshold_in,
                                                             threshold_out=threshold_out,
                                                             verbose=verbose,
                                                             max_iteration=max_iteration)
        elif select_type == 'group':
            included = super().stepwise_selection_for_group(data=data,
                                                            response=response,
                                                            initial_list=initial_list,
                                                            full_feature=full_feature,
                                                            threshold_in=threshold_in,
                                                            threshold_out=threshold_out,
                                                            verbose=verbose,
                                                            max_iteration=max_iteration)
        else:
            raise BaseException('select_type must be single or group')
        self.feature = included

    @staticmethod
    def get_cross_feature(feature, num):
        """
        :param feature: initial feature list
        :param num: the max num for interactive
        :return:
        """
        rel = []
        if len(feature) < 2:
            msg = 'feature num less 2, will return original feature'
            warnings.warn(msg)
            return feature
        elif num > len(feature):
            raise BaseException('The number exceeds the maximum length of the list')
        for i in range(1, num + 1):
            rel = rel + list(combinations(feature, i))
        return rel

    def get_group_data(self, data, group_list, exp_column, func_dict, response, column_name_for_group='group_id',
                       max_block_num=3, min_sample_size=500, max_sample_size=2000, step_size=100, seed=None, ignore=True,
                       verbose=False, max_iteration=20):
        """
        Method for getting small grouping. First this method will ger a categorical combination of variables, second，
        traversing whether each combination passes the normality test. The traversal order depends on the number of
        variables, the more variables, the earlier the traversal. When the number of variables is same, the traversal
        order is random.

        :param data:input_data, a data frame
        :param group_list: Variables that can be used for grouping
        :param exp_column: Experiment identification
        :param func_dict: Indicator aggregation dictionary
        :param norm_test_column: Column name of normal test
        :param column_name_for_group: default 'group_id', column name after grouping
        :param max_block_num: max block number, default 3,
        :param min_sample_size: min sample size, default 50
        :param max_sample_size: max sample size, default 200
        :param step_size: the step size in the process about finding sample size, default 10
        :param seed: random seed
        :param ignore: boolean, if ignore warning about norm test
        :param verbose: boolean, if print find group data process
        :param max_iteration: The maximum number of iterations

        :return: the data after grouping, a data frame

        Examples
        ------------
        >>> data = pd.Dataframe()
        >>> blocking_factor_list = ['city_id', 'passenger_lifecycle_type', 'subsidy_sensitive', 'native_flag']
        >>> exp_factor = 'exp_group'
        >>> group_data = rcb.get_group_data(data, group_list=blocking_factor_list, exp_column=exp_factor,
                                    func_dict=func_list, norm_test_column='gmv_his', verbose=True, max_iteration=20)

        the result maybe is:
        ----------------------------------------------------
        try the 1 times, block is ['city_id', 'subsidy_sensitive', 'native_flag']
        try sample_size: 50
        Eligible data has been found, block factor is ['city_id', 'subsidy_sensitive', 'native_flag'], sample size is 50

        or
        ----------------------------------------------------
        try the 1 times, block is ['city_id', 'passenger_lifecycle_type', 'subsidy_sensitive']
        try sample_size: 50
        try sample_size: 60
        try sample_size: 70
        try sample_size: 80
        try sample_size: 90
        try sample_size: 100
        try sample_size: 110
        try sample_size: 120
        try sample_size: 130
        try sample_size: 140
        try sample_size: 150
        try sample_size: 160
        try sample_size: 170
        try sample_size: 180
        try sample_size: 190
        try sample_size: 200
        ----------------------------------------------------
        try the 2 times, block is ['city_id', 'subsidy_sensitive', 'native_flag']
        try sample_size: 50
        Eligible data has been found, block factor is ['city_id', 'subsidy_sensitive', 'native_flag'], sample size is 50
        ------------

        """
        iteration = 1
        if len(group_list) == 0:
            raise BaseException('group list must not ne None')
        if ignore:
            warnings.filterwarnings("ignore", message="p-value may not be accurate for N > 5000.")
            warnings.filterwarnings("ignore", message="kurtosistest only valid for n>=20 ... continuing")
        temp = self.get_cross_feature(group_list, num=max_block_num)
        random_num = np.random.normal(size=len(temp))
        tmp_dict = {}
        for i in range(len(temp)):
            tmp_dict[temp[i]] = 10 * len(temp[i]) + random_num[i]
        blocking_factor = sorted(tmp_dict.items(), key=lambda x: x[1], reverse=True)
        for i in blocking_factor:
            if type(i[0]) == str:
                key = [i[0]]
            else:
                key = list(i[0])
            if verbose:
                print('-----------------------------------------------------------------------------')
                print('try the {} times, block is {}'.format(iteration, key))
            for j in range(min_sample_size, max_sample_size + step_size, step_size):
                group_data = self.__get_group_data(data, column_name_for_group, group_list=key, exp_column=exp_column,
                                                   func_dict=func_dict, sample_size=j, seed=seed)
                formula = '{} ~ '.format(response) + 'C({}) + '.format(exp_column) + '+'.join(
                    ['C({})'.format(i) for i in key])
                model_resid = smf.ols(formula=formula, data=group_data).fit()
                df_norm = self.norm_test_response(model_resid.resid)
                if verbose:
                    print('try sample_size: {}, shapiro.p_value:{}, kurtosistest.p_value:{}'.format(j, str(
                        round(df_norm.shapiro, 4)), str(round(df_norm.normal_test, 4))))
                if (df_norm.shapiro >= 0.05) | (df_norm.normal_test >= 0.05):
                    if verbose:
                        print('Eligible data has been found, block factor is {}, sample size is {}'.format(key, j))
                        print('-----------------------------------------------------------------------------')
                    return group_data

            if iteration < max_iteration:
                iteration += 1
            else:
                msg = 'the method has been iterated {} times, but it has not converge. The method returns ' \
                      'the group data from the last iteration (not the best one), you can try again with ' \
                      'another blocking factor or use this group data if you think it is OK'.format(iteration)
                warnings.warn(msg)
                if verbose:
                    print('block factor is {}, sample size is {}'.format(key, j))
                    print('-----------------------------------------------------------------------------')
                return group_data
        msg = 'the method has been iterated {} times, and it has traversed all possible combinations,' \
              'but it has not converge. The method returns ' \
              'the group data from the last iteration (not the best one), you can try again with ' \
              'another blocking factor or use this group data if you think it is OK'.format(iteration)
        warnings.warn(msg)

        return group_data

    def get_group_data_for_designation(self, data, column_name_for_group, group_list, exp_column, func_dict,
                                       sample_size=50,
                                       seed=None):
        """
        :param data: input data, must be data frame
        :param column_name_for_group: set column name for group in group data
        :param group_list: factor to be grouping
        :param exp_column: the column name of treatment
        :param func_dict: aggregate function dict
        :param sample_size: sample size per group
        :param seed: //
        :return:
        group_data: a data frame after grouping
        """
        return self.__get_group_data(data, column_name_for_group, group_list, exp_column, func_dict,
                                     sample_size=sample_size, seed=seed)