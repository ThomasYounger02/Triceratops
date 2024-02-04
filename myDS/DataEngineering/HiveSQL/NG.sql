https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Select

--官方select语句构成
SELECT 
    [ALL | DISTINCT] select_expr, select_expr, ...
FROM 
    table_reference
[WHERE where_condition]
[GROUP BY col_list]
[ORDER BY col_list]
[CLUSTER BY col_list | [DISTRIBUTE BY col_list] 
[SORT BY col_list]
[LIMIT [offset,] rows]



--sql style
- Use lowercase SQL;
- Left align everything;
- Use single quotes `''`;
- Use `!=` over `<>`;
- Break long lists of in values into multiple indented lines;
- Table names should be a plural `snake_case` of the noun;
- Column names should be `snake_case`;
    - Boolean fields should be prefixed with `is_`, `has_`, or `does_`. For example, `is_customer`, `has_unsubscribed`, etc.
    - Date-only fields should be suffixed with `_date`. For example, `report_date`.
    - Date+time fields should be suffixed with `_at`. For example, `created_at`, `posted_at`, etc.
- Use `as` to alias column names

