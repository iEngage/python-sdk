# iengage-client.ProjectManagementApi

All URIs are relative to *https://api.iengage.io:8243/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_milestone_comment**](ProjectManagementApi.md#add_milestone_comment) | **POST** /milestones/{milestoneId}/comments | Comment on milestone
[**add_task_comment**](ProjectManagementApi.md#add_task_comment) | **POST** /milestones/tasks/{taskId}/comments | Comment on task
[**create_milestone**](ProjectManagementApi.md#create_milestone) | **POST** /milestones | Create milestone
[**create_task**](ProjectManagementApi.md#create_task) | **POST** /milestones/{milestoneId}/tasks | Create task
[**delete_milestone**](ProjectManagementApi.md#delete_milestone) | **DELETE** /milestones/{milestoneId} | Delete milestone
[**delete_task**](ProjectManagementApi.md#delete_task) | **DELETE** /milestones/tasks/{taskId} | Delete task
[**get_milestones**](ProjectManagementApi.md#get_milestones) | **GET** /milestones | Get list of milestones
[**get_milestones_comments**](ProjectManagementApi.md#get_milestones_comments) | **GET** /milestones/{milestoneId}/comments | Get list of comments written on Milestones
[**get_task_comments**](ProjectManagementApi.md#get_task_comments) | **GET** /milestones/tasks/{taskId}/comments | Get list of Comments written on task
[**get_user_tasks**](ProjectManagementApi.md#get_user_tasks) | **GET** /milestones/tasks/{userId}/assigned | Get list of task assigned to user
[**update_milestone**](ProjectManagementApi.md#update_milestone) | **PUT** /milestones/{milestoneId} | Update milestone
[**update_task**](ProjectManagementApi.md#update_task) | **PUT** /milestones/tasks/{taskId} | Update task
[**update_task_status**](ProjectManagementApi.md#update_task_status) | **PUT** /milestones/tasks/{taskId}/status | Update task status


# **add_milestone_comment**
> VerveResponseComment add_milestone_comment(milestone_id, comment_text, logged_in_user_id, access_token, client_token)

Comment on milestone

Allows the user to comment on milestone. Returns the comments

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
milestone_id = 789 # int | milestoneId
comment_text = 'comment_text_example' # str | commentText
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Comment on milestone
    api_response = api_instance.add_milestone_comment(milestone_id, comment_text, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->add_milestone_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_id** | **int**| milestoneId | 
 **comment_text** | **str**| commentText | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseComment**](VerveResponseComment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_task_comment**
> VerveResponseComment add_task_comment(task_id, comment_text, logged_in_user_id, access_token, client_token)

Comment on task

Allows  the user to comment on task. Returns the task comment

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
task_id = 789 # int | taskId
comment_text = 'comment_text_example' # str | commentText
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Comment on task
    api_response = api_instance.add_task_comment(task_id, comment_text, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->add_task_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| taskId | 
 **comment_text** | **str**| commentText | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseComment**](VerveResponseComment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_milestone**
> VerveResponseMilestone create_milestone(title, description, due_date, never_due, logged_in_user_id, access_token, client_token, organization_id=organization_id, fields=fields)

Create milestone

Allows the user to create milestone. Returns the created milestone

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
title = 'title_example' # str | title
description = 'description_example' # str | description
due_date = 'due_date_example' # str | Due date(Format: MM-dd-yyyy HH:mm:ss a)
never_due = true # bool | neverDue. If neverDue is true, it takes higher priority than dueDate
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
organization_id = 789 # int | organizationId (optional)
fields = 'milestoneId,milestoneTitle,milestoneDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)milestoneId<br/>2)milestoneTitle<br/>3)milestoneDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)milestoneId<br/>2)milestoneTitle<br/>3)milestoneDescription<br/>4)createdDate<br/>5)status<br/>6)priority<br/>7)dueDate (optional) (default to milestoneId,milestoneTitle,milestoneDescription,createdDate)

try: 
    # Create milestone
    api_response = api_instance.create_milestone(title, description, due_date, never_due, logged_in_user_id, access_token, client_token, organization_id=organization_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->create_milestone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| title | 
 **description** | **str**| description | 
 **due_date** | **str**| Due date(Format: MM-dd-yyyy HH:mm:ss a) | 
 **never_due** | **bool**| neverDue. If neverDue is true, it takes higher priority than dueDate | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **organization_id** | **int**| organizationId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)milestoneId&lt;br/&gt;2)milestoneTitle&lt;br/&gt;3)milestoneDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)milestoneId&lt;br/&gt;2)milestoneTitle&lt;br/&gt;3)milestoneDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)status&lt;br/&gt;6)priority&lt;br/&gt;7)dueDate | [optional] [default to milestoneId,milestoneTitle,milestoneDescription,createdDate]

### Return type

[**VerveResponseMilestone**](VerveResponseMilestone.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> VerveResponseTask create_task(title, description, priority, assignee_user_id, due_date, never_due, milestone_id, logged_in_user_id, access_token, client_token, fields=fields)

Create task

Allows user to create task. Returns the created task

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
title = 'title_example' # str | title
description = 'description_example' # str | description
priority = 56 # int | Task priority <br/> 1 - HIGH <br/> 2 - LOW <br/> 3 - NORMAL
assignee_user_id = 789 # int | assignee User Id
due_date = 'due_date_example' # str | Due date (Format: MM-dd-yyyy HH:mm:ss a)
never_due = true # bool | neverDue. If neverDue is true, it takes higher priority than dueDate
milestone_id = 789 # int | Milestone Id
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'taskId,taskTitle,taskDescription,dueDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)taskTitle<br/>3)taskDescription<br/>4)dueDate<br/><b>A) Available values-</b><br/>1)taskId<br/>2)taskTitle<br/>3)taskDescription<br/>4)status<br/>5)priority<br/>6)dueDate<br/>7)milestoneName<br/>8)groupType<br/>9)groupName (optional) (default to taskId,taskTitle,taskDescription,dueDate)

try: 
    # Create task
    api_response = api_instance.create_task(title, description, priority, assignee_user_id, due_date, never_due, milestone_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| title | 
 **description** | **str**| description | 
 **priority** | **int**| Task priority &lt;br/&gt; 1 - HIGH &lt;br/&gt; 2 - LOW &lt;br/&gt; 3 - NORMAL | 
 **assignee_user_id** | **int**| assignee User Id | 
 **due_date** | **str**| Due date (Format: MM-dd-yyyy HH:mm:ss a) | 
 **never_due** | **bool**| neverDue. If neverDue is true, it takes higher priority than dueDate | 
 **milestone_id** | **int**| Milestone Id | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)taskTitle&lt;br/&gt;3)taskDescription&lt;br/&gt;4)dueDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)taskId&lt;br/&gt;2)taskTitle&lt;br/&gt;3)taskDescription&lt;br/&gt;4)status&lt;br/&gt;5)priority&lt;br/&gt;6)dueDate&lt;br/&gt;7)milestoneName&lt;br/&gt;8)groupType&lt;br/&gt;9)groupName | [optional] [default to taskId,taskTitle,taskDescription,dueDate]

