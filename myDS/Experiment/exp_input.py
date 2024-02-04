import os
import inspect
import warnings
import pandas as pd
from os import path

from pandas.api.types import is_numeric_dtype

# __all__ = ['read', 'save', 'encode']


class InputCheck:
    known_column = ['city_id', 'driver_id', 'pid', 'passenger_id']

    def __init__(self, addr='.', col_id='_', **kward):
        self.file_path = addr
        self.col_id = col_id
        self.kward = dict(kward)
        self.schema = {'block': [],
                       'measure': [],
                       'identity': [],
                       'group': str()}
        self.file_type = self.__file_type()
        self.df = self.__parse_file(**kward)
        self.__data_validation()
        if self.col_id != '_':
            self.__value_check()
        self.data_ready_flag = True

    def __file_type(self):
        if self.file_path.endswith('csv'):
            file_type = 'csv'
        elif self.file_path.endswith('tsv'):
            file_type = 'tsv'
        elif self.file_path.endswith('xlsx') or self.file_path.endswith('xls'):
            file_type = 'xlsx'
        else:
            file_type = 'other'
            raise Warning('当前格式的文件可能不会被正确解析')
        return file_type

    def __data_validation(self):
        # print('----------Data Validation------------')
        # print('before going furthur, we need some info about your data')
        # print('here we got several columns in your data input as follows')
        data_format = {}
        for i in list(self.df.columns):
            if i.lower() in self.known_column:
                data_format[i] = 'category'
        self.df.astype(dtype=data_format)
        return

    def define_schema(self):
        print('----------数据元信息输入------------')
        print('以下输入数据中所有数据列名')
        print(*list(self.df.columns), sep = ", ")
        valid_measure, valid_block, valid_group = False, False, False
        while valid_measure == False:
            m_input = input('请输入实验评估指标对应列名: ')
            if m_input not in self.df.columns:
                print('输入的列名不存在，请重新输入')
            else:
                valid_measure = True
        while valid_block is False:
            invalid = list()
            b_input = input('请输入分层信息(block)对应的列名(以,分隔): ')
            if ',' in b_input:
                b_input = b_input.split(',')
            else:
                print('single block')
                b_input = [b_input]
            for i in range(0, len(b_input)):
                if b_input[i] not in self.df.columns:
                    invalid.append(b_input[i])
            if len(invalid) > 0:
                print('输入的列名%s不存在，请重新输入' % ','.join(map(str, invalid)))
            else:
                valid_block = True
        while valid_group is False:
            g_input = input('请输入实验单元实验分组标签对应的列名: ')
            if g_input not in self.df.columns:
                print('输入的列名不存在，请重新输入')
            else:
                valid_group = True

        self.schema['measure'] = m_input
        self.schema['block'] = b_input
        self.schema['group'] = g_input
        return

    def __outlier_exclude(self, low=0, high=0.99):
        quant_df = self.df.quantile([low, high])
        for name in list(self.df.columns):
            if is_numeric_dtype(self.df[name]):
                self.df = self.df[(self.df[name] >
                                   quant_df.loc[low, name])&(self.df[name] < quant_df.loc[high, name])]
        return

    def __parse_file(self, **kwargs):
        """Read file with **kwargs; files supported: xls, xlsx, csv, csv.gz, pkl"""
        read_map = {'xls': pd.read_excel, 'xlsx': pd.read_excel, 'csv': pd.read_csv,
                    'gz': pd.read_csv, 'pkl': pd.read_pickle}
        ext = os.path.splitext(self.file_path)[1].lower()[1:]
        assert ext in read_map, """Input file not in correct format, must be xls,
                                 xlsx, csv, csv.gz, pkl; current format '{0}'""".format(ext)
        assert os.path.isfile(self.file_path), "File Not Found Exception '{0}'.".format(self.file_path)
        return read_map[ext](self.file_path, **kwargs)

    def __value_check(self):
        print('------------数据质量检测-----------')
        if len(self.df[self.col_id].drop_duplicates()) < len(self.df[self.col_id]):
            # raise Warning('there are multiple records for one item in the data')
            warnings.warn('多个重复的实验单元ID')
        if self.df[self.col_id].isna().sum() > 0:
            warnings.warn('存在未被标识的实验单元ID')
            self.df[self.col_id].fillna(0)
        if self.df.isna().values.sum() > 0:
            self.df.fillna(0)
            warnings.warn('存在无效值，且由0替代')
        return

    def bootstrap(v, sample_size=1000, n_samples=1000):
        return [np.random.choice(v, sample_size).mean() for _ in range(n_samples)]

    def save(addr, data, **kward):
        '''to save some temp files
        '''
        data.save(addr, **kward)
        return

    def encode(self, code='cp936'):
        '''change the python environment encode
            to deal with the encoding issues, there might be encoding issues between
            mac and pc
        '''
        import sys
        if sys.version_info.major == 2:
            stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
            reload(sys)
            sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde
            from sys import setdefaultencoding
            setdefaultencoding(code)