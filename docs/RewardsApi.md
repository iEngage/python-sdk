# iengage_client.RewardsApi

All URIs are relative to *https://api.iengage.io:8243/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_top_friends**](RewardsApi.md#get_top_friends) | **GET** /rewards/points/top/friends | Get list of top friends
[**get_top_users**](RewardsApi.md#get_top_users) | **GET** /rewards/points/top | Get list of top users
[**get_user_points**](RewardsApi.md#get_user_points) | **GET** /rewards/points/{userId} | Get list of user points


# **get_top_friends**
> VerveResponseUserPointsList get_top_friends(user_id, start, end, requester_id, client_token, access_token=access_token)

Get list of top friends

Returns the list top friends

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.RewardsApi()
user_id = 789 # int | userId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of top friends
    api_response = api_instance.get_top_friends(user_id, start, end, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RewardsApi->get_top_friends: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseUserPointsList**](VerveResponseUserPointsList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_users**
> VerveResponseUserPointsList get_top_users(start, end, requester_id, client_token, access_token=access_token)

Get list of top users

Returns the list of top users

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.RewardsApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of top users
    api_response = api_instance.get_top_users(start, end, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RewardsApi->get_top_users: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseUserPointsList**](VerveResponseUserPointsList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_points**
> VerveResponseUserPoints get_user_points(user_id, requester_id, client_token, access_token=access_token)

Get list of user points

Returns the list of user points

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.RewardsApi()
user_id = 789 # int | User Id whose points wants to get
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of user points
    api_response = api_instance.get_user_points(user_id, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RewardsApi->get_user_points: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id whose points wants to get | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseUserPoints**](VerveResponseUserPoints.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