### Return type

[**VerveResponseTask**](VerveResponseTask.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_milestone**
> VerveResponseMilestone delete_milestone(milestone_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete milestone

Allows the user to delete milestone. Returns the deleted milestone

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
milestone_id = 789 # int | milestoneId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'milestoneId,milestoneTitle,milestoneDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)milestoneId<br/>2)milestoneTitle<br/>3)milestoneDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)milestoneId<br/>2)milestoneTitle<br/>3)milestoneDescription<br/>4)createdDate<br/>5)status<br/>6)priority<br/>7)dueDate (optional) (default to milestoneId,milestoneTitle,milestoneDescription,createdDate)

try: 
    # Delete milestone
    api_response = api_instance.delete_milestone(milestone_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->delete_milestone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_id** | **int**| milestoneId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)milestoneId&lt;br/&gt;2)milestoneTitle&lt;br/&gt;3)milestoneDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)milestoneId&lt;br/&gt;2)milestoneTitle&lt;br/&gt;3)milestoneDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)status&lt;br/&gt;6)priority&lt;br/&gt;7)dueDate | [optional] [default to milestoneId,milestoneTitle,milestoneDescription,createdDate]

### Return type

[**VerveResponseMilestone**](VerveResponseMilestone.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> VerveResponseTask delete_task(task_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete task

Allows the user to delete task. Returns the deleted task

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
task_id = 789 # int | taskId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'taskId,taskTitle,taskDescription,dueDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)taskTitle<br/>3)taskDescription<br/>4)dueDate<br/><b>A) Available values-</b><br/>1)taskId<br/>2)taskTitle<br/>3)taskDescription<br/>4)status<br/>5)priority<br/>6)dueDate<br/>7)milestoneName<br/>8)groupType<br/>9)groupName (optional) (default to taskId,taskTitle,taskDescription,dueDate)

try: 
    # Delete task
    api_response = api_instance.delete_task(task_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| taskId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)taskTitle&lt;br/&gt;3)taskDescription&lt;br/&gt;4)dueDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)taskId&lt;br/&gt;2)taskTitle&lt;br/&gt;3)taskDescription&lt;br/&gt;4)status&lt;br/&gt;5)priority&lt;br/&gt;6)dueDate&lt;br/&gt;7)milestoneName&lt;br/&gt;8)groupType&lt;br/&gt;9)groupName | [optional] [default to taskId,taskTitle,taskDescription,dueDate]

