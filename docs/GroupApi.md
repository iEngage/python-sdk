# iengage_client.GroupApi

All URIs are relative to *https://api.iengage.io:8243/api/1.0*

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
> VerveResponseGroup create_group(organization_id, title, description, manager_id, access_type, logged_in_user_id, access_token, client_token)

Create group

Allows the uer to create a group. Returns the created group

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
api_instance = iengage_client.GroupApi()
organization_id = 789 # int | organization Id
title = 'title_example' # str | title
description = 'description_example' # str | description
manager_id = 789 # int | managerId
access_type = 'access_type_example' # str | accessType<br>1)open<br>2)restricted
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Create group
    api_response = api_instance.create_group(organization_id, title, description, manager_id, access_type, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| organization Id | 
 **title** | **str**| title | 
 **description** | **str**| description | 
 **manager_id** | **int**| managerId | 
 **access_type** | **str**| accessType&lt;br&gt;1)open&lt;br&gt;2)restricted | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseGroup**](VerveResponseGroup.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> VerveResponseGroup delete_group(group_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete group

Allows the user to delete a group. Returns the deleted group

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
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/><b>A) Available values-</b><br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/>5)ideasCount<br/>6)followersCount<br/>7)currentUserFollowing<br/>8)dueDate<br/>9)participantsCount<br/>10)friendsParticipantsCount<br/>11)friendsIdeasCount (optional) (default to groupId,groupName,description,startDate)

try: 
    # Delete group
    api_response = api_instance.delete_group(group_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;5)ideasCount&lt;br/&gt;6)followersCount&lt;br/&gt;7)currentUserFollowing&lt;br/&gt;8)dueDate&lt;br/&gt;9)participantsCount&lt;br/&gt;10)friendsParticipantsCount&lt;br/&gt;11)friendsIdeasCount | [optional] [default to groupId,groupName,description,startDate]

### Return type

[**VerveResponseGroup**](VerveResponseGroup.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow_group**
> VerveResponseGroup follow_group(group_id, logged_in_user_id, access_token, client_token, fields=fields)

Follow group

Allows the user to follow a group. Returns the followed group

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
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/><b>A) Available values-</b><br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/>5)ideasCount<br/>6)followersCount<br/>7)currentUserFollowing<br/>8)dueDate<br/>9)participantsCount<br/>10)friendsParticipantsCount<br/>11)friendsIdeasCount (optional) (default to groupId,groupName,description,startDate)

try: 
    # Follow group
    api_response = api_instance.follow_group(group_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->follow_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;5)ideasCount&lt;br/&gt;6)followersCount&lt;br/&gt;7)currentUserFollowing&lt;br/&gt;8)dueDate&lt;br/&gt;9)participantsCount&lt;br/&gt;10)friendsParticipantsCount&lt;br/&gt;11)friendsIdeasCount | [optional] [default to groupId,groupName,description,startDate]

### Return type

[**VerveResponseGroup**](VerveResponseGroup.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_followers**
> VerveResponseUserList get_group_followers(group_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get the list of followers for the group

Returns the list of followers for the group

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
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'userId,firstName,lastName,profileImage' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)profileImage<br/><b>A) Available values-</b><br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)emailId<br/>5)profileImage<br/>6)birthDate<br/>7)currentUserFollowing<br/>8)currentUserFriend<br/>9)equityScore (optional) (default to userId,firstName,lastName,profileImage)

try: 
    # Get the list of followers for the group
    api_response = api_instance.get_group_followers(group_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)profileImage&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)emailId&lt;br/&gt;5)profileImage&lt;br/&gt;6)birthDate&lt;br/&gt;7)currentUserFollowing&lt;br/&gt;8)currentUserFriend&lt;br/&gt;9)equityScore | [optional] [default to userId,firstName,lastName,profileImage]

### Return type

[**VerveResponseUserList**](VerveResponseUserList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_ideas**
> VerveResponseIdeaList get_group_ideas(group_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of all ideas in a group

Returns the list of all ideas in a group

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
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)

try: 
    # Get list of all ideas in a group
    api_response = api_instance.get_group_ideas(group_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_ideas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]

### Return type

[**VerveResponseIdeaList**](VerveResponseIdeaList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> VerveResponseGroupList get_groups(start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get the list of groups visible for user

Returns the list of groups

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
api_instance = iengage_client.GroupApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/><b>A) Available values-</b><br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/>5)ideasCount<br/>6)followersCount<br/>7)currentUserFollowing<br/>8)dueDate<br/>9)participantsCount<br/>10)friendsParticipantsCount<br/>11)friendsIdeasCount (optional) (default to groupId,groupName,description,startDate)

try: 
    # Get the list of groups visible for user
    api_response = api_instance.get_groups(start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;5)ideasCount&lt;br/&gt;6)followersCount&lt;br/&gt;7)currentUserFollowing&lt;br/&gt;8)dueDate&lt;br/&gt;9)participantsCount&lt;br/&gt;10)friendsParticipantsCount&lt;br/&gt;11)friendsIdeasCount | [optional] [default to groupId,groupName,description,startDate]

### Return type

[**VerveResponseGroupList**](VerveResponseGroupList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommendation_group**
> VerveResponseGroupList get_recommendation_group(start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of recommended groups

Returns the list of recommended groups

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
api_instance = iengage_client.GroupApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/><b>A) Available values-</b><br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/>5)ideasCount<br/>6)followersCount<br/>7)currentUserFollowing<br/>8)dueDate<br/>9)participantsCount<br/>10)friendsParticipantsCount<br/>11)friendsIdeasCount (optional) (default to groupId,groupName,description,startDate)

