# iengage_client.BPMApi

All URIs are relative to *https://api.iengage.io:8243/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_wf_task**](BPMApi.md#assign_wf_task) | **POST** /bpm/tasks/{taskId}/assign | Assign task
[**complete_wf_task**](BPMApi.md#complete_wf_task) | **POST** /bpm/tasks/{taskId}/complete | Complete task
[**get_bpm_tasks**](BPMApi.md#get_bpm_tasks) | **GET** /bpm/tasks/{taskId} | Get task by task id
[**get_search_task**](BPMApi.md#get_search_task) | **GET** /bpm/{userId}/tasks/name | Get list of BPM task assigned to user
[**get_tasks_by_entity**](BPMApi.md#get_tasks_by_entity) | **GET** /bpm/{userId}/tasks/{entityId} | Get list of BPM task assigned to user
[**get_user_bpm_tasks**](BPMApi.md#get_user_bpm_tasks) | **GET** /bpm/{userId}/tasks | Get list of BPM task assigned to user
[**get_user_roles_bpm_tasks**](BPMApi.md#get_user_roles_bpm_tasks) | **GET** /bpm/{userId}/roles/tasks | Get list of BPM task assigned to user roles


# **assign_wf_task**
> VerveResponseWFTask assign_wf_task(assignee_user_id, task_id, logged_in_user_id, access_token, client_token, comment=comment, due_date=due_date, fields=fields)

Assign task

Assign BPM task, It will return task object

### Example 
```python
from __future__ import print_statement
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.BPMApi()
assignee_user_id = 789 # int | assigneeUserId - assign to this user
task_id = 789 # int | taskId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
comment = 'comment_example' # str | comment (optional)
due_date = 789 # int | dueDate (optional)
fields = 'taskId,name,type' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)name<br/>3)type<br/><b>A) Available values -</b> <br/>1)taskId<br/>2)name<br/>3)dueDate<br/>4)description<br/>5)transitionList<br/>6)type<br/>7)entityId<br/>8)attributes (optional) (default to taskId,name,type)

try: 
    # Assign task
    api_response = api_instance.assign_wf_task(assignee_user_id, task_id, logged_in_user_id, access_token, client_token, comment=comment, due_date=due_date, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BPMApi->assign_wf_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignee_user_id** | **int**| assigneeUserId - assign to this user | 
 **task_id** | **int**| taskId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **comment** | **str**| comment | [optional] 
 **due_date** | **int**| dueDate | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)type&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)dueDate&lt;br/&gt;4)description&lt;br/&gt;5)transitionList&lt;br/&gt;6)type&lt;br/&gt;7)entityId&lt;br/&gt;8)attributes | [optional] [default to taskId,name,type]

### Return type

[**VerveResponseWFTask**](VerveResponseWFTask.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_wf_task**
> VerveResponseWFTask complete_wf_task(user_id, task_id, logged_in_user_id, access_token, client_token, transition=transition, comment=comment, fields=fields)

Complete task

Complete BPM task, It will return task object

### Example 
```python
from __future__ import print_statement
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.BPMApi()
user_id = 789 # int | userId whose task want to complete
task_id = 789 # int | taskId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
transition = 'transition_example' # str | transition (optional)
comment = 'comment_example' # str | comment (optional)
fields = 'taskId,name,type' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)name<br/>3)type<br/><b>A) Available values -</b> <br/>1)taskId<br/>2)name<br/>3)dueDate<br/>4)description<br/>5)transitionList<br/>6)type<br/>7)entityId<br/>8)attributes (optional) (default to taskId,name,type)

try: 
    # Complete task
    api_response = api_instance.complete_wf_task(user_id, task_id, logged_in_user_id, access_token, client_token, transition=transition, comment=comment, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BPMApi->complete_wf_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId whose task want to complete | 
 **task_id** | **int**| taskId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **transition** | **str**| transition | [optional] 
 **comment** | **str**| comment | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)type&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)dueDate&lt;br/&gt;4)description&lt;br/&gt;5)transitionList&lt;br/&gt;6)type&lt;br/&gt;7)entityId&lt;br/&gt;8)attributes | [optional] [default to taskId,name,type]

### Return type

