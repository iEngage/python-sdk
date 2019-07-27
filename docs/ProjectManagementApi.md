# iengage_client.ProjectManagementApi

All URIs are relative to *https://api.iengage.io:8243/api/2.0*

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
> VerveResponseComment add_milestone_comment(milestone_id, requester_id, client_token, body=body, access_token=access_token)

Comment on milestone

This service allows a user to comment on a milestone. The following fields(key:value) are required to be present in the Comment JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API.  **Required fields**  1. milestoneId (Path Parameter) 2. commentText  

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
milestone_id = 789 # int | milestoneId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body = iengage_client.Comment() # Comment |  (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Comment on milestone
    api_response = api_instance.add_milestone_comment(milestone_id, requester_id, client_token, body=body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->add_milestone_comment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_id** | **int**| milestoneId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body** | [**Comment**](Comment.md)|  | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseComment**](VerveResponseComment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_task_comment**
> VerveResponseComment add_task_comment(task_id, requester_id, client_token, body=body, access_token=access_token)

Comment on task

This service allows a user to comment on a task. The following fields(key:value) are required to be present in the Comment JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API.  **Required fields**  1. **taskId (Path Parameter)**  2. **commentText**  

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
task_id = 789 # int | taskId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body = iengage_client.Comment() # Comment |  (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Comment on task
    api_response = api_instance.add_task_comment(task_id, requester_id, client_token, body=body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->add_task_comment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| taskId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body** | [**Comment**](Comment.md)|  | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseComment**](VerveResponseComment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_milestone**
> VerveResponseMilestone create_milestone(requester_id, client_token, body=body, access_token=access_token)

Create milestone

This service allows a user to create a milestone. The following fields(key:value) are required to be present in the Milestone JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API.  **Required fields**  1. **milestoneTitle**  2. **milestoneDescription**  3. **dueDate**  4. **neverDue**  

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body = iengage_client.Milestone() # Milestone |  (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Create milestone
    api_response = api_instance.create_milestone(requester_id, client_token, body=body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->create_milestone: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body** | [**Milestone**](Milestone.md)|  | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseMilestone**](VerveResponseMilestone.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> VerveResponseTask create_task(milestone_id, requester_id, client_token, body=body, access_token=access_token)

Create task

This service allows a user to create a task. The following fields(key:value) are required to be present in the Task JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API.   **Required fields**  1. **taskTitle**  2. **taskDescription**  3. **priority**  4. **dueDate**  5. **assigneeUserId**  6. **neverDue**  7. **user: { userId }**

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
milestone_id = 789 # int | Milestone Id
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body = iengage_client.Task() # Task |  (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Create task
    api_response = api_instance.create_task(milestone_id, requester_id, client_token, body=body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->create_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_id** | **int**| Milestone Id | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body** | [**Task**](Task.md)|  | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseTask**](VerveResponseTask.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_milestone**
> VerveResponseMilestone delete_milestone(milestone_id, requester_id, client_token, fields=fields, access_token=access_token)

Delete milestone

Allows the user to delete milestone. Returns the deleted milestone

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
milestone_id = 789 # int | milestoneId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'milestoneId,milestoneTitle,milestoneDescription,createdDate' # str | Filter fields in result list      /*   **A) Default values -**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate        **A) Available values-**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate       5)status       6)priority       7)dueDate   */ (optional) (default to milestoneId,milestoneTitle,milestoneDescription,createdDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Delete milestone
    api_response = api_instance.delete_milestone(milestone_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->delete_milestone: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_id** | **int**| milestoneId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list      /*   **A) Default values -**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate        **A) Available values-**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate       5)status       6)priority       7)dueDate   */ | [optional] [default to milestoneId,milestoneTitle,milestoneDescription,createdDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseMilestone**](VerveResponseMilestone.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> VerveResponseTask delete_task(task_id, requester_id, client_token, fields=fields, access_token=access_token)

Delete task

Allows the user to delete task. Returns the deleted task

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
task_id = 789 # int | taskId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'taskId,taskTitle,taskDescription,dueDate' # str | Filter fields in result list        /*   **A) Default values -**        1)taskId       2)taskTitle       3)taskDescription       4)dueDate        **A) Available values-**        1)taskId       2)taskTitle       3)taskDescription       4)status       5)priority       6)dueDate       7)milestoneName       8)groupType       9)groupName   */ (optional) (default to taskId,taskTitle,taskDescription,dueDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Delete task
    api_response = api_instance.delete_task(task_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->delete_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| taskId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)taskId       2)taskTitle       3)taskDescription       4)dueDate        **A) Available values-**        1)taskId       2)taskTitle       3)taskDescription       4)status       5)priority       6)dueDate       7)milestoneName       8)groupType       9)groupName   */ | [optional] [default to taskId,taskTitle,taskDescription,dueDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseTask**](VerveResponseTask.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_milestones**
> VerveResponseMilestoneList get_milestones(requester_id, client_token, organization_id=organization_id, fields=fields, access_token=access_token)

Get list of milestones

Returns the list of milestones

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
organization_id = 789 # int | organizationId (optional)
fields = 'milestoneId,milestoneTitle,milestoneDescription,createdDate' # str | Filter fields in result list      /*   **A) Default values -**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate        **A) Available values-**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate       5)status       6)priority       7)dueDate   */ (optional) (default to milestoneId,milestoneTitle,milestoneDescription,createdDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of milestones
    api_response = api_instance.get_milestones(requester_id, client_token, organization_id=organization_id, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->get_milestones: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **organization_id** | **int**| organizationId | [optional] 
 **fields** | **str**| Filter fields in result list      /*   **A) Default values -**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate        **A) Available values-**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate       5)status       6)priority       7)dueDate   */ | [optional] [default to milestoneId,milestoneTitle,milestoneDescription,createdDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseMilestoneList**](VerveResponseMilestoneList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_milestones_comments**
> VerveResponseCommentList get_milestones_comments(milestone_id, requester_id, client_token, access_token=access_token)

Get list of comments written on Milestones

Returns the list comments written on milestone

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
milestone_id = 789 # int | milestoneId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of comments written on Milestones
    api_response = api_instance.get_milestones_comments(milestone_id, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->get_milestones_comments: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_id** | **int**| milestoneId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseCommentList**](VerveResponseCommentList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_comments**
> VerveResponseCommentList get_task_comments(task_id, requester_id, client_token, access_token=access_token)

Get list of Comments written on task

Returns the list of comments written on task

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
task_id = 789 # int | taskId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of Comments written on task
    api_response = api_instance.get_task_comments(task_id, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->get_task_comments: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| taskId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseCommentList**](VerveResponseCommentList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_tasks**
> VerveResponseTaskList get_user_tasks(user_id, status, requester_id, client_token, fields=fields, access_token=access_token)

Get list of task assigned to user

Returns the list of task assigned to user

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
user_id = 789 # int | User Id whose assinged task want to get
status = 56 # int |   /*   Task status   0 - ALL   1 - OPEN   2 - PERCENT_TWENTY   3 - PERCENT_FORTY   4 - PERCENT_SIXTY   5 - PERCENT_EIGHTY   6 - RESOLVED   7 - REOPENED   */
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'taskId,taskTitle,taskDescription,dueDate' # str | Filter fields in result list        /*   **A) Default values -**        1)taskId       2)taskTitle       3)taskDescription       4)dueDate        **A) Available values-**        1)taskId       2)taskTitle       3)taskDescription       4)status       5)priority       6)dueDate       7)milestoneName       8)groupType       9)groupName   */ (optional) (default to taskId,taskTitle,taskDescription,dueDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of task assigned to user
    api_response = api_instance.get_user_tasks(user_id, status, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->get_user_tasks: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id whose assinged task want to get | 
 **status** | **int**|   /*   Task status   0 - ALL   1 - OPEN   2 - PERCENT_TWENTY   3 - PERCENT_FORTY   4 - PERCENT_SIXTY   5 - PERCENT_EIGHTY   6 - RESOLVED   7 - REOPENED   */ | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)taskId       2)taskTitle       3)taskDescription       4)dueDate        **A) Available values-**        1)taskId       2)taskTitle       3)taskDescription       4)status       5)priority       6)dueDate       7)milestoneName       8)groupType       9)groupName   */ | [optional] [default to taskId,taskTitle,taskDescription,dueDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseTaskList**](VerveResponseTaskList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_milestone**
> VerveResponseMilestone update_milestone(milestone_id, title, description, due_date, requester_id, client_token, fields=fields, access_token=access_token)

Update milestone

Allows the user to update milestone. Returns the updated milestone

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
milestone_id = 789 # int | milestoneId
title = 'title_example' # str | title
description = 'description_example' # str | description
due_date = 'due_date_example' # str | Due date (Format: MM-dd-yyyy HH:mm:ss a)
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'milestoneId,milestoneTitle,milestoneDescription,createdDate' # str | Filter fields in result list      /*   **A) Default values -**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate        **A) Available values-**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate       5)status       6)priority       7)dueDate   */ (optional) (default to milestoneId,milestoneTitle,milestoneDescription,createdDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Update milestone
    api_response = api_instance.update_milestone(milestone_id, title, description, due_date, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->update_milestone: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_id** | **int**| milestoneId | 
 **title** | **str**| title | 
 **description** | **str**| description | 
 **due_date** | **str**| Due date (Format: MM-dd-yyyy HH:mm:ss a) | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list      /*   **A) Default values -**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate        **A) Available values-**        1)milestoneId       2)milestoneTitle       3)milestoneDescription       4)createdDate       5)status       6)priority       7)dueDate   */ | [optional] [default to milestoneId,milestoneTitle,milestoneDescription,createdDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseMilestone**](VerveResponseMilestone.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> VerveResponseTask update_task(task_id, title, description, due_date, status, re_assignee_user_id, requester_id, client_token, fields=fields, access_token=access_token)

Update task

Allows the user to update task. Returns the updated task

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
task_id = 789 # int | taskId
title = 'title_example' # str | title
description = 'description_example' # str | description
due_date = 'due_date_example' # str | Due date
status = 56 # int |   /*   Task status   1 - OPEN   2 - PERCENT_TWENTY   3 - PERCENT_FORTY   4 - PERCENT_SIXTY   5 - PERCENT_EIGHTY   6 - RESOLVED   7 - REOPENED   */
re_assignee_user_id = 789 # int | re-assignee User Id
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'taskId,taskTitle,taskDescription,dueDate' # str | Filter fields in result list        /*   **A) Default values -**        1)taskId       2)taskTitle       3)taskDescription       4)dueDate        **A) Available values-**        1)taskId       2)taskTitle       3)taskDescription       4)status       5)priority       6)dueDate       7)milestoneName       8)groupType       9)groupName   */ (optional) (default to taskId,taskTitle,taskDescription,dueDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Update task
    api_response = api_instance.update_task(task_id, title, description, due_date, status, re_assignee_user_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->update_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| taskId | 
 **title** | **str**| title | 
 **description** | **str**| description | 
 **due_date** | **str**| Due date | 
 **status** | **int**|   /*   Task status   1 - OPEN   2 - PERCENT_TWENTY   3 - PERCENT_FORTY   4 - PERCENT_SIXTY   5 - PERCENT_EIGHTY   6 - RESOLVED   7 - REOPENED   */ | 
 **re_assignee_user_id** | **int**| re-assignee User Id | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)taskId       2)taskTitle       3)taskDescription       4)dueDate        **A) Available values-**        1)taskId       2)taskTitle       3)taskDescription       4)status       5)priority       6)dueDate       7)milestoneName       8)groupType       9)groupName   */ | [optional] [default to taskId,taskTitle,taskDescription,dueDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseTask**](VerveResponseTask.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_status**
> VerveResponseTask update_task_status(task_id, status, requester_id, client_token, fields=fields, access_token=access_token)

Update task status

Allows the user to update task status. Returns the updated task status

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.ProjectManagementApi()
task_id = 789 # int | taskId
status = 56 # int |   /*  Task status   1 - OPEN   2 - PERCENT_TWENTY   3 - PERCENT_FORTY   4 - PERCENT_SIXTY   5 - PERCENT_EIGHTY   6 - RESOLVED   7 - REOPENED   */
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'taskId,taskTitle,taskDescription,dueDate' # str | Filter fields in result list        /*   **A) Default values -**        1)taskId       2)taskTitle       3)taskDescription       4)dueDate        **A) Available values-**        1)taskId       2)taskTitle       3)taskDescription       4)status       5)priority       6)dueDate       7)milestoneName       8)groupType       9)groupName   */ (optional) (default to taskId,taskTitle,taskDescription,dueDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Update task status
    api_response = api_instance.update_task_status(task_id, status, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectManagementApi->update_task_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| taskId | 
 **status** | **int**|   /*  Task status   1 - OPEN   2 - PERCENT_TWENTY   3 - PERCENT_FORTY   4 - PERCENT_SIXTY   5 - PERCENT_EIGHTY   6 - RESOLVED   7 - REOPENED   */ | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)taskId       2)taskTitle       3)taskDescription       4)dueDate        **A) Available values-**        1)taskId       2)taskTitle       3)taskDescription       4)status       5)priority       6)dueDate       7)milestoneName       8)groupType       9)groupName   */ | [optional] [default to taskId,taskTitle,taskDescription,dueDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseTask**](VerveResponseTask.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

