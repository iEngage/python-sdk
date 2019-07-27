# iengage_client.GroupApi

All URIs are relative to *https://api.iengage.io:8243/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupApi.md#create_group) | **POST** /groups | Create group
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /groups/{groupId} | Delete group
[**follow_group**](GroupApi.md#follow_group) | **POST** /groups/{groupId}/follow | Follow group
[**get_group_followers**](GroupApi.md#get_group_followers) | **GET** /groups/{groupId}/followers | Get the list of followers for the group
[**get_group_ideas**](GroupApi.md#get_group_ideas) | **GET** /groups/{groupId}/ideas | Get list of all ideas in a group
[**get_groups**](GroupApi.md#get_groups) | **GET** /groups | Get the list of groups visible for user
[**get_recommendation_group**](GroupApi.md#get_recommendation_group) | **GET** /groups/recommend | Get list of recommended groups
[**get_user_following_groups**](GroupApi.md#get_user_following_groups) | **GET** /groups/{userId}/following | Get list of groups that a user is following
[**search_groups**](GroupApi.md#search_groups) | **GET** /groups/search | Get list of matching groups
[**unfollow_group**](GroupApi.md#unfollow_group) | **POST** /groups/{groupId}/unfollow | Unfollow group
[**update_group**](GroupApi.md#update_group) | **PUT** /groups/{groupId} | Update group


# **create_group**
> VerveResponseGroup create_group(requester_id, client_token, body=body, access_token=access_token)

Create group

This service allows a user to create a group. The following fields(key:value) are required to be present in the Group JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API. **Required fields**      1. association      2. groupName      3. description      4. managerId [1,2,..]      5. accessType

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.GroupApi()
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body = iengage_client.Group() # Group |  (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Create group
    api_response = api_instance.create_group(requester_id, client_token, body=body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupApi->create_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body** | [**Group**](Group.md)|  | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseGroup**](VerveResponseGroup.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> VerveResponseGroup delete_group(group_id, requester_id, client_token, fields=fields, access_token=access_token)

Delete group

Allows the user to delete a group. Returns the deleted group

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ (optional) (default to groupId,groupName,description,startDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Delete group
    api_response = api_instance.delete_group(group_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupApi->delete_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ | [optional] [default to groupId,groupName,description,startDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseGroup**](VerveResponseGroup.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow_group**
> VerveResponseGroup follow_group(group_id, requester_id, client_token, fields=fields, access_token=access_token)

Follow group

Allows the user to follow a group. Returns the followed group

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ (optional) (default to groupId,groupName,description,startDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Follow group
    api_response = api_instance.follow_group(group_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupApi->follow_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ | [optional] [default to groupId,groupName,description,startDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseGroup**](VerveResponseGroup.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_followers**
> VerveResponseUserList get_group_followers(group_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get the list of followers for the group

Returns the list of followers for the group

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'userId,firstName,lastName,profileImage' # str | Filter fields in result list        /*   **A) Default values -**        1)userId       2)firstName       3)lastName       4)profileImage        **A) Available values-**       1)userId       2)firstName       3)lastName       4)emailId       5)profileImage       6)birthDate        */ (optional) (default to userId,firstName,lastName,profileImage)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get the list of followers for the group
    api_response = api_instance.get_group_followers(group_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupApi->get_group_followers: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)userId       2)firstName       3)lastName       4)profileImage        **A) Available values-**       1)userId       2)firstName       3)lastName       4)emailId       5)profileImage       6)birthDate        */ | [optional] [default to userId,firstName,lastName,profileImage]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseUserList**](VerveResponseUserList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_ideas**
> VerveResponseIdeaList get_group_ideas(group_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get list of all ideas in a group

Returns the list of all ideas in a group

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list       /*   **A) Default values-**      1)ideaId       2)ideaTitle       3)ideaDescription       4)ideaCreationDate        **A) Available values-**        1)ideaId       2)ideaTitle       3)group       4)ideaDescription       5)ideator       6)ideaCreationDate       7)lastModifiedDate       8)ideaStage       9)domain       10)technology       11)accessType       12)videoId       13)activeStatus       14)teamStatus       15)projectStatus       16)totalFollowers       17)totalComments       18)totalBlogs       19)averageRatingScore       20)numberOfRatings       21)currentUserFollowing       22)currentUserRating       23)ideaFileURL       24)sentiment       25)entity   */ (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of all ideas in a group
    api_response = api_instance.get_group_ideas(group_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupApi->get_group_ideas: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list       /*   **A) Default values-**      1)ideaId       2)ideaTitle       3)ideaDescription       4)ideaCreationDate        **A) Available values-**        1)ideaId       2)ideaTitle       3)group       4)ideaDescription       5)ideator       6)ideaCreationDate       7)lastModifiedDate       8)ideaStage       9)domain       10)technology       11)accessType       12)videoId       13)activeStatus       14)teamStatus       15)projectStatus       16)totalFollowers       17)totalComments       18)totalBlogs       19)averageRatingScore       20)numberOfRatings       21)currentUserFollowing       22)currentUserRating       23)ideaFileURL       24)sentiment       25)entity   */ | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdeaList**](VerveResponseIdeaList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> VerveResponseGroupList get_groups(start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get the list of groups visible for user

Returns the list of groups

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.GroupApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ (optional) (default to groupId,groupName,description,startDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get the list of groups visible for user
    api_response = api_instance.get_groups(start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupApi->get_groups: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ | [optional] [default to groupId,groupName,description,startDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseGroupList**](VerveResponseGroupList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommendation_group**
> VerveResponseGroupList get_recommendation_group(start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get list of recommended groups

Returns the list of recommended groups

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.GroupApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ (optional) (default to groupId,groupName,description,startDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of recommended groups
    api_response = api_instance.get_recommendation_group(start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupApi->get_recommendation_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ | [optional] [default to groupId,groupName,description,startDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseGroupList**](VerveResponseGroupList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_following_groups**
> VerveResponseGroupList get_user_following_groups(user_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get list of groups that a user is following

Returns the list of groups the user is following

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.GroupApi()
user_id = 789 # int | User Id whose groups want to get.
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ (optional) (default to groupId,groupName,description,startDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of groups that a user is following
    api_response = api_instance.get_user_following_groups(user_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupApi->get_user_following_groups: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id whose groups want to get. | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ | [optional] [default to groupId,groupName,description,startDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseGroupList**](VerveResponseGroupList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_groups**
> VerveResponseGroupList search_groups(query, start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get list of matching groups

Returns the list of matching group

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.GroupApi()
query = 'query_example' # str | query
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ (optional) (default to groupId,groupName,description,startDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of matching groups
    api_response = api_instance.search_groups(query, start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupApi->search_groups: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ | [optional] [default to groupId,groupName,description,startDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseGroupList**](VerveResponseGroupList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfollow_group**
> VerveResponseGroup unfollow_group(group_id, requester_id, client_token, fields=fields, access_token=access_token)

Unfollow group

Allows the user to unfollow a group. Returns the unfollowed group

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ (optional) (default to groupId,groupName,description,startDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Unfollow group
    api_response = api_instance.unfollow_group(group_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupApi->unfollow_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ | [optional] [default to groupId,groupName,description,startDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseGroup**](VerveResponseGroup.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> VerveResponseGroup update_group(group_id, title, description, requester_id, client_token, fields=fields, access_token=access_token)

Update group

Allows the user to update the group. Returns the updated group

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
title = 'title_example' # str | title
description = 'description_example' # str | description
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ (optional) (default to groupId,groupName,description,startDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Update group
    api_response = api_instance.update_group(group_id, title, description, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupApi->update_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **title** | **str**| title | 
 **description** | **str**| description | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list        /*   **A) Default values -**        1)groupId       2)groupName       3)description       4)startDate        **A) Available values-**        1)groupId       2)groupName       3)description       4)startDate       5)ideasCount       6)followersCount       7)currentUserFollowing       8)dueDate       9)participantsCount       10)friendsParticipantsCount       11)friendsIdeasCount   */ | [optional] [default to groupId,groupName,description,startDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseGroup**](VerveResponseGroup.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

