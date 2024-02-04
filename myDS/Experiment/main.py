# -*- encoding: utf-8 -*-

import os
import pandas as pd
import statsmodels.formula.api as smf
import seaborn as sns
from matplotlib import pyplot as plt

from experiment_auto import exp_input, rcb_assessment  #, compare_position, compare_scaler

ABS_PATH = os.path.abspath(os.path.dirname(__file__))


def running():
    data_input = exp_input.InputCheck(addr=os.path.join(ABS_PATH, 'data', INPUT_PATH))
    data_input.define_schema()
    model_assess = rcb_assessment.RCBAutomatedAssessment()
    training_data = model_assess.get_group_data(data_input.df, data_input.schema['block'],
                                                data_input.schema['group'], ['mean'],
                                                data_input.schema['measure'],
                                                max_block_num=min(len(data_input.schema['block']),3),
                                                verbose=True)
    try:
        training_data.columns = training_data.columns.droplevel(1)
        print('drop level')
    except:
        print('pass')
        pass
    print(training_data.head())
    blocking_factor_list = ([data_input.schema['group']] +
                            [i for i in data_input.schema['block'] if i in training_data.columns])
    included = ['C(%s)' % data_input.schema['group']]
    feature = model_assess.get_cross_feature(['C({})'.format(i) for i in blocking_factor_list], num=2)
    feature = [':'.join(i) for i in feature]
    fe = model_assess.stepwise_selection(data=training_data.copy(),
                                         response=data_input.schema['measure'],
                                         select_type='group',
                                         initial_list=included,
                                         full_feature=feature,
                                         threshold_in=0.01,
                                         threshold_out=0.07,
                                         verbose=True,
                                         max_iteration=20)
    print('remain feature: ', model_assess.feature)
    model_assess.feature = (['C(%s)' % data_input.schema['group']] +
                            [i for i in model_assess.feature if i != 'C(%s)' % data_input.schema['group']])
    formula = '{} ~ {} + 1'.format(data_input.schema['measure'], '+'.join(model_assess.feature))
    model = smf.ols(formula=formula, data=training_data).fit()
    print(model.summary())
    model_assess.multi_col_linearity_test(training_data, formula, 2)
    f, ax = plt.subplots(figsize=(6, 6))
    sns.kdeplot(model.resid)
    plt.show()


if __name__ == "__main__":
    INPUT_PATH = input('请输入实验数据文件名: ')
    running()