### Return type

[**VerveResponseTask**](VerveResponseTask.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_milestones**
> VerveResponseMilestoneList get_milestones(logged_in_user_id, access_token, client_token, organization_id=organization_id, fields=fields)

Get list of milestones

Returns the list of milestones

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
organization_id = 789 # int | organizationId (optional)
fields = 'milestoneId,milestoneTitle,milestoneDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)milestoneId<br/>2)milestoneTitle<br/>3)milestoneDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)milestoneId<br/>2)milestoneTitle<br/>3)milestoneDescription<br/>4)createdDate<br/>5)status<br/>6)priority<br/>7)dueDate (optional) (default to milestoneId,milestoneTitle,milestoneDescription,createdDate)

try: 
    # Get list of milestones
    api_response = api_instance.get_milestones(logged_in_user_id, access_token, client_token, organization_id=organization_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->get_milestones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **organization_id** | **int**| organizationId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)milestoneId&lt;br/&gt;2)milestoneTitle&lt;br/&gt;3)milestoneDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)milestoneId&lt;br/&gt;2)milestoneTitle&lt;br/&gt;3)milestoneDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)status&lt;br/&gt;6)priority&lt;br/&gt;7)dueDate | [optional] [default to milestoneId,milestoneTitle,milestoneDescription,createdDate]

### Return type