[**VerveResponseWFTask**](VerveResponseWFTask.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bpm_tasks**
> VerveResponseWFTask get_bpm_tasks(user_id, task_id, logged_in_user_id, access_token, client_token, fields=fields)

Get task by task id

Return the BPM task

### Example 
```python
from __future__ import print_statement
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.BPMApi()
user_id = 789 # int | userId
task_id = 789 # int | taskId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'taskId,name,type' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)name<br/>3)type<br/><b>A) Available values -</b> <br/>1)taskId<br/>2)name<br/>3)dueDate<br/>4)description<br/>5)transitionList<br/>6)type<br/>7)entityId<br/>8)attributes (optional) (default to taskId,name,type)

try: 
    # Get task by task id
    api_response = api_instance.get_bpm_tasks(user_id, task_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BPMApi->get_bpm_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **task_id** | **int**| taskId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)type&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)dueDate&lt;br/&gt;4)description&lt;br/&gt;5)transitionList&lt;br/&gt;6)type&lt;br/&gt;7)entityId&lt;br/&gt;8)attributes | [optional] [default to taskId,name,type]

### Return type

[**VerveResponseWFTask**](VerveResponseWFTask.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_task**
> VerveResponseWFTaskList get_search_task(user_id, search_string, completed, search_by_user_roles, start, end, logged_in_user_id, access_token, client_token, type=type, organization_id=organization_id, fields=fields)

Get list of BPM task assigned to user

Return the list of BPM task

### Example 
```python
from __future__ import print_statement
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.BPMApi()
user_id = 789 # int | userId
search_string = 'search_string_example' # str | searchString
completed = true # bool | 1) true - Completed <br/> 2) false - Pending <br/>
search_by_user_roles = true # bool | 1) true - Assigned to roles <br/> 2) false - Assigned to user
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
type = 'type_example' # str | Type (optional)
organization_id = 789 # int | organizationId (optional)
fields = 'taskId,name,type' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)name<br/>3)type<br/><b>A) Available values -</b> <br/>1)taskId<br/>2)name<br/>3)dueDate<br/>4)description<br/>5)transitionList<br/>6)type<br/>7)entityId<br/>8)attributes (optional) (default to taskId,name,type)

try: 
    # Get list of BPM task assigned to user
    api_response = api_instance.get_search_task(user_id, search_string, completed, search_by_user_roles, start, end, logged_in_user_id, access_token, client_token, type=type, organization_id=organization_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BPMApi->get_search_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **search_string** | **str**| searchString | 
 **completed** | **bool**| 1) true - Completed &lt;br/&gt; 2) false - Pending &lt;br/&gt; | 
 **search_by_user_roles** | **bool**| 1) true - Assigned to roles &lt;br/&gt; 2) false - Assigned to user | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **type** | **str**| Type | [optional] 
 **organization_id** | **int**| organizationId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)type&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)dueDate&lt;br/&gt;4)description&lt;br/&gt;5)transitionList&lt;br/&gt;6)type&lt;br/&gt;7)entityId&lt;br/&gt;8)attributes | [optional] [default to taskId,name,type]

### Return type

