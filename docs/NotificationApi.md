# iengage_client.NotificationApi

All URIs are relative to *https://api.iengage.io:8243/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notifications**](NotificationApi.md#get_notifications) | **GET** /notifications | Get list of notifications
[**mark_all_notification_as_read**](NotificationApi.md#mark_all_notification_as_read) | **POST** /notifications/read/all | Mark all notification as read
[**mark_notification_as_read**](NotificationApi.md#mark_notification_as_read) | **POST** /notifications/read/{notificationId} | Mark notification as read
[**notification_count**](NotificationApi.md#notification_count) | **GET** /notifications/count | Get notifications count


# **get_notifications**
> VerveResponseNotificationList get_notifications(type, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of notifications

Return the list of notifications

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
api_instance = iengage_client.NotificationApi()
type = 'ALL' # str | Type of count<br/> 1) UNREAD <br/> 2) READ <br/> 3)ALL (default to ALL)
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'notificationId,message,isRead,date' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)notificationId<br/>2)message<br/>3)isRead<br/>4)date<br/><b>A) Available values-</b><br/>1)notificationId<br/>2)message<br/>3)isRead<br/>4)date<br/>5)type<br/>6)byUser<br/>7)entity<br/>8)parentEntity (optional) (default to notificationId,message,isRead,date)

try: 
    # Get list of notifications
    api_response = api_instance.get_notifications(type, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of count&lt;br/&gt; 1) UNREAD &lt;br/&gt; 2) READ &lt;br/&gt; 3)ALL | [default to ALL]
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)notificationId&lt;br/&gt;2)message&lt;br/&gt;3)isRead&lt;br/&gt;4)date&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)notificationId&lt;br/&gt;2)message&lt;br/&gt;3)isRead&lt;br/&gt;4)date&lt;br/&gt;5)type&lt;br/&gt;6)byUser&lt;br/&gt;7)entity&lt;br/&gt;8)parentEntity | [optional] [default to notificationId,message,isRead,date]

### Return type

[**VerveResponseNotificationList**](VerveResponseNotificationList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_all_notification_as_read**
> bool mark_all_notification_as_read(logged_in_user_id, access_token, client_token)

Mark all notification as read

Allows the user to mark all the notification as read

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
api_instance = iengage_client.NotificationApi()
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Mark all notification as read
    api_response = api_instance.mark_all_notification_as_read(logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->mark_all_notification_as_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

**bool**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_notification_as_read**
> bool mark_notification_as_read(notification_id, logged_in_user_id, access_token, client_token)

Mark notification as read

Allows the user to mark the notification as read

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
api_instance = iengage_client.NotificationApi()
notification_id = 789 # int | notification Id
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Mark notification as read
    api_response = api_instance.mark_notification_as_read(notification_id, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->mark_notification_as_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| notification Id | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

**bool**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_count**
> int notification_count(type, logged_in_user_id, access_token, client_token)

Get notifications count

Returns the notification count

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
api_instance = iengage_client.NotificationApi()
type = 'ALL' # str | Type of count<br/> 1) UNREAD <br/> 2) READ <br/> 3)ALL (default to ALL)
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Get notifications count
    api_response = api_instance.notification_count(type, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of count&lt;br/&gt; 1) UNREAD &lt;br/&gt; 2) READ &lt;br/&gt; 3)ALL | [default to ALL]
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

**int**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