[**VerveResponseMilestoneList**](VerveResponseMilestoneList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_milestones_comments**
> VerveResponseCommentList get_milestones_comments(milestone_id, logged_in_user_id, access_token, client_token)

Get list of comments written on Milestones

Returns the list comments written on milestone

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
milestone_id = 789 # int | milestoneId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Get list of comments written on Milestones
    api_response = api_instance.get_milestones_comments(milestone_id, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->get_milestones_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_id** | **int**| milestoneId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseCommentList**](VerveResponseCommentList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_comments**
> VerveResponseCommentList get_task_comments(task_id, logged_in_user_id, access_token, client_token)

Get list of Comments written on task

Returns the list of comments written on task

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
task_id = 789 # int | taskId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Get list of Comments written on task
    api_response = api_instance.get_task_comments(task_id, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->get_task_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| taskId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseCommentList**](VerveResponseCommentList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_tasks**
> VerveResponseTaskList get_user_tasks(user_id, status, logged_in_user_id, access_token, client_token, fields=fields)

Get list of task assigned to user

Returns the list of task assigned to user

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
user_id = 789 # int | userId
status = 56 # int | Task status <br/> 0 - ALL <br/> 1 - OPEN <br/> 2 - PERCENT_TWENTY <br/> 3 - PERCENT_FORTY <br/> 4 - PERCENT_SIXTY <br/> 5 - PERCENT_EIGHTY <br/> 6 - RESOLVED <br/> 7 - REOPENED
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'taskId,taskTitle,taskDescription,dueDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)taskTitle<br/>3)taskDescription<br/>4)dueDate<br/><b>A) Available values-</b><br/>1)taskId<br/>2)taskTitle<br/>3)taskDescription<br/>4)status<br/>5)priority<br/>6)dueDate<br/>7)milestoneName<br/>8)groupType<br/>9)groupName (optional) (default to taskId,taskTitle,taskDescription,dueDate)

try: 
    # Get list of task assigned to user
    api_response = api_instance.get_user_tasks(user_id, status, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->get_user_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **status** | **int**| Task status &lt;br/&gt; 0 - ALL &lt;br/&gt; 1 - OPEN &lt;br/&gt; 2 - PERCENT_TWENTY &lt;br/&gt; 3 - PERCENT_FORTY &lt;br/&gt; 4 - PERCENT_SIXTY &lt;br/&gt; 5 - PERCENT_EIGHTY &lt;br/&gt; 6 - RESOLVED &lt;br/&gt; 7 - REOPENED | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)taskTitle&lt;br/&gt;3)taskDescription&lt;br/&gt;4)dueDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)taskId&lt;br/&gt;2)taskTitle&lt;br/&gt;3)taskDescription&lt;br/&gt;4)status&lt;br/&gt;5)priority&lt;br/&gt;6)dueDate&lt;br/&gt;7)milestoneName&lt;br/&gt;8)groupType&lt;br/&gt;9)groupName | [optional] [default to taskId,taskTitle,taskDescription,dueDate]

### Return type

[**VerveResponseTaskList**](VerveResponseTaskList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_milestone**
> VerveResponseMilestone update_milestone(milestone_id, title, description, due_date, logged_in_user_id, access_token, client_token, fields=fields)

Update milestone

Allows the user to update milestone. Returns the updated milestone

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
milestone_id = 789 # int | milestoneId
title = 'title_example' # str | title
description = 'description_example' # str | description
due_date = 'due_date_example' # str | Due date (Format: MM-dd-yyyy HH:mm:ss a)
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'milestoneId,milestoneTitle,milestoneDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)milestoneId<br/>2)milestoneTitle<br/>3)milestoneDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)milestoneId<br/>2)milestoneTitle<br/>3)milestoneDescription<br/>4)createdDate<br/>5)status<br/>6)priority<br/>7)dueDate (optional) (default to milestoneId,milestoneTitle,milestoneDescription,createdDate)

try: 
    # Update milestone
    api_response = api_instance.update_milestone(milestone_id, title, description, due_date, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->update_milestone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_id** | **int**| milestoneId | 
 **title** | **str**| title | 
 **description** | **str**| description | 
 **due_date** | **str**| Due date (Format: MM-dd-yyyy HH:mm:ss a) | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)milestoneId&lt;br/&gt;2)milestoneTitle&lt;br/&gt;3)milestoneDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)milestoneId&lt;br/&gt;2)milestoneTitle&lt;br/&gt;3)milestoneDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)status&lt;br/&gt;6)priority&lt;br/&gt;7)dueDate | [optional] [default to milestoneId,milestoneTitle,milestoneDescription,createdDate]

### Return type

