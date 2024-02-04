# 去最值后求平均
def cal_mean(series, type=None):
    series.sort()
    if type == 'without_max':
    	new_series = series[0: len(series)-1]
    elif type == 'without_min':
    	new_series = series[1: ]
    elif type == 'without_both':
    	new_series = series[1: len(series)-1]
    else:
    	new_series = series 
    mean_value = sum(new_series)/len(new_series)
    return mean_value