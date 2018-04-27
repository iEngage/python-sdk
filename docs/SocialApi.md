# iengage_client.SocialApi

All URIs are relative to *https://api.iengage.io:8243/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_friend**](SocialApi.md#add_friend) | **POST** /social/friends/add | Add Friend
[**confirm_friend_request**](SocialApi.md#confirm_friend_request) | **POST** /social/friends/request/action | confirm/ignore friend request
[**follow**](SocialApi.md#follow) | **POST** /social/follow | Follow user
[**get_user**](SocialApi.md#get_user) | **GET** /social/users/{userId} | Get user by id 
[**get_user_detail**](SocialApi.md#get_user_detail) | **GET** /social/userDetail | Get user details 
[**get_user_followers**](SocialApi.md#get_user_followers) | **GET** /social/followers/{userId} | Get list of followers
[**get_user_following**](SocialApi.md#get_user_following) | **GET** /social/following/{userId} | Get list of users that are being followed
[**get_user_friends**](SocialApi.md#get_user_friends) | **GET** /social/friends{userId} | Get list of friends
[**remove_friend**](SocialApi.md#remove_friend) | **POST** /social/friends/remove | Remove friend 
[**request_friend**](SocialApi.md#request_friend) | **POST** /social/friends/request | Send friend request
[**requests_for_me**](SocialApi.md#requests_for_me) | **GET** /social/friends/request | Get list of friend requests
[**unfollow**](SocialApi.md#unfollow) | **POST** /social/unfollow | Unfollow user


# **add_friend**
> bool add_friend(id1, id2, requester_id, client_token, access_token=access_token)

Add Friend

Allows the user to add friend. Returns true if successful

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
api_instance = iengage_client.SocialApi()
id1 = 'id1_example' # str | Enter userId/mailId of the person who wants to add a friend
id2 = 'id2_example' # str | Enter userId /mailId you want to add in friend list
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Add Friend
    api_response = api_instance.add_friend(id1, id2, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->add_friend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id1** | **str**| Enter userId/mailId of the person who wants to add a friend | 
 **id2** | **str**| Enter userId /mailId you want to add in friend list | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

**bool**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_friend_request**
> bool confirm_friend_request(user_id, status, requester_id, client_token, access_token=access_token)

confirm/ignore friend request

Allows the user to confirm/ignore friend request. Returns true if successful

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
api_instance = iengage_client.SocialApi()
user_id = 789 # int | userId of user who sent friend request
status = 56 # int | Set Friend Request status <br/> CONFIRM - 1  <br/> IGNORE - 2 
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # confirm/ignore friend request
    api_response = api_instance.confirm_friend_request(user_id, status, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->confirm_friend_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId of user who sent friend request | 
 **status** | **int**| Set Friend Request status &lt;br/&gt; CONFIRM - 1  &lt;br/&gt; IGNORE - 2  | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

**bool**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow**
> bool follow(follower, followee, requester_id, client_token, access_token=access_token)

Follow user

Allows to follow a user. Returns true if successful

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
api_instance = iengage_client.SocialApi()
follower = 'follower_example' # str | Enter the userId/mailId of the follower
followee = 'followee_example' # str | Enter the userId/mailId of the user the follower wants to follow
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Follow user
    api_response = api_instance.follow(follower, followee, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->follow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **follower** | **str**| Enter the userId/mailId of the follower | 
 **followee** | **str**| Enter the userId/mailId of the user the follower wants to follow | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

**bool**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> VerveResponseUser get_user(user_id, requester_id, client_token, fields=fields, access_token=access_token)

Get user by id 

Returns the user.

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
api_instance = iengage_client.SocialApi()
user_id = 789 # int | User Id
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'userId,firstName,lastName,profileImage' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)profileImage<br/><b>A) Available values-</b><br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)emailId<br/>5)profileImage<br/>6)birthDate<br/> (optional) (default to userId,firstName,lastName,profileImage)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get user by id 
    api_response = api_instance.get_user(user_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)profileImage&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)emailId&lt;br/&gt;5)profileImage&lt;br/&gt;6)birthDate&lt;br/&gt; | [optional] [default to userId,firstName,lastName,profileImage]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseUser**](VerveResponseUser.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_detail**
> VerveResponseUserDetail get_user_detail(user_id, requester_id, client_token, access_token=access_token)

Get user details 

Returns the user details.

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
api_instance = iengage_client.SocialApi()
user_id = 789 # int | Enter user Id whose details you need
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get user details 
    api_response = api_instance.get_user_detail(user_id, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->get_user_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Enter user Id whose details you need | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseUserDetail**](VerveResponseUserDetail.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_followers**
> VerveResponseUserList get_user_followers(user_id, requester_id, client_token, fields=fields, access_token=access_token)

Get list of followers

Returns the list of followers

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
api_instance = iengage_client.SocialApi()
user_id = 789 # int | User Id whose followers wants to get.
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'userId,firstName,lastName,profileImage' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)profileImage<br/><b>A) Available values-</b><br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)emailId<br/>5)profileImage<br/>6)birthDate<br/> (optional) (default to userId,firstName,lastName,profileImage)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of followers
    api_response = api_instance.get_user_followers(user_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->get_user_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id whose followers wants to get. | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)profileImage&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)emailId&lt;br/&gt;5)profileImage&lt;br/&gt;6)birthDate&lt;br/&gt; | [optional] [default to userId,firstName,lastName,profileImage]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseUserList**](VerveResponseUserList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_following**
> VerveResponseUserList get_user_following(user_id, requester_id, client_token, fields=fields, access_token=access_token)

Get list of users that are being followed

Returns the list of users that are being followed

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
api_instance = iengage_client.SocialApi()
user_id = 789 # int | User Id whose followed list want to get
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'userId,firstName,lastName,profileImage' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)profileImage<br/><b>A) Available values-</b><br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)emailId<br/>5)profileImage<br/>6)birthDate<br/> (optional) (default to userId,firstName,lastName,profileImage)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of users that are being followed
    api_response = api_instance.get_user_following(user_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->get_user_following: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id whose followed list want to get | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)profileImage&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)emailId&lt;br/&gt;5)profileImage&lt;br/&gt;6)birthDate&lt;br/&gt; | [optional] [default to userId,firstName,lastName,profileImage]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseUserList**](VerveResponseUserList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_friends**
> VerveResponseUserList get_user_friends(user_id, requester_id, client_token, fields=fields, access_token=access_token)

Get list of friends

Returns the list of friends

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
api_instance = iengage_client.SocialApi()
user_id = 789 # int | userId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'userId,firstName,lastName,profileImage' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)profileImage<br/><b>A) Available values-</b><br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)emailId<br/>5)profileImage<br/>6)birthDate<br/> (optional) (default to userId,firstName,lastName,profileImage)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of friends
    api_response = api_instance.get_user_friends(user_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->get_user_friends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)profileImage&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)emailId&lt;br/&gt;5)profileImage&lt;br/&gt;6)birthDate&lt;br/&gt; | [optional] [default to userId,firstName,lastName,profileImage]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseUserList**](VerveResponseUserList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_friend**
> bool remove_friend(id1, id2, requester_id, client_token, access_token=access_token)

Remove friend 

Allows the user to remove friend. Returns true if successful

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
api_instance = iengage_client.SocialApi()
id1 = 'id1_example' # str | Enter userId/mailId of the person who wants to remove from friend
id2 = 'id2_example' # str | Enter userId /mailId you want to remove in friend list
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Remove friend 
    api_response = api_instance.remove_friend(id1, id2, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->remove_friend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id1** | **str**| Enter userId/mailId of the person who wants to remove from friend | 
 **id2** | **str**| Enter userId /mailId you want to remove in friend list | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

**bool**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_friend**
> bool request_friend(user_id, requester_id, client_token, access_token=access_token)

Send friend request

Allows user to send a friend request. Returns true if successful

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
api_instance = iengage_client.SocialApi()
user_id = 789 # int | Enter userId /mailId you want to send friend request
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Send friend request
    api_response = api_instance.request_friend(user_id, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->request_friend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Enter userId /mailId you want to send friend request | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

**bool**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requests_for_me**
> VerveResponseRequestForMeList requests_for_me(requester_id, client_token, access_token=access_token)

Get list of friend requests

Returns the list of friend requests

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
api_instance = iengage_client.SocialApi()
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of friend requests
    api_response = api_instance.requests_for_me(requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->requests_for_me: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseRequestForMeList**](VerveResponseRequestForMeList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfollow**
> bool unfollow(unfollower, unfollowee, requester_id, client_token, access_token=access_token)

Unfollow user

Allows to unfollow user. Returns true if successful

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
api_instance = iengage_client.SocialApi()
unfollower = 'unfollower_example' # str | Enter the userId/mailId of the unfollower
unfollowee = 'unfollowee_example' # str | Enter the userId/mailId of the user the unfollower wants to unfollow
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Unfollow user
    api_response = api_instance.unfollow(unfollower, unfollowee, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialApi->unfollow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unfollower** | **str**| Enter the userId/mailId of the unfollower | 
 **unfollowee** | **str**| Enter the userId/mailId of the user the unfollower wants to unfollow | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

**bool**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

