select
    length('abcedfg')      --字符串长度
    ,reverse('abcedfg')        --反转
    ,concat('abc','def','gh')  --拼接
    ,concat_ws(',','abc','def','gh')
    
    --字符串裁剪
    ,substr('abcde', 1, 4)
    ,upper('abSEd')            --大写
    ,lower('abSEd')
    ,trim(' abc ')             --去除字符串两边的空格

    --正则表达式
    ,regexp_replace('foobar', 'oo|ar', '')

    --数学函数
    ,round(10.234)                  --10, 返回DOUBLE型的d的BIGINT类型的近似值
	,round(10.234, 1)               --10.2, 返回DOUBLE型的d的保留n位小数的DOUBLE类型的近似值
	,floor(10.234)                  --10, 是DOUBLE类型的，返回<=d的最大的BIGINT值
	,ceil(10.234)                   --11, 是DOUBLE类型的，返回>=d的最小的BIGINT值
	,rand()                         --0.7075876695466097 
	,rand(50)                       --0.7297136425657874, 每行返回一个DOUBLE型的随机数，整数seed是随机因子

	,exp(DOUBLE d)                     --返回e的d幂次方
	,ln(DOUBLE d)                     --以自然数为底d的对数
	,log10(DOUBLE d)                  -- 以10为底的d的对数
	,log2(DOUBLE d)                   --以2为底的d的对数
	,log(DOUBLE base,DOUBLE d)        --以base为底的d的对数
	,power(DOUBLE d,DOUBLE p)         --计算d的p次幂
	,sqrt(DOUBLE d)                   --d的平方根
	
	,pmod(INT i1 ,INT i2)             --i1对i2取模

	,abs(DOUBLE d)                 --计算d的绝对值
	,positive(DOUBLE d)           --返回+d
	,negative(DOUBLE d)           --返回-d
	,sign(DOUBLE d)               --如果d是正数，则返回+1.0，如果d是负数，则返回-1.0，否则为0