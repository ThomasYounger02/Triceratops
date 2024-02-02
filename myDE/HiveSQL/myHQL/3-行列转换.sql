--宽格式转换为长格式
select
	field_1
	,field_2
	,index_name
	,index_value
from
	(
	select 
		field_1
		,field_2
		,map(
			'index_name_1', index_value_1
			,'index_name_2', index_value_2
			) as index_map
	from
		(--origin table
		select
			field_1
			,field_2
			,index_value_1
			,index_value_2
		from
		    origin_table
		) a 
	) t0
	lateral view explode(index_map) lv as index_name, index_value