# Python Script Examples in NiFi
This space contains python script examples for using in Apache NiFi's scripting components, especially the ExecuteScript processor.


## ExecuteScript Samples
| Script             | Description                                       |
| :----------------- | :------------------------------------------------ |
| update_attribute.py | Read flowfile and update flowfile's attributes |
| simple_write_content.py | Update flowfile content |
| read_update_content.py| Read and overwrite content |
| json_to_string_transform.py| Read JSON and transform to string |
| nested_json_to_string_transform.py | Read nested JSON and transform to string |
| json_transform.py  | Update content of JSON format flowfile                       |
| nested_json_transform.py | Update content of nested JSON format flowfile |



 


## Variable used in ExecuteScript
 | Variable Name | Description          |
 | :------------ | :------------------- |
 | session       | ProcessSession       |
 | context       | ProcessContext       |
 | log           | Log Component        |
 | REL_SUCCESS   | Success Relationship |
 | REL_FAILURE   | Failure Relationship |

## Reference:
* [BatchIQ](https://github.com/BatchIQ/nifi-scripting-samples)
* [ExecuteScript Cookbook](https://community.hortonworks.com/articles/75032/executescript-cookbook-part-1.html)