try: 
    # Get list of recommended groups
    api_response = api_instance.get_recommendation_group(start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_recommendation_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;5)ideasCount&lt;br/&gt;6)followersCount&lt;br/&gt;7)currentUserFollowing&lt;br/&gt;8)dueDate&lt;br/&gt;9)participantsCount&lt;br/&gt;10)friendsParticipantsCount&lt;br/&gt;11)friendsIdeasCount | [optional] [default to groupId,groupName,description,startDate]

### Return type

[**VerveResponseGroupList**](VerveResponseGroupList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_following_groups**
> VerveResponseGroupList get_user_following_groups(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of groups that a user is following

Returns the list of groups the user is following

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
api_instance = iengage_client.GroupApi()
user_id = 789 # int | userId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/><b>A) Available values-</b><br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/>5)ideasCount<br/>6)followersCount<br/>7)currentUserFollowing<br/>8)dueDate<br/>9)participantsCount<br/>10)friendsParticipantsCount<br/>11)friendsIdeasCount (optional) (default to groupId,groupName,description,startDate)

try: 
    # Get list of groups that a user is following
    api_response = api_instance.get_user_following_groups(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_user_following_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;5)ideasCount&lt;br/&gt;6)followersCount&lt;br/&gt;7)currentUserFollowing&lt;br/&gt;8)dueDate&lt;br/&gt;9)participantsCount&lt;br/&gt;10)friendsParticipantsCount&lt;br/&gt;11)friendsIdeasCount | [optional] [default to groupId,groupName,description,startDate]

### Return type

[**VerveResponseGroupList**](VerveResponseGroupList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_groups**
> VerveResponseGroupList search_groups(query, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of matching groups

Returns the list of matching group

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
api_instance = iengage_client.GroupApi()
query = 'query_example' # str | query
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/><b>A) Available values-</b><br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/>5)ideasCount<br/>6)followersCount<br/>7)currentUserFollowing<br/>8)dueDate<br/>9)participantsCount<br/>10)friendsParticipantsCount<br/>11)friendsIdeasCount (optional) (default to groupId,groupName,description,startDate)

try: 
    # Get list of matching groups
    api_response = api_instance.search_groups(query, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->search_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;5)ideasCount&lt;br/&gt;6)followersCount&lt;br/&gt;7)currentUserFollowing&lt;br/&gt;8)dueDate&lt;br/&gt;9)participantsCount&lt;br/&gt;10)friendsParticipantsCount&lt;br/&gt;11)friendsIdeasCount | [optional] [default to groupId,groupName,description,startDate]

### Return type

[**VerveResponseGroupList**](VerveResponseGroupList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfollow_group**
> VerveResponseGroup unfollow_group(group_id, logged_in_user_id, access_token, client_token, fields=fields)

Unfollow group

Allows the user to unfollow a group. Returns the unfollowed group

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
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/><b>A) Available values-</b><br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/>5)ideasCount<br/>6)followersCount<br/>7)currentUserFollowing<br/>8)dueDate<br/>9)participantsCount<br/>10)friendsParticipantsCount<br/>11)friendsIdeasCount (optional) (default to groupId,groupName,description,startDate)

try: 
    # Unfollow group
    api_response = api_instance.unfollow_group(group_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->unfollow_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;5)ideasCount&lt;br/&gt;6)followersCount&lt;br/&gt;7)currentUserFollowing&lt;br/&gt;8)dueDate&lt;br/&gt;9)participantsCount&lt;br/&gt;10)friendsParticipantsCount&lt;br/&gt;11)friendsIdeasCount | [optional] [default to groupId,groupName,description,startDate]

### Return type

[**VerveResponseGroup**](VerveResponseGroup.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> VerveResponseGroup update_group(group_id, title, description, logged_in_user_id, access_token, client_token, fields=fields)

Update group

Allows the user to update the group. Returns the updated group

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
api_instance = iengage_client.GroupApi()
group_id = 789 # int | groupId
title = 'title_example' # str | title
description = 'description_example' # str | description
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'groupId,groupName,description,startDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/><b>A) Available values-</b><br/>1)groupId<br/>2)groupName<br/>3)description<br/>4)startDate<br/>5)ideasCount<br/>6)followersCount<br/>7)currentUserFollowing<br/>8)dueDate<br/>9)participantsCount<br/>10)friendsParticipantsCount<br/>11)friendsIdeasCount (optional) (default to groupId,groupName,description,startDate)

try: 
    # Update group
    api_response = api_instance.update_group(group_id, title, description, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **title** | **str**| title | 
 **description** | **str**| description | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)groupId&lt;br/&gt;2)groupName&lt;br/&gt;3)description&lt;br/&gt;4)startDate&lt;br/&gt;5)ideasCount&lt;br/&gt;6)followersCount&lt;br/&gt;7)currentUserFollowing&lt;br/&gt;8)dueDate&lt;br/&gt;9)participantsCount&lt;br/&gt;10)friendsParticipantsCount&lt;br/&gt;11)friendsIdeasCount | [optional] [default to groupId,groupName,description,startDate]

### Return type

[**VerveResponseGroup**](VerveResponseGroup.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

