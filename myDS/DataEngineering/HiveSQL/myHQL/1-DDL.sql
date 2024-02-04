

##########################################################################################################################################
--Create Table
CREATE TABLE IF NOT EXITS table_name
(
    field_bigint bigint comment 'comment of field'
    ,field_string string comment 'comment of field'
    ,field_map map<string, string> comment 'comment of field'
)
COMMENT 'comment of table'
PARTITIONED BY (dt string comment 'comment of partition');

INSERT OVERWRITE TABLE table_name PARTITION (dt='${date_var}')
