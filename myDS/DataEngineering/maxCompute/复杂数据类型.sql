--构建复杂数据格式的临时表
create table table_name 
(
    field_name     map<string, string> comment 'field_name'    --虽然定义为string，数值仍然可以相加；
)


select
    map('field01', value01,
        'field02', value02
       ) as field_name         --通过map函数构建
    ,str_to_map
--####################################################################################################
--map\struct\json\\array