[**VerveResponseWFTaskList**](VerveResponseWFTaskList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_by_entity**
> VerveResponseWFTaskList get_tasks_by_entity(user_id, entity_id, completed, search_by_user_roles, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of BPM task assigned to user

Return the list of BPM task

### Example 
```python
from __future__ import print_statement
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.BPMApi()
user_id = 789 # int | userId whose task want to see
entity_id = 789 # int | entityId
completed = true # bool | 1) true - Completed <br/> 2) false - Pending <br/>
search_by_user_roles = true # bool | 1) true - Assigned to roles <br/> 2) false - Assigned to user
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'taskId,name,type' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)name<br/>3)type<br/><b>A) Available values -</b> <br/>1)taskId<br/>2)name<br/>3)dueDate<br/>4)description<br/>5)transitionList<br/>6)type<br/>7)entityId<br/>8)attributes (optional) (default to taskId,name,type)

try: 
    # Get list of BPM task assigned to user
    api_response = api_instance.get_tasks_by_entity(user_id, entity_id, completed, search_by_user_roles, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BPMApi->get_tasks_by_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId whose task want to see | 
 **entity_id** | **int**| entityId | 
 **completed** | **bool**| 1) true - Completed &lt;br/&gt; 2) false - Pending &lt;br/&gt; | 
 **search_by_user_roles** | **bool**| 1) true - Assigned to roles &lt;br/&gt; 2) false - Assigned to user | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)type&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)dueDate&lt;br/&gt;4)description&lt;br/&gt;5)transitionList&lt;br/&gt;6)type&lt;br/&gt;7)entityId&lt;br/&gt;8)attributes | [optional] [default to taskId,name,type]

### Return type

[**VerveResponseWFTaskList**](VerveResponseWFTaskList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_bpm_tasks**
> VerveResponseWFTaskList get_user_bpm_tasks(user_id, completed, start, end, logged_in_user_id, access_token, client_token, type=type, organization_id=organization_id, fields=fields)

Get list of BPM task assigned to user

Return the list of BPM task

### Example 
```python
from __future__ import print_statement
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.BPMApi()
user_id = 789 # int | userId whose task want to see
completed = true # bool | 1) true - Completed <br/> 2) false - Pending <br/> 3) Blank - All
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
type = 'type_example' # str | Type (optional)
organization_id = 789 # int | organizationId (optional)
fields = 'taskId,name,type' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)name<br/>3)type<br/><b>A) Available values -</b> <br/>1)taskId<br/>2)name<br/>3)dueDate<br/>4)description<br/>5)transitionList<br/>6)type<br/>7)entityId<br/>8)attributes (optional) (default to taskId,name,type)

try: 
    # Get list of BPM task assigned to user
    api_response = api_instance.get_user_bpm_tasks(user_id, completed, start, end, logged_in_user_id, access_token, client_token, type=type, organization_id=organization_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BPMApi->get_user_bpm_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId whose task want to see | 
 **completed** | **bool**| 1) true - Completed &lt;br/&gt; 2) false - Pending &lt;br/&gt; 3) Blank - All | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **type** | **str**| Type | [optional] 
 **organization_id** | **int**| organizationId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)type&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)dueDate&lt;br/&gt;4)description&lt;br/&gt;5)transitionList&lt;br/&gt;6)type&lt;br/&gt;7)entityId&lt;br/&gt;8)attributes | [optional] [default to taskId,name,type]

### Return type

[**VerveResponseWFTaskList**](VerveResponseWFTaskList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles_bpm_tasks**
> VerveResponseWFTaskList get_user_roles_bpm_tasks(user_id, completed, start, end, logged_in_user_id, access_token, client_token, type=type, organization_id=organization_id, fields=fields)

Get list of BPM task assigned to user roles

Return the list of BPM task

### Example 
```python
from __future__ import print_statement
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.BPMApi()
user_id = 789 # int | userId whose task want to see
completed = true # bool | 1) true - Completed <br/> 2) false - Pending <br/> 3) Blank - All
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
type = 'type_example' # str | Type (optional)
organization_id = 789 # int | organizationId (optional)
fields = 'taskId,name,type' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)name<br/>3)type<br/><b>A) Available values -</b> <br/>1)taskId<br/>2)name<br/>3)dueDate<br/>4)description<br/>5)transitionList<br/>6)type<br/>7)entityId<br/>8)attributes (optional) (default to taskId,name,type)

try: 
    # Get list of BPM task assigned to user roles
    api_response = api_instance.get_user_roles_bpm_tasks(user_id, completed, start, end, logged_in_user_id, access_token, client_token, type=type, organization_id=organization_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BPMApi->get_user_roles_bpm_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId whose task want to see | 
 **completed** | **bool**| 1) true - Completed &lt;br/&gt; 2) false - Pending &lt;br/&gt; 3) Blank - All | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **type** | **str**| Type | [optional] 
 **organization_id** | **int**| organizationId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)type&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)name&lt;br/&gt;3)dueDate&lt;br/&gt;4)description&lt;br/&gt;5)transitionList&lt;br/&gt;6)type&lt;br/&gt;7)entityId&lt;br/&gt;8)attributes | [optional] [default to taskId,name,type]

### Return type

[**VerveResponseWFTaskList**](VerveResponseWFTaskList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

