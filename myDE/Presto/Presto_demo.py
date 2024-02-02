import numpy as np 
import pandas as pd 
import prestodb
import sys

import warnings
warnings.filterwarnings('ignore')


def Presto(sql):
    '''
    connect to database with presto。

        Args:
            sql(string): sql files。

        Returns:
            df_data(dataframe): data in dataframe。
    '''
    conn=prestodb.dbapi.connect(
        host='0.0.0.0',
        port=8888,
        user='user',
        password='password',
        catalog='hive'
        )
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    df_data = pd.DataFrame(rows)
    return df_data