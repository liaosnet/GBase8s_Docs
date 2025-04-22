# wm_concat兼容函数存储过程写法  
带分隔符写法(分隔符少于10个字节)  
```sql
DROP FUNCTION IF EXISTS wm_concat_ws_init;
-- p_delimiter : delimiter, default ','
CREATE dba FUNCTION  wm_concat_ws_init (p_dummy varchar(255), p_delimiter varchar(10) default ',')
  RETURNING varchar(255) with (not variant);
  -- length of delimident & delimident
  RETURN CHAR_LENGTH(p_delimiter) || p_delimiter;
END FUNCTION;

DROP FUNCTION IF EXISTS wm_concat_ws_iter;
-- p_iter_result : iter result
-- p_next_value  : iter next value
CREATE dba FUNCTION  wm_concat_ws_iter (p_iter_result varchar(255), p_next_value varchar(255))
  RETURNING varchar(255) with (not variant);
  DEFINE v_del_str varchar(10);
  DEFINE v_del_len smallint;
  LET v_del_len = left(p_iter_result,1) + 0;
  LET v_del_str = substr(p_iter_result,2,v_del_len);
  RETURN p_iter_result || p_next_value || v_del_str;
END FUNCTION;

DROP FUNCTION IF EXISTS wm_concat_ws_combine;
CREATE dba FUNCTION  wm_concat_ws_combine(p_partial1 varchar(255), p_partial2 varchar(255))
  RETURNING varchar(255) with (not variant);
  RETURN p_partial1 || p_partial2;
END FUNCTION;

DROP FUNCTION IF EXISTS wm_concat_ws_final;
-- p_final : finish iter result
CREATE dba FUNCTION  wm_concat_ws_final(p_final varchar(255))
  RETURNING varchar(255) with (not variant);
  DEFINE v_str_len int;
  DEFINE v_del_len smallint;
  ON EXCEPTION
    RETURN null;
  END EXCEPTION;
  IF p_final IS NULL OR p_final = '' THEN
    RETURN null;
  ELSE
    LET v_del_len = left(p_final,1);
    LET v_str_len = CHAR_LENGTH(p_final) - 2 * v_del_len - 1;
	-- remove head and tail p_delimiter and first number
    RETURN substr(p_final,v_del_len + 2,v_str_len);
  END IF;
END FUNCTION;

DROP aggregate if exists wm_concat_ws;
-- param1 : column for aggregate
-- param2 : delimiter to init (p_delimiter)
create aggregate wm_concat_ws with
(
  INIT = wm_concat_ws_init,
  ITER = wm_concat_ws_iter,
  COMBINE = wm_concat_ws_combine,
  FINAL = wm_concat_ws_final
);
```
示例：  
```sql
SELECT col1,wm_concat_ws(col2,'###')
FROM tab11
GROUP BY col1;
```