[**VerveResponseMilestone**](VerveResponseMilestone.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> VerveResponseTask update_task(task_id, title, description, due_date, status, re_assignee_user_id, logged_in_user_id, access_token, client_token, fields=fields)

Update task

Allows the user to update task. Returns the updated task

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
task_id = 789 # int | taskId
title = 'title_example' # str | title
description = 'description_example' # str | description
due_date = 'due_date_example' # str | Due date
status = 56 # int | Task status <br/> 1 - OPEN <br/> 2 - PERCENT_TWENTY <br/> 3 - PERCENT_FORTY <br/> 4 - PERCENT_SIXTY <br/> 5 - PERCENT_EIGHTY <br/> 6 - RESOLVED <br/> 7 - REOPENED
re_assignee_user_id = 789 # int | re-assignee User Id
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'taskId,taskTitle,taskDescription,dueDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)taskTitle<br/>3)taskDescription<br/>4)dueDate<br/><b>A) Available values-</b><br/>1)taskId<br/>2)taskTitle<br/>3)taskDescription<br/>4)status<br/>5)priority<br/>6)dueDate<br/>7)milestoneName<br/>8)groupType<br/>9)groupName (optional) (default to taskId,taskTitle,taskDescription,dueDate)

try: 
    # Update task
    api_response = api_instance.update_task(task_id, title, description, due_date, status, re_assignee_user_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| taskId | 
 **title** | **str**| title | 
 **description** | **str**| description | 
 **due_date** | **str**| Due date | 
 **status** | **int**| Task status &lt;br/&gt; 1 - OPEN &lt;br/&gt; 2 - PERCENT_TWENTY &lt;br/&gt; 3 - PERCENT_FORTY &lt;br/&gt; 4 - PERCENT_SIXTY &lt;br/&gt; 5 - PERCENT_EIGHTY &lt;br/&gt; 6 - RESOLVED &lt;br/&gt; 7 - REOPENED | 
 **re_assignee_user_id** | **int**| re-assignee User Id | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)taskTitle&lt;br/&gt;3)taskDescription&lt;br/&gt;4)dueDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)taskId&lt;br/&gt;2)taskTitle&lt;br/&gt;3)taskDescription&lt;br/&gt;4)status&lt;br/&gt;5)priority&lt;br/&gt;6)dueDate&lt;br/&gt;7)milestoneName&lt;br/&gt;8)groupType&lt;br/&gt;9)groupName | [optional] [default to taskId,taskTitle,taskDescription,dueDate]

### Return type

[**VerveResponseTask**](VerveResponseTask.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_status**
> VerveResponseTask update_task_status(task_id, status, logged_in_user_id, access_token, client_token, fields=fields)

Update task status

Allows the user to update task status. Returns the updated task status

### Example 
```python
from __future__ import print_statement
import time
import iengage-client
from iengage-client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage-client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage-client.ProjectManagementApi()
task_id = 789 # int | taskId
status = 56 # int | Task status <br/> 1 - OPEN <br/> 2 - PERCENT_TWENTY <br/> 3 - PERCENT_FORTY <br/> 4 - PERCENT_SIXTY <br/> 5 - PERCENT_EIGHTY <br/> 6 - RESOLVED <br/> 7 - REOPENED
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'taskId,taskTitle,taskDescription,dueDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)taskId<br/>2)taskTitle<br/>3)taskDescription<br/>4)dueDate<br/><b>A) Available values-</b><br/>1)taskId<br/>2)taskTitle<br/>3)taskDescription<br/>4)status<br/>5)priority<br/>6)dueDate<br/>7)milestoneName<br/>8)groupType<br/>9)groupName (optional) (default to taskId,taskTitle,taskDescription,dueDate)

try: 
    # Update task status
    api_response = api_instance.update_task_status(task_id, status, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectManagementApi->update_task_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| taskId | 
 **status** | **int**| Task status &lt;br/&gt; 1 - OPEN &lt;br/&gt; 2 - PERCENT_TWENTY &lt;br/&gt; 3 - PERCENT_FORTY &lt;br/&gt; 4 - PERCENT_SIXTY &lt;br/&gt; 5 - PERCENT_EIGHTY &lt;br/&gt; 6 - RESOLVED &lt;br/&gt; 7 - REOPENED | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)taskId&lt;br/&gt;2)taskTitle&lt;br/&gt;3)taskDescription&lt;br/&gt;4)dueDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)taskId&lt;br/&gt;2)taskTitle&lt;br/&gt;3)taskDescription&lt;br/&gt;4)status&lt;br/&gt;5)priority&lt;br/&gt;6)dueDate&lt;br/&gt;7)milestoneName&lt;br/&gt;8)groupType&lt;br/&gt;9)groupName | [optional] [default to taskId,taskTitle,taskDescription,dueDate]

### Return type

[**VerveResponseTask**](VerveResponseTask.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

