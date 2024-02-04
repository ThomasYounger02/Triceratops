--建表
DROP TABLE IF EXISTS new_table;
CREATE TABLE IF NOT EXISTS new_table
(
    city_id                      bigint                 comment '城市ID'
    ,extra                       map<string, string>    comment '其他指标'
)
COMMENT 'the description of new_table'
PARTITIONED BY (dt string comment '日期')
LIFECYCLE 9999;

--插入
INSERT OVERWRITE TABLE new_table PARTITION (dt='biz_date')