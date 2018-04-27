# iengage_client.IdeaApi

All URIs are relative to *https://api.iengage.io:8243/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_comment**](IdeaApi.md#delete_comment) | **DELETE** /ideas/comments/{commentId} | Delete comment
[**delete_idea**](IdeaApi.md#delete_idea) | **DELETE** /ideas/{ideaId} | Delete idea
[**follow_idea**](IdeaApi.md#follow_idea) | **POST** /ideas/{ideaId}/follow | Follow idea
[**get_all_ideas**](IdeaApi.md#get_all_ideas) | **GET** /ideas | Get list of Ideas
[**get_following_ideas**](IdeaApi.md#get_following_ideas) | **GET** /ideas/{userId}/following | Get list of ideas that users are following
[**get_group_ideas**](IdeaApi.md#get_group_ideas) | **GET** /ideas/getGroupIdeas | Get list of ideas in group
[**get_idea**](IdeaApi.md#get_idea) | **GET** /ideas/{ideaId} | Get idea by id
[**get_idea_comment**](IdeaApi.md#get_idea_comment) | **GET** /ideas/{ideaId}/comments | Get list of comments on idea
[**get_idea_followers**](IdeaApi.md#get_idea_followers) | **GET** /ideas/{ideaId}/followers | Get list of followers for this idea
[**get_idea_rating_parameters**](IdeaApi.md#get_idea_rating_parameters) | **GET** /ideas/getIdeaRatingParameters | Get rating parameters of idea by user
[**get_idea_ratings**](IdeaApi.md#get_idea_ratings) | **GET** /ideas/getIdeaUserRating | Get list of ideas that are rated by user 
[**get_recommend_ideas**](IdeaApi.md#get_recommend_ideas) | **GET** /ideas/recommend | Get the list of recommended ideas
[**get_top_ideas**](IdeaApi.md#get_top_ideas) | **GET** /ideas/top | Get the list of top ideas
[**get_user_ideas**](IdeaApi.md#get_user_ideas) | **GET** /ideas/{userId}/shared | Get list of ideas shared by user
[**get_user_rate_ideas**](IdeaApi.md#get_user_rate_ideas) | **GET** /ideas/{userId}/rated | Get list of ideas rated by user
[**rate_idea**](IdeaApi.md#rate_idea) | **POST** /ideas/rateIdea | Rate an idea
[**rate_idea_0**](IdeaApi.md#rate_idea_0) | **GET** /ideas/rateIdeaByParameter | Give rating on idea
[**search_ideas**](IdeaApi.md#search_ideas) | **GET** /ideas/search | Get list of matching ideas
[**share_form_idea**](IdeaApi.md#share_form_idea) | **POST** /ideas/attachment | Share Idea with attachments
[**share_idea**](IdeaApi.md#share_idea) | **POST** /ideas | Share idea  
[**share_idea_comment**](IdeaApi.md#share_idea_comment) | **POST** /ideas/{ideaId}/comments | Comment on shared idea
[**unfollow_idea**](IdeaApi.md#unfollow_idea) | **POST** /ideas/{ideaId}/unfollow | Unfollow idea
[**update_commet**](IdeaApi.md#update_commet) | **PUT** /ideas/comments/{commentId} | Update comment
[**update_idea**](IdeaApi.md#update_idea) | **PUT** /ideas/{ideaId} | Update idea


# **delete_comment**
> VerveResponseComment delete_comment(comment_id, requester_id, client_token, access_token=access_token)

Delete comment

Allows the user to delete comment. Returns the deleted comment

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
api_instance = iengage_client.IdeaApi()
comment_id = 789 # int | Comment Id
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Delete comment
    api_response = api_instance.delete_comment(comment_id, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| Comment Id | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseComment**](VerveResponseComment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_idea**
> VerveResponseIdea delete_idea(idea_id, requester_id, client_token, file, fields=fields, access_token=access_token)

Delete idea

Allows the user to delete idea. Returns the deleted idea

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
api_instance = iengage_client.IdeaApi()
idea_id = 789 # int | ideaId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
file = '/path/to/file.txt' # file | file
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Delete idea
    api_response = api_instance.delete_idea(idea_id, requester_id, client_token, file, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->delete_idea: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea_id** | **int**| ideaId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **file** | **file**| file | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdea**](VerveResponseIdea.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow_idea**
> VerveResponseIdea follow_idea(idea_id, requester_id, client_token, fields=fields, access_token=access_token)

Follow idea

Allows the user to follow idea. Returns the followed idea

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
api_instance = iengage_client.IdeaApi()
idea_id = 789 # int | idea Id
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Follow idea
    api_response = api_instance.follow_idea(idea_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->follow_idea: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea_id** | **int**| idea Id | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdea**](VerveResponseIdea.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ideas**
> VerveResponseIdeaList get_all_ideas(start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get list of Ideas

Returns the list of ideas

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
api_instance = iengage_client.IdeaApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of Ideas
    api_response = api_instance.get_all_ideas(start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_all_ideas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdeaList**](VerveResponseIdeaList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_following_ideas**
> VerveResponseIdeaList get_following_ideas(user_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get list of ideas that users are following

Returns the list of ideas being followed

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
api_instance = iengage_client.IdeaApi()
user_id = 789 # int | User Id whose followed ideas want to get.
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of ideas that users are following
    api_response = api_instance.get_following_ideas(user_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_following_ideas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id whose followed ideas want to get. | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdeaList**](VerveResponseIdeaList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_ideas**
> VerveResponseIdeaList get_group_ideas(user_id, group_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get list of ideas in group

Return the ideas list on group

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
api_instance = iengage_client.IdeaApi()
user_id = 789 # int | user Id
group_id = 789 # int | group Id
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of ideas in group
    api_response = api_instance.get_group_ideas(user_id, group_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_group_ideas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| user Id | 
 **group_id** | **int**| group Id | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdeaList**](VerveResponseIdeaList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idea**
> VerveResponseIdea get_idea(idea_id, requester_id, client_token, fields=fields, access_token=access_token)

Get idea by id

Returns the idea by id

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
api_instance = iengage_client.IdeaApi()
idea_id = 789 # int | idea Id
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get idea by id
    api_response = api_instance.get_idea(idea_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_idea: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea_id** | **int**| idea Id | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdea**](VerveResponseIdea.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idea_comment**
> VerveResponseCommentList get_idea_comment(idea_id, start, end, requester_id, client_token, access_token=access_token)

Get list of comments on idea

Returns the list of comments on idea

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
api_instance = iengage_client.IdeaApi()
idea_id = 789 # int | idea Id
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of comments on idea
    api_response = api_instance.get_idea_comment(idea_id, start, end, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_idea_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea_id** | **int**| idea Id | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
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

# **get_idea_followers**
> VerveResponseUserList get_idea_followers(idea_id, start, end, requester_id, client_token, access_token=access_token)

Get list of followers for this idea

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
api_instance = iengage_client.IdeaApi()
idea_id = 789 # int | ideaId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of followers for this idea
    api_response = api_instance.get_idea_followers(idea_id, start, end, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_idea_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea_id** | **int**| ideaId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseUserList**](VerveResponseUserList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idea_rating_parameters**
> VerveResponseString get_idea_rating_parameters(user_id, idea_stage, requester_id, client_token, access_token=access_token)

Get rating parameters of idea by user

Return the rating parameters of idea by user

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
api_instance = iengage_client.IdeaApi()
user_id = 789 # int | user Id
idea_stage = 'idea_stage_example' # str | Idea stages<br/>1)under-consideration <br/>2) shortlisted <br/>3) accepted <br/>4) prototyping
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get rating parameters of idea by user
    api_response = api_instance.get_idea_rating_parameters(user_id, idea_stage, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_idea_rating_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| user Id | 
 **idea_stage** | **str**| Idea stages&lt;br/&gt;1)under-consideration &lt;br/&gt;2) shortlisted &lt;br/&gt;3) accepted &lt;br/&gt;4) prototyping | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseString**](VerveResponseString.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idea_ratings**
> VerveResponseIdeaUserRatingList get_idea_ratings(user_id, idea_id, idea_stage, requester_id, client_token, access_token=access_token)

Get list of ideas that are rated by user 

Return the rated ideas list

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
api_instance = iengage_client.IdeaApi()
user_id = 789 # int | user Id
idea_id = 789 # int | idea Id
idea_stage = 'idea_stage_example' # str | Idea stages<br/>1)under-consideration <br/>2) shortlisted <br/>3) accepted <br/>4) prototyping
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of ideas that are rated by user 
    api_response = api_instance.get_idea_ratings(user_id, idea_id, idea_stage, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_idea_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| user Id | 
 **idea_id** | **int**| idea Id | 
 **idea_stage** | **str**| Idea stages&lt;br/&gt;1)under-consideration &lt;br/&gt;2) shortlisted &lt;br/&gt;3) accepted &lt;br/&gt;4) prototyping | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdeaUserRatingList**](VerveResponseIdeaUserRatingList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommend_ideas**
> VerveResponseIdeaList get_recommend_ideas(start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get the list of recommended ideas

Returns the list of recommended ideas 

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
api_instance = iengage_client.IdeaApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get the list of recommended ideas
    api_response = api_instance.get_recommend_ideas(start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_recommend_ideas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdeaList**](VerveResponseIdeaList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_ideas**
> VerveResponseIdeaList get_top_ideas(start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get the list of top ideas

Return the list of top ideas

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
api_instance = iengage_client.IdeaApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get the list of top ideas
    api_response = api_instance.get_top_ideas(start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_top_ideas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdeaList**](VerveResponseIdeaList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_ideas**
> VerveResponseIdeaList get_user_ideas(user_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get list of ideas shared by user

Returns the list of ideas shared by user

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
api_instance = iengage_client.IdeaApi()
user_id = 789 # int | userId whose shared ideas want to get
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of ideas shared by user
    api_response = api_instance.get_user_ideas(user_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_user_ideas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId whose shared ideas want to get | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdeaList**](VerveResponseIdeaList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_rate_ideas**
> VerveResponseIdeaList get_user_rate_ideas(user_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get list of ideas rated by user

Return the list of ideas rated by user

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
api_instance = iengage_client.IdeaApi()
user_id = 789 # int | userId whose rated ideas want to get
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of ideas rated by user
    api_response = api_instance.get_user_rate_ideas(user_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->get_user_rate_ideas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId whose rated ideas want to get | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdeaList**](VerveResponseIdeaList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rate_idea**
> VerveResponseIdea rate_idea(user_id, idea_id, idea_stage, requester_id, client_token, fields=fields, access_token=access_token)

Rate an idea

Allows the user to rate an idea. Returns the rated idea

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
api_instance = iengage_client.IdeaApi()
user_id = 789 # int | user Id
idea_id = 789 # int | idea Id
idea_stage = 'idea_stage_example' # str | Ideas stage<br/>1)under-consideration <br/>2) shortlisted <br/>3) accepted <br/>4) prototyping
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Rate an idea
    api_response = api_instance.rate_idea(user_id, idea_id, idea_stage, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->rate_idea: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| user Id | 
 **idea_id** | **int**| idea Id | 
 **idea_stage** | **str**| Ideas stage&lt;br/&gt;1)under-consideration &lt;br/&gt;2) shortlisted &lt;br/&gt;3) accepted &lt;br/&gt;4) prototyping | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdea**](VerveResponseIdea.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rate_idea_0**
> VerveResponseIdea rate_idea_0(user_id, idea_id, idea_stage, parameter, rating, requester_id, client_token, fields=fields, access_token=access_token)

Give rating on idea

Allows the user to give a rating on idea. Returns the rated idea

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
api_instance = iengage_client.IdeaApi()
user_id = 789 # int | user Id
idea_id = 789 # int | idea Id
idea_stage = 'idea_stage_example' # str | Idea stages<br/>1)under-consideration <br/>2) shortlisted <br/>3) accepted <br/>4) prototyping
parameter = 'parameter_example' # str | parameter
rating = 1.2 # float | rating
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Give rating on idea
    api_response = api_instance.rate_idea_0(user_id, idea_id, idea_stage, parameter, rating, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->rate_idea_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| user Id | 
 **idea_id** | **int**| idea Id | 
 **idea_stage** | **str**| Idea stages&lt;br/&gt;1)under-consideration &lt;br/&gt;2) shortlisted &lt;br/&gt;3) accepted &lt;br/&gt;4) prototyping | 
 **parameter** | **str**| parameter | 
 **rating** | **float**| rating | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdea**](VerveResponseIdea.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ideas**
> VerveResponseIdeaList search_ideas(search_text, start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get list of matching ideas

Returns the list of matching ideas

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
api_instance = iengage_client.IdeaApi()
search_text = 'search_text_example' # str | Enter text to be searched
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of matching ideas
    api_response = api_instance.search_ideas(search_text, start, end, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->search_ideas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Enter text to be searched | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdeaList**](VerveResponseIdeaList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_form_idea**
> VerveResponseIdea share_form_idea(title, description, group_id, file, logged_in_user_id, access_token, client_token)

Share Idea with attachments

Allows the user to share idea with attachments

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
api_instance = iengage_client.IdeaApi()
title = 'title_example' # str | title
description = 'description_example' # str | description
group_id = 'group_id_example' # str | groupId
file = '/path/to/file.txt' # file | file
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Share Idea with attachments
    api_response = api_instance.share_form_idea(title, description, group_id, file, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->share_form_idea: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| title | 
 **description** | **str**| description | 
 **group_id** | **str**| groupId | 
 **file** | **file**| file | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseIdea**](VerveResponseIdea.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_idea**
> VerveResponseIdea share_idea(requester_id, client_token, body=body, access_token=access_token)

Share idea  

This service allows a user to share a idea. The following fields(key:value) are required to be present in the Idea JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API.</br><b>Required fields </br>1. ideaTitle </br>2. ideaDescription </br>3. group: { groupId } </br>

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
api_instance = iengage_client.IdeaApi()
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body = iengage_client.Idea() # Idea |  (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Share idea  
    api_response = api_instance.share_idea(requester_id, client_token, body=body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->share_idea: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body** | [**Idea**](Idea.md)|  | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdea**](VerveResponseIdea.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_idea_comment**
> VerveResponseComment share_idea_comment(idea_id, requester_id, client_token, body=body, access_token=access_token)

Comment on shared idea

This service allows a user to comment on a idea. The following fields(key:value) are required to be present in the Comment JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API.</br><b>Required fields </br>1. ideaId (Path Parameter)</br>2. commentText </br>

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
api_instance = iengage_client.IdeaApi()
idea_id = 789 # int | idea Id
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body = iengage_client.Comment() # Comment |  (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Comment on shared idea
    api_response = api_instance.share_idea_comment(idea_id, requester_id, client_token, body=body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->share_idea_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea_id** | **int**| idea Id | 
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

# **unfollow_idea**
> VerveResponseIdea unfollow_idea(idea_id, requester_id, client_token, fields=fields, access_token=access_token)

Unfollow idea

Allows the user to unfollow idea. Returns the unfollowed idea

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
api_instance = iengage_client.IdeaApi()
idea_id = 789 # int | idea Id
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Unfollow idea
    api_response = api_instance.unfollow_idea(idea_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->unfollow_idea: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea_id** | **int**| idea Id | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdea**](VerveResponseIdea.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_commet**
> VerveResponseComment update_commet(comment_id, comment_text, requester_id, client_token, access_token=access_token)

Update comment

Allows the user to update comment. Returns the updated comment

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
api_instance = iengage_client.IdeaApi()
comment_id = 789 # int | commentId
comment_text = 'comment_text_example' # str | Comment text
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Update comment
    api_response = api_instance.update_commet(comment_id, comment_text, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->update_commet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| commentId | 
 **comment_text** | **str**| Comment text | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseComment**](VerveResponseComment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_idea**
> VerveResponseIdea update_idea(idea_id, idea_title, idea_description, requester_id, client_token, fields=fields, access_token=access_token)

Update idea

Allows the user to update idea. Returns the updated idea

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
api_instance = iengage_client.IdeaApi()
idea_id = 789 # int | ideaId
idea_title = 'idea_title_example' # str | Idea Title
idea_description = 'idea_description_example' # str | Describe Idea
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'ideaId,ideaTitle,ideaDescription,ideaCreationDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)ideaId<br/>2)ideaTitle<br/>3)ideaDescription<br/>4)ideaCreationDate<br/><b>A) Available values-</b><br/>1)ideaId<br/>2)ideaTitle<br/>3)group<br/>4)ideaDescription<br/>5)ideator<br/>6)ideaCreationDate<br/>7)lastModifiedDate<br/>8)ideaStage<br/>9)domain<br/>10)technology<br/>11)accessType<br/>12)videoId<br/>13)activeStatus<br/>14)teamStatus<br/>15)projectStatus<br/>16)totalFollowers<br/>17)totalComments<br/>18)totalBlogs<br/>19)averageRatingScore<br/>20)numberOfRatings<br/>21)currentUserFollowing<br/>22)currentUserRating<br/>23)ideaFileURL<br/>24)sentiment</br>25)entity (optional) (default to ideaId,ideaTitle,ideaDescription,ideaCreationDate)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Update idea
    api_response = api_instance.update_idea(idea_id, idea_title, idea_description, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdeaApi->update_idea: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea_id** | **int**| ideaId | 
 **idea_title** | **str**| Idea Title | 
 **idea_description** | **str**| Describe Idea | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)ideaDescription&lt;br/&gt;4)ideaCreationDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)ideaId&lt;br/&gt;2)ideaTitle&lt;br/&gt;3)group&lt;br/&gt;4)ideaDescription&lt;br/&gt;5)ideator&lt;br/&gt;6)ideaCreationDate&lt;br/&gt;7)lastModifiedDate&lt;br/&gt;8)ideaStage&lt;br/&gt;9)domain&lt;br/&gt;10)technology&lt;br/&gt;11)accessType&lt;br/&gt;12)videoId&lt;br/&gt;13)activeStatus&lt;br/&gt;14)teamStatus&lt;br/&gt;15)projectStatus&lt;br/&gt;16)totalFollowers&lt;br/&gt;17)totalComments&lt;br/&gt;18)totalBlogs&lt;br/&gt;19)averageRatingScore&lt;br/&gt;20)numberOfRatings&lt;br/&gt;21)currentUserFollowing&lt;br/&gt;22)currentUserRating&lt;br/&gt;23)ideaFileURL&lt;br/&gt;24)sentiment&lt;/br&gt;25)entity | [optional] [default to ideaId,ideaTitle,ideaDescription,ideaCreationDate]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseIdea**](VerveResponseIdea.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

