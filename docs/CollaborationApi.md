# iengage-client.CollaborationApi

All URIs are relative to *https://api.iengage.io:8243/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment_blog**](CollaborationApi.md#add_comment_blog) | **POST** /collaborations/blogs/{blogId}/comments | Comment on posted blog
[**add_comment_discussion**](CollaborationApi.md#add_comment_discussion) | **POST** /collaborations/discussions/{discussionId}/comments | Comment on discussion
[**delete_blog**](CollaborationApi.md#delete_blog) | **DELETE** /collaborations/blogs/{blogId} | Delete blog
[**delete_blog_comment**](CollaborationApi.md#delete_blog_comment) | **DELETE** /collaborations/blogs/comments/{commentId} | Delete blog comment
[**delete_discussion**](CollaborationApi.md#delete_discussion) | **DELETE** /collaborations/discussions/{discussionId} | Delete discussion
[**delete_discussion_comment**](CollaborationApi.md#delete_discussion_comment) | **DELETE** /collaborations/discussions/comments/{commentId} | Delete discussion comment
[**get_blog_comments**](CollaborationApi.md#get_blog_comments) | **GET** /collaborations/blogs/{blogId}/comments | Get list of comments on blog
[**get_blogs**](CollaborationApi.md#get_blogs) | **GET** /collaborations/blogs | Get list of blogs
[**get_discussion_comments**](CollaborationApi.md#get_discussion_comments) | **GET** /collaborations/discussions/{discussionId}/comments | Get list of comments on discussion
[**get_discussions**](CollaborationApi.md#get_discussions) | **GET** /collaborations/discussions | Get list of discussions
[**get_user_subscribed_blogs**](CollaborationApi.md#get_user_subscribed_blogs) | **GET** /collaborations/blogs/{userId}/subscribe | Get list of blogs subscribed by user
[**get_user_subscribed_discussions**](CollaborationApi.md#get_user_subscribed_discussions) | **GET** /collaborations/discussions/{userId}/subscribe | Get list of discussions subscribed by user
[**post_blog**](CollaborationApi.md#post_blog) | **POST** /collaborations/blogs | Post blog
[**start_discussion**](CollaborationApi.md#start_discussion) | **POST** /collaborations/discussions | Start discussion
[**subscribe_blog**](CollaborationApi.md#subscribe_blog) | **POST** /collaborations/blogs/{blogId}/subscribe | Subscribe blog
[**subscribe_discussion**](CollaborationApi.md#subscribe_discussion) | **POST** /collaborations/discussions/{discussionId}/subscribe | Subscribe discussion
[**unsubscribe_blog**](CollaborationApi.md#unsubscribe_blog) | **POST** /collaborations/blogs/{blogId}/unsubscribe | Unsubscribe blog
[**unsubscribe_discussion**](CollaborationApi.md#unsubscribe_discussion) | **POST** /collaborations/discussions/{discussionId}/unsubscribe | Unsubscribe discussion
[**update_blog**](CollaborationApi.md#update_blog) | **PUT** /collaborations/blogs/{blogId} | Update blog
[**update_blog_comment**](CollaborationApi.md#update_blog_comment) | **PUT** /collaborations/blogs/comments/{commentId} | Update blog comment
[**update_discussion**](CollaborationApi.md#update_discussion) | **PUT** /collaborations/discussions/{discussionId} | Update discussion
[**update_discussion_comment**](CollaborationApi.md#update_discussion_comment) | **PUT** /collaborations/discussions/comments/{commentId} | Update discussion comment


# **add_comment_blog**
> VerveResponseComment add_comment_blog(blog_id, comment_text, logged_in_user_id, access_token, client_token)

Comment on posted blog

Allows the user to give comment on posted Blog. Returns the comment

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
api_instance = iengage-client.CollaborationApi()
blog_id = 789 # int | blogId
comment_text = 'comment_text_example' # str | Comment Text
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Comment on posted blog
    api_response = api_instance.add_comment_blog(blog_id, comment_text, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->add_comment_blog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_id** | **int**| blogId | 
 **comment_text** | **str**| Comment Text | 
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

# **add_comment_discussion**
> VerveResponseComment add_comment_discussion(discussion_id, comment_text, logged_in_user_id, access_token, client_token)

Comment on discussion

Allows the user to comment on discussion. Returns the comment

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
api_instance = iengage-client.CollaborationApi()
discussion_id = 789 # int | discussionId
comment_text = 'comment_text_example' # str | Comment Text
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Comment on discussion
    api_response = api_instance.add_comment_discussion(discussion_id, comment_text, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->add_comment_discussion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discussion_id** | **int**| discussionId | 
 **comment_text** | **str**| Comment Text | 
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

# **delete_blog**
> VerveResponseBlog delete_blog(blog_id, logged_in_user_id, access_token, client_token)

Delete blog

Allows the user to delete blog. Returns the deleted blog

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
api_instance = iengage-client.CollaborationApi()
blog_id = 789 # int | blog Id
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Delete blog
    api_response = api_instance.delete_blog(blog_id, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_blog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_id** | **int**| blog Id | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseBlog**](VerveResponseBlog.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_blog_comment**
> VerveResponseComment delete_blog_comment(comment_id, logged_in_user_id, access_token, client_token)

Delete blog comment

Allows the user to delete blog comment.  Returns the deleted blog comment

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
api_instance = iengage-client.CollaborationApi()
comment_id = 789 # int | comment Id
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Delete blog comment
    api_response = api_instance.delete_blog_comment(comment_id, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_blog_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| comment Id | 
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

# **delete_discussion**
> VerveResponseDiscussion delete_discussion(discussion_id, logged_in_user_id, access_token, client_token)

Delete discussion

Allows the user to delete discussion. Returns the deleted discussion

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
api_instance = iengage-client.CollaborationApi()
discussion_id = 789 # int | discussion Id
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Delete discussion
    api_response = api_instance.delete_discussion(discussion_id, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_discussion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discussion_id** | **int**| discussion Id | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseDiscussion**](VerveResponseDiscussion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_discussion_comment**
> VerveResponseComment delete_discussion_comment(comment_id, logged_in_user_id, access_token, client_token)

Delete discussion comment

Allows the user to delete discussion comment. Returns the deleted discussion comment

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
api_instance = iengage-client.CollaborationApi()
comment_id = 789 # int | comment Id
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Delete discussion comment
    api_response = api_instance.delete_discussion_comment(comment_id, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_discussion_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| comment Id | 
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

# **get_blog_comments**
> VerveResponseCommentList get_blog_comments(blog_id, start, end, logged_in_user_id, access_token, client_token)

Get list of comments on blog

Returns the list of comments on blog

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
api_instance = iengage-client.CollaborationApi()
blog_id = 789 # int | blogId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Get list of comments on blog
    api_response = api_instance.get_blog_comments(blog_id, start, end, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_blog_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_id** | **int**| blogId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
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

# **get_blogs**
> VerveResponseBlogList get_blogs(organization_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of blogs

Returns the list of blogs

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
api_instance = iengage-client.CollaborationApi()
organization_id = 789 # int | organizationId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'blogId,blogTitle,blogDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)blogId<br/>2)blogTitle<br/>3)blogDescription<br/>4)createdDate<br/><b>A )Available values-</b><br/>1)blogId<br/>2)blogTitle<br/>3)blogDescription<br/>4)createdDate<br/>5)user<br/>6)sentiment</br>7)entity (optional) (default to blogId,blogTitle,blogDescription,createdDate)

try: 
    # Get list of blogs
    api_response = api_instance.get_blogs(organization_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_blogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| organizationId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)blogId&lt;br/&gt;2)blogTitle&lt;br/&gt;3)blogDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A )Available values-&lt;/b&gt;&lt;br/&gt;1)blogId&lt;br/&gt;2)blogTitle&lt;br/&gt;3)blogDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)user&lt;br/&gt;6)sentiment&lt;/br&gt;7)entity | [optional] [default to blogId,blogTitle,blogDescription,createdDate]

### Return type

[**VerveResponseBlogList**](VerveResponseBlogList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discussion_comments**
> VerveResponseCommentList get_discussion_comments(discussion_id, start, end, logged_in_user_id, access_token, client_token)

Get list of comments on discussion

Returns the list of comments on discussion

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
api_instance = iengage-client.CollaborationApi()
discussion_id = 789 # int | discussionId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Get list of comments on discussion
    api_response = api_instance.get_discussion_comments(discussion_id, start, end, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_discussion_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discussion_id** | **int**| discussionId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
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

# **get_discussions**
> VerveResponseDiscussionList get_discussions(organization_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of discussions

Returns the list of discussions

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
api_instance = iengage-client.CollaborationApi()
organization_id = 789 # int | organizationId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'discussionId,discussionSubject,discussionDescription,createdDate ' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)discussionId<br/>2)discussionSubject<br/>3)discussionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)discussionId<br/>2)discussionSubject<br/>3)discussionDescription<br/>4)createdDate<br/>5)user<br/>6)sentiment</br>7)entity (optional) (default to discussionId,discussionSubject,discussionDescription,createdDate )

try: 
    # Get list of discussions
    api_response = api_instance.get_discussions(organization_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_discussions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| organizationId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)discussionId&lt;br/&gt;2)discussionSubject&lt;br/&gt;3)discussionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)discussionId&lt;br/&gt;2)discussionSubject&lt;br/&gt;3)discussionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)user&lt;br/&gt;6)sentiment&lt;/br&gt;7)entity | [optional] [default to discussionId,discussionSubject,discussionDescription,createdDate ]

### Return type

[**VerveResponseDiscussionList**](VerveResponseDiscussionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscribed_blogs**
> VerveResponseBlog get_user_subscribed_blogs(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of blogs subscribed by user

Returns the list of blogs subscribed by user

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
api_instance = iengage-client.CollaborationApi()
user_id = 789 # int | userId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'blogId,blogTitle,blogDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)blogId<br/>2)blogTitle<br/>3)blogDescription<br/>4)createdDate<br/><b>A )Available values-</b><br/>1)blogId<br/>2)blogTitle<br/>3)blogDescription<br/>4)createdDate<br/>5)user<br/>6)sentiment</br>7)entity (optional) (default to blogId,blogTitle,blogDescription,createdDate)

try: 
    # Get list of blogs subscribed by user
    api_response = api_instance.get_user_subscribed_blogs(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_user_subscribed_blogs: %s\n" % e)
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
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)blogId&lt;br/&gt;2)blogTitle&lt;br/&gt;3)blogDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A )Available values-&lt;/b&gt;&lt;br/&gt;1)blogId&lt;br/&gt;2)blogTitle&lt;br/&gt;3)blogDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)user&lt;br/&gt;6)sentiment&lt;/br&gt;7)entity | [optional] [default to blogId,blogTitle,blogDescription,createdDate]

### Return type

[**VerveResponseBlog**](VerveResponseBlog.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscribed_discussions**
> VerveResponseDiscussionList get_user_subscribed_discussions(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of discussions subscribed by user

Returns the list of discussions subscribed by user 

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
api_instance = iengage-client.CollaborationApi()
user_id = 789 # int | userId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'discussionId,discussionSubject,discussionDescription,createdDate ' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)discussionId<br/>2)discussionSubject<br/>3)discussionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)discussionId<br/>2)discussionSubject<br/>3)discussionDescription<br/>4)createdDate<br/>5)user<br/>6)sentiment</br>7)entity (optional) (default to discussionId,discussionSubject,discussionDescription,createdDate )

try: 
    # Get list of discussions subscribed by user
    api_response = api_instance.get_user_subscribed_discussions(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_user_subscribed_discussions: %s\n" % e)
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
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)discussionId&lt;br/&gt;2)discussionSubject&lt;br/&gt;3)discussionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)discussionId&lt;br/&gt;2)discussionSubject&lt;br/&gt;3)discussionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)user&lt;br/&gt;6)sentiment&lt;/br&gt;7)entity | [optional] [default to discussionId,discussionSubject,discussionDescription,createdDate ]

### Return type

[**VerveResponseDiscussionList**](VerveResponseDiscussionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_blog**
> VerveResponseBlog post_blog(organization_id, blog_title, blog_description, logged_in_user_id, access_token, client_token)

Post blog

Allows the user to post a blog. Returns the posted blog

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
api_instance = iengage-client.CollaborationApi()
organization_id = 789 # int | organizationId
blog_title = 'blog_title_example' # str | blogTitle
blog_description = 'blog_description_example' # str | blogDescription
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Post blog
    api_response = api_instance.post_blog(organization_id, blog_title, blog_description, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->post_blog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| organizationId | 
 **blog_title** | **str**| blogTitle | 
 **blog_description** | **str**| blogDescription | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseBlog**](VerveResponseBlog.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_discussion**
> VerveResponseDiscussion start_discussion(organization_id, subject, description, logged_in_user_id, access_token, client_token)

Start discussion

Allows the user to start discussion. Returns the started discussion

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
api_instance = iengage-client.CollaborationApi()
organization_id = 789 # int | organizationId
subject = 'subject_example' # str | subject
description = 'description_example' # str | description
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Start discussion
    api_response = api_instance.start_discussion(organization_id, subject, description, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->start_discussion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| organizationId | 
 **subject** | **str**| subject | 
 **description** | **str**| description | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseDiscussion**](VerveResponseDiscussion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_blog**
> VerveResponseBlog subscribe_blog(blog_id, logged_in_user_id, access_token, client_token)

Subscribe blog

Allows the user to subscribe to blog. Returns the subscribed blog

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
api_instance = iengage-client.CollaborationApi()
blog_id = 789 # int | blogId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Subscribe blog
    api_response = api_instance.subscribe_blog(blog_id, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->subscribe_blog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_id** | **int**| blogId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseBlog**](VerveResponseBlog.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_discussion**
> VerveResponseDiscussion subscribe_discussion(discussion_id, logged_in_user_id, access_token, client_token)

Subscribe discussion

Allows the user to subscribe to a discussion. Returns the subscribed discussion

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
api_instance = iengage-client.CollaborationApi()
discussion_id = 789 # int | discussionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Subscribe discussion
    api_response = api_instance.subscribe_discussion(discussion_id, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->subscribe_discussion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discussion_id** | **int**| discussionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseDiscussion**](VerveResponseDiscussion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_blog**
> VerveResponseBlog unsubscribe_blog(blog_id, logged_in_user_id, access_token, client_token)

Unsubscribe blog

Allows the user to unsubscribe blog. Returns the unsubscribed blog

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
api_instance = iengage-client.CollaborationApi()
blog_id = 789 # int | blogId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Unsubscribe blog
    api_response = api_instance.unsubscribe_blog(blog_id, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->unsubscribe_blog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_id** | **int**| blogId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseBlog**](VerveResponseBlog.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_discussion**
> VerveResponseDiscussion unsubscribe_discussion(discussion_id, logged_in_user_id, access_token, client_token)

Unsubscribe discussion

Allows the user to unsubscribe to a discussion. Returns the unsubscribed discussion

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
api_instance = iengage-client.CollaborationApi()
discussion_id = 789 # int | discussionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Unsubscribe discussion
    api_response = api_instance.unsubscribe_discussion(discussion_id, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->unsubscribe_discussion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discussion_id** | **int**| discussionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseDiscussion**](VerveResponseDiscussion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_blog**
> VerveResponseBlog update_blog(blog_id, blog_title, blog_description, logged_in_user_id, access_token, client_token)

Update blog

Allows the user to update blog. Returns the updated blog

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
api_instance = iengage-client.CollaborationApi()
blog_id = 789 # int | blogId
blog_title = 'blog_title_example' # str | blog title
blog_description = 'blog_description_example' # str | blog description
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Update blog
    api_response = api_instance.update_blog(blog_id, blog_title, blog_description, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_blog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_id** | **int**| blogId | 
 **blog_title** | **str**| blog title | 
 **blog_description** | **str**| blog description | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseBlog**](VerveResponseBlog.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_blog_comment**
> VerveResponseComment update_blog_comment(comment_id, comment_text, logged_in_user_id, access_token, client_token)

Update blog comment

Allows the user to update blog comment. Returns the updated blog comment

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
api_instance = iengage-client.CollaborationApi()
comment_id = 789 # int | commentId
comment_text = 'comment_text_example' # str | comment text
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Update blog comment
    api_response = api_instance.update_blog_comment(comment_id, comment_text, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_blog_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| commentId | 
 **comment_text** | **str**| comment text | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseComment**](VerveResponseComment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_discussion**
> VerveResponseDiscussion update_discussion(discussion_id, subject, discussion_description, logged_in_user_id, access_token, client_token)

Update discussion

Allows the user to update discussion. Returns the updated discussion

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
api_instance = iengage-client.CollaborationApi()
discussion_id = 789 # int | discussionId
subject = 'subject_example' # str | subject
discussion_description = 'discussion_description_example' # str | discussion Description
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Update discussion
    api_response = api_instance.update_discussion(discussion_id, subject, discussion_description, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_discussion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discussion_id** | **int**| discussionId | 
 **subject** | **str**| subject | 
 **discussion_description** | **str**| discussion Description | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseDiscussion**](VerveResponseDiscussion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_discussion_comment**
> VerveResponseDiscussion update_discussion_comment(comment_id, comment_text, logged_in_user_id, access_token, client_token)

Update discussion comment

Allows the user to update discussion comment. Returns the updated discussion comment

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
api_instance = iengage-client.CollaborationApi()
comment_id = 789 # int | commentId
comment_text = 'comment_text_example' # str | comment text
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Update discussion comment
    api_response = api_instance.update_discussion_comment(comment_id, comment_text, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_discussion_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| commentId | 
 **comment_text** | **str**| comment text | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseDiscussion**](VerveResponseDiscussion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

