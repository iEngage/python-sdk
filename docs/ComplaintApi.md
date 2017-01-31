# iengage_client.ComplaintApi

All URIs are relative to *https://api.iengage.io:8243/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_complaint**](ComplaintApi.md#add_complaint) | **POST** /complaints | Share complaint without attachment
[**add_complaint_0**](ComplaintApi.md#add_complaint_0) | **POST** /complaints/attachment | Share complaint with attachment
[**add_solution**](ComplaintApi.md#add_solution) | **POST** /complaints/{complaintId}/solutions | Share solution on complaint
[**create_complaint_category**](ComplaintApi.md#create_complaint_category) | **POST** /complaints/categories | Create complaint category
[**delete_complaint**](ComplaintApi.md#delete_complaint) | **DELETE** /complaints/{complaintId} | Delete complaint
[**delete_complaint_category**](ComplaintApi.md#delete_complaint_category) | **DELETE** /complaints/categories/{categoryId} | Delete complaint cotegory
[**delete_solution**](ComplaintApi.md#delete_solution) | **DELETE** /complaints/solutions/{solutionId} | Delete solution
[**dislike_solution**](ComplaintApi.md#dislike_solution) | **POST** /complaints/{complaintId}/solutions/{solutionId}/dislike | Dislike Solution
[**get_complaint**](ComplaintApi.md#get_complaint) | **GET** /complaints/{complaintId} | Get complaint by id
[**get_complaint_categories**](ComplaintApi.md#get_complaint_categories) | **GET** /complaints/categories | Get list of complaint category
[**get_complaints_for_user**](ComplaintApi.md#get_complaints_for_user) | **GET** /complaints | Get list of all complaint visible for user
[**get_friends_complaints**](ComplaintApi.md#get_friends_complaints) | **GET** /complaints/friends | Get list of complaints shared by your friends
[**get_recommend_complaint**](ComplaintApi.md#get_recommend_complaint) | **GET** /complaints/recommend | Get list of recommended complaints
[**get_recommended_complaints_from_db**](ComplaintApi.md#get_recommended_complaints_from_db) | **GET** /complaints/{userId}/recommendedComplaints | Get list of recommended complaints from DB
[**get_recommended_users_from_db**](ComplaintApi.md#get_recommended_users_from_db) | **GET** /complaints/{complaintId}/recommendedUsers | Get list of recommended Users from DB
[**get_solutions**](ComplaintApi.md#get_solutions) | **GET** /complaints/{complaintId}/solutions | Get list of solutions by ComplaintId
[**get_user_complaints**](ComplaintApi.md#get_user_complaints) | **GET** /complaints/{userId}/shared | Get list of complaints shared by user
[**get_user_subscribed_complaint_categories**](ComplaintApi.md#get_user_subscribed_complaint_categories) | **GET** /complaints/categories/{userId}/subscribe | Get list of Complaint categories subscribed by user
[**get_user_subscribed_complaints**](ComplaintApi.md#get_user_subscribed_complaints) | **GET** /complaints/{userId}/subscribe | Get list of complaints subscribed by user
[**like_solution**](ComplaintApi.md#like_solution) | **POST** /complaints/{complaintId}/solutions/{solutionId}/like | Like solution
[**mark_as_an_solution**](ComplaintApi.md#mark_as_an_solution) | **POST** /complaints/{complaintId}/solutions/{solutionId}/mark | Mark solution as a solution
[**search_complaints**](ComplaintApi.md#search_complaints) | **GET** /complaints/search | Get list of complaints by search
[**subscribe_complaint**](ComplaintApi.md#subscribe_complaint) | **POST** /complaints/{complaintId}/subscribe | Subscribe complaint
[**subscribe_complaint_category**](ComplaintApi.md#subscribe_complaint_category) | **POST** /complaints/categories/{categoryId}/subscribe | Subscribe complaint category
[**unmark_as_an_solution**](ComplaintApi.md#unmark_as_an_solution) | **POST** /complaints/{complaintId}/solutions/{solutionId}/unmark | Unmark solution as a solution
[**unsubscribe_complaint**](ComplaintApi.md#unsubscribe_complaint) | **POST** /complaints/{complaintId}/unsubscribe | Unsubscribe Complaint
[**unsubscribe_complaint_category**](ComplaintApi.md#unsubscribe_complaint_category) | **POST** /complaints/categories/{categoryId}/unsubscribe | Unsubscribe complaint category
[**update_complaint**](ComplaintApi.md#update_complaint) | **PUT** /complaints/{complaintId} | Update complaint
[**update_complaint_category**](ComplaintApi.md#update_complaint_category) | **PUT** /complaints/categories/{categoryId} | Update complaint category
[**update_solution**](ComplaintApi.md#update_solution) | **PUT** /complaints/solutions/{solutionId} | Update solution


# **add_complaint**
> VerveResponseComplaint add_complaint(category_id, complaint_title, complaint_description, logged_in_user_id, access_token, client_token)

Share complaint without attachment

Allows the user to share complaint. Returns complaint

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
api_instance = iengage_client.ComplaintApi()
category_id = 789 # int | categoryId
complaint_title = 'complaint_title_example' # str | Complaint Title
complaint_description = 'complaint_description_example' # str | Describe complaint
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Share complaint without attachment
    api_response = api_instance.add_complaint(category_id, complaint_title, complaint_description, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->add_complaint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **complaint_title** | **str**| Complaint Title | 
 **complaint_description** | **str**| Describe complaint | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseComplaint**](VerveResponseComplaint.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_complaint_0**
> VerveResponseComplaint add_complaint_0(body, body2, body3, logged_in_user_id, access_token, client_token, body4=body4)

Share complaint with attachment

Allows the user to share complaints. Returns the complaint object

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
api_instance = iengage_client.ComplaintApi()
body = 789 # int | categoryId
body2 = 'body_example' # str | complaintTitle
body3 = 'body_example' # str | complaintDescription
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body4 = [iengage_client.Attachment()] # list[Attachment] |  (optional)

try: 
    # Share complaint with attachment
    api_response = api_instance.add_complaint_0(body, body2, body3, logged_in_user_id, access_token, client_token, body4=body4)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->add_complaint_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **int**| categoryId | 
 **body2** | **str**| complaintTitle | 
 **body3** | **str**| complaintDescription | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body4** | [**list[Attachment]**](Attachment.md)|  | [optional] 

### Return type

[**VerveResponseComplaint**](VerveResponseComplaint.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_solution**
> VerveResponseSolution add_solution(complaint_id, solution, logged_in_user_id, access_token, client_token, fields=fields)

Share solution on complaint

Allows the user to share a solution on complaint

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
solution = 'solution_example' # str | solution
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'solutionId,solutionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/><b>A) Available values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/>4)complaintId<br/>5)solvingUser<br/>6)isMarkedSolution<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to solutionId,solutionDescription,createdDate)

try: 
    # Share solution on complaint
    api_response = api_instance.add_solution(complaint_id, solution, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->add_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **solution** | **str**| solution | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)complaintId&lt;br/&gt;5)solvingUser&lt;br/&gt;6)isMarkedSolution&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to solutionId,solutionDescription,createdDate]

### Return type

[**VerveResponseSolution**](VerveResponseSolution.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_complaint_category**
> VerveResponseComplaintCategory create_complaint_category(name, description, logged_in_user_id, access_token, client_token, organization_id=organization_id, fields=fields)

Create complaint category

Allows the user to create complaint category. Returns the created complaint category

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
api_instance = iengage_client.ComplaintApi()
name = 'name_example' # str | Name
description = 'description_example' # str | description
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
organization_id = 789 # int | OrganizationId (optional)
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2) categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Create complaint category
    api_response = api_instance.create_complaint_category(name, description, logged_in_user_id, access_token, client_token, organization_id=organization_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->create_complaint_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 
 **description** | **str**| description | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **organization_id** | **int**| OrganizationId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2) categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseComplaintCategory**](VerveResponseComplaintCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_complaint**
> VerveResponseComplaint delete_complaint(complaint_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete complaint

Allows the user to delete complaint. Returns the deleted complaint

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Delete complaint
    api_response = api_instance.delete_complaint(complaint_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->delete_complaint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaint**](VerveResponseComplaint.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_complaint_category**
> VerveResponseComplaintCategory delete_complaint_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete complaint cotegory

Returns the deleted complaint category

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
api_instance = iengage_client.ComplaintApi()
category_id = 789 # int | categoryId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2) categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Delete complaint cotegory
    api_response = api_instance.delete_complaint_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->delete_complaint_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2) categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseComplaintCategory**](VerveResponseComplaintCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_solution**
> VerveResponseSolution delete_solution(solution_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete solution

Allows the user to delete solution. Returns the deleted solution

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
api_instance = iengage_client.ComplaintApi()
solution_id = 789 # int | solutionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'solutionId,solutionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/><b>A) Available values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/>4)complaintId<br/>5)solvingUser<br/>6)isMarkedSolution<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to solutionId,solutionDescription,createdDate)

try: 
    # Delete solution
    api_response = api_instance.delete_solution(solution_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->delete_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | **int**| solutionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)complaintId&lt;br/&gt;5)solvingUser&lt;br/&gt;6)isMarkedSolution&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to solutionId,solutionDescription,createdDate]

### Return type

[**VerveResponseSolution**](VerveResponseSolution.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dislike_solution**
> VerveResponseSolution dislike_solution(complaint_id, solution_id, logged_in_user_id, access_token, client_token, fields=fields)

Dislike Solution

Allows the user to dislike the solution. Returns the disliked solution

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
solution_id = 789 # int | solutionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'solutionId,solutionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/><b>A) Available values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/>4)complaintId<br/>5)solvingUser<br/>6)isMarkedSolution<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to solutionId,solutionDescription,createdDate)

try: 
    # Dislike Solution
    api_response = api_instance.dislike_solution(complaint_id, solution_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->dislike_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **solution_id** | **int**| solutionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)complaintId&lt;br/&gt;5)solvingUser&lt;br/&gt;6)isMarkedSolution&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to solutionId,solutionDescription,createdDate]

### Return type

[**VerveResponseSolution**](VerveResponseSolution.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_complaint**
> VerveResponseComplaint get_complaint(complaint_id, logged_in_user_id, access_token, client_token, fields=fields)

Get complaint by id

Returns the complaint by id

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Get complaint by id
    api_response = api_instance.get_complaint(complaint_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->get_complaint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaint**](VerveResponseComplaint.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_complaint_categories**
> VerveResponseComplaintCategoryList get_complaint_categories(start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of complaint category

Returns the list of complaint category

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
api_instance = iengage_client.ComplaintApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2) categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Get list of complaint category
    api_response = api_instance.get_complaint_categories(start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->get_complaint_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2) categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseComplaintCategoryList**](VerveResponseComplaintCategoryList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_complaints_for_user**
> VerveResponseComplaintList get_complaints_for_user(complaint_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)

Get list of all complaint visible for user

Returns the list of all complaints visible for user

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
api_instance = iengage_client.ComplaintApi()
complaint_status = 'complaint_status_example' # str | Complaint status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Get list of all complaint visible for user
    api_response = api_instance.get_complaints_for_user(complaint_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->get_complaints_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_status** | **str**| Complaint status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaintList**](VerveResponseComplaintList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_friends_complaints**
> VerveResponseComplaintList get_friends_complaints(complaint_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)

Get list of complaints shared by your friends

Returns the list of complaints shared by friends

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
api_instance = iengage_client.ComplaintApi()
complaint_status = 'complaint_status_example' # str | Complaint status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Get list of complaints shared by your friends
    api_response = api_instance.get_friends_complaints(complaint_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->get_friends_complaints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_status** | **str**| Complaint status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaintList**](VerveResponseComplaintList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommend_complaint**
> VerveResponseComplaintList get_recommend_complaint(start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of recommended complaints

Returns the list of recommended complaints

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
api_instance = iengage_client.ComplaintApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Get list of recommended complaints
    api_response = api_instance.get_recommend_complaint(start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->get_recommend_complaint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaintList**](VerveResponseComplaintList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_complaints_from_db**
> VerveResponseComplaintList get_recommended_complaints_from_db(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of recommended complaints from DB

Returns the list of recommended complaints from DB

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
api_instance = iengage_client.ComplaintApi()
user_id = 789 # int | userId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Get list of recommended complaints from DB
    api_response = api_instance.get_recommended_complaints_from_db(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->get_recommended_complaints_from_db: %s\n" % e)
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
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaintList**](VerveResponseComplaintList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_users_from_db**
> VerveResponseUserList get_recommended_users_from_db(complaint_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of recommended Users from DB

Returns the list of recommended users from DB

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'userId,firstName,lastName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)profileImage<br/><b>A) Available values-</b><br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)emailId<br/>5)profileImage<br/>6)birthDate<br/>7)currentUserFollowing<br/>8)currentUserFriend<br/>9)equityScore (optional) (default to userId,firstName,lastName)

try: 
    # Get list of recommended Users from DB
    api_response = api_instance.get_recommended_users_from_db(complaint_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->get_recommended_users_from_db: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)profileImage&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)emailId&lt;br/&gt;5)profileImage&lt;br/&gt;6)birthDate&lt;br/&gt;7)currentUserFollowing&lt;br/&gt;8)currentUserFriend&lt;br/&gt;9)equityScore | [optional] [default to userId,firstName,lastName]

### Return type

[**VerveResponseUserList**](VerveResponseUserList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solutions**
> VerveResponseSolutionList get_solutions(complaint_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of solutions by ComplaintId

Return the list of solutions

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'solutionId,solutionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/><b>A) Available values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/>4)complaintId<br/>5)solvingUser<br/>6)isMarkedSolution<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to solutionId,solutionDescription,createdDate)

try: 
    # Get list of solutions by ComplaintId
    api_response = api_instance.get_solutions(complaint_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->get_solutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)complaintId&lt;br/&gt;5)solvingUser&lt;br/&gt;6)isMarkedSolution&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to solutionId,solutionDescription,createdDate]

### Return type

[**VerveResponseSolutionList**](VerveResponseSolutionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_complaints**
> VerveResponseComplaintList get_user_complaints(user_id, complaint_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)

Get list of complaints shared by user

Returns the list of complaints shared by the user himself

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
api_instance = iengage_client.ComplaintApi()
user_id = 789 # int | userId
complaint_status = 'complaint_status_example' # str | Complaint status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Get list of complaints shared by user
    api_response = api_instance.get_user_complaints(user_id, complaint_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->get_user_complaints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **complaint_status** | **str**| Complaint status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaintList**](VerveResponseComplaintList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscribed_complaint_categories**
> VerveResponseComplaintCategoryList get_user_subscribed_complaint_categories(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of Complaint categories subscribed by user

Returns the list of complaint categories subscribed by user himself

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
api_instance = iengage_client.ComplaintApi()
user_id = 789 # int | userId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2) categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Get list of Complaint categories subscribed by user
    api_response = api_instance.get_user_subscribed_complaint_categories(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->get_user_subscribed_complaint_categories: %s\n" % e)
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
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2) categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseComplaintCategoryList**](VerveResponseComplaintCategoryList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscribed_complaints**
> VerveResponseComplaintList get_user_subscribed_complaints(user_id, complaint_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)

Get list of complaints subscribed by user

Returns the list of complaints subscribed by user himself

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
api_instance = iengage_client.ComplaintApi()
user_id = 789 # int | userId
complaint_status = 'complaint_status_example' # str | Complaint status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Get list of complaints subscribed by user
    api_response = api_instance.get_user_subscribed_complaints(user_id, complaint_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->get_user_subscribed_complaints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **complaint_status** | **str**| Complaint status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaintList**](VerveResponseComplaintList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **like_solution**
> VerveResponseSolution like_solution(complaint_id, solution_id, logged_in_user_id, access_token, client_token, fields=fields)

Like solution

Allows the user to like the solution. Returns the liked solution

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
solution_id = 789 # int | solutionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'solutionId,solutionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/><b>A) Available values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/>4)complaintId<br/>5)solvingUser<br/>6)isMarkedSolution<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to solutionId,solutionDescription,createdDate)

try: 
    # Like solution
    api_response = api_instance.like_solution(complaint_id, solution_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->like_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **solution_id** | **int**| solutionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)complaintId&lt;br/&gt;5)solvingUser&lt;br/&gt;6)isMarkedSolution&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to solutionId,solutionDescription,createdDate]

### Return type

[**VerveResponseSolution**](VerveResponseSolution.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_as_an_solution**
> VerveResponseSolution mark_as_an_solution(complaint_id, solution_id, logged_in_user_id, access_token, client_token, fields=fields)

Mark solution as a solution

Allows the user to mark a solution. This means user is satisfied with the solution & the complaint will be closed

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
solution_id = 789 # int | solutionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'solutionId,solutionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/><b>A) Available values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/>4)complaintId<br/>5)solvingUser<br/>6)isMarkedSolution<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to solutionId,solutionDescription,createdDate)

try: 
    # Mark solution as a solution
    api_response = api_instance.mark_as_an_solution(complaint_id, solution_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->mark_as_an_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **solution_id** | **int**| solutionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)complaintId&lt;br/&gt;5)solvingUser&lt;br/&gt;6)isMarkedSolution&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to solutionId,solutionDescription,createdDate]

### Return type

[**VerveResponseSolution**](VerveResponseSolution.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_complaints**
> VerveResponseComplaint search_complaints(search_text, complaint_status, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of complaints by search

Returns the list of matching complaints

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
api_instance = iengage_client.ComplaintApi()
search_text = 'search_text_example' # str | Enter text to be searched
complaint_status = 'complaint_status_example' # str | Complaint status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Get list of complaints by search
    api_response = api_instance.search_complaints(search_text, complaint_status, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->search_complaints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Enter text to be searched | 
 **complaint_status** | **str**| Complaint status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaint**](VerveResponseComplaint.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_complaint**
> VerveResponseComplaint subscribe_complaint(complaint_id, logged_in_user_id, access_token, client_token, fields=fields)

Subscribe complaint

Allows the user to subscribe a complaint. Returns the subscibed complaint

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Subscribe complaint
    api_response = api_instance.subscribe_complaint(complaint_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->subscribe_complaint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaint**](VerveResponseComplaint.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_complaint_category**
> VerveResponseComplaintCategory subscribe_complaint_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)

Subscribe complaint category

Allows the user to subscribe complaint category. Returns the subscribed complaint category.

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
api_instance = iengage_client.ComplaintApi()
category_id = 789 # int | categoryId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2) categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Subscribe complaint category
    api_response = api_instance.subscribe_complaint_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->subscribe_complaint_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2) categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseComplaintCategory**](VerveResponseComplaintCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmark_as_an_solution**
> VerveResponseSolution unmark_as_an_solution(complaint_id, solution_id, logged_in_user_id, access_token, client_token, fields=fields)

Unmark solution as a solution

Allows the user to unmark a solution. This will remove the marked solution.

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
solution_id = 789 # int | solutionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'solutionId,solutionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/><b>A) Available values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/>4)complaintId<br/>5)solvingUser<br/>6)isMarkedSolution<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to solutionId,solutionDescription,createdDate)

try: 
    # Unmark solution as a solution
    api_response = api_instance.unmark_as_an_solution(complaint_id, solution_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->unmark_as_an_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **solution_id** | **int**| solutionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)complaintId&lt;br/&gt;5)solvingUser&lt;br/&gt;6)isMarkedSolution&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to solutionId,solutionDescription,createdDate]

### Return type

[**VerveResponseSolution**](VerveResponseSolution.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_complaint**
> VerveResponseComplaint unsubscribe_complaint(complaint_id, logged_in_user_id, access_token, client_token, fields=fields)

Unsubscribe Complaint

Allows the user to unsubscribe complaint. Returns the unsubscribed complaint

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Unsubscribe Complaint
    api_response = api_instance.unsubscribe_complaint(complaint_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->unsubscribe_complaint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaint**](VerveResponseComplaint.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_complaint_category**
> VerveResponseComplaintCategory unsubscribe_complaint_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)

Unsubscribe complaint category

Allows the user to unsubscribe complaint category. Returns the unsubscribed complaint category

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
api_instance = iengage_client.ComplaintApi()
category_id = 789 # int | categoryId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2) categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Unsubscribe complaint category
    api_response = api_instance.unsubscribe_complaint_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->unsubscribe_complaint_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2) categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseComplaintCategory**](VerveResponseComplaintCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_complaint**
> VerveResponseComplaint update_complaint(complaint_id, complaint_title, complaint_description, logged_in_user_id, access_token, client_token, fields=fields)

Update complaint

Allows the user to update complaint. Returns the updated complaint

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
api_instance = iengage_client.ComplaintApi()
complaint_id = 789 # int | complaintId
complaint_title = 'complaint_title_example' # str | Complaint Title
complaint_description = 'complaint_description_example' # str | Describe Complaint
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'complaintId,complaintTitle,complaintDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)createdDate<br/><b>A) Availablevalues-</b><br/>1)complaintId<br/>2)complaintTitle<br/>3)complaintDescription<br/>4)issuer<br/>5)noOfSolutions<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to complaintId,complaintTitle,complaintDescription,createdDate)

try: 
    # Update complaint
    api_response = api_instance.update_complaint(complaint_id, complaint_title, complaint_description, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->update_complaint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| complaintId | 
 **complaint_title** | **str**| Complaint Title | 
 **complaint_description** | **str**| Describe Complaint | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Availablevalues-&lt;/b&gt;&lt;br/&gt;1)complaintId&lt;br/&gt;2)complaintTitle&lt;br/&gt;3)complaintDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfSolutions&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to complaintId,complaintTitle,complaintDescription,createdDate]

### Return type

[**VerveResponseComplaint**](VerveResponseComplaint.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_complaint_category**
> VerveResponseComplaintCategory update_complaint_category(category_id, category_name, category_description, logged_in_user_id, access_token, client_token, fields=fields)

Update complaint category

Returns the updated complaint category

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
api_instance = iengage_client.ComplaintApi()
category_id = 789 # int | categoryId
category_name = 'category_name_example' # str | Category Name
category_description = 'category_description_example' # str | Describe category
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2) categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Update complaint category
    api_response = api_instance.update_complaint_category(category_id, category_name, category_description, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->update_complaint_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **category_name** | **str**| Category Name | 
 **category_description** | **str**| Describe category | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2) categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseComplaintCategory**](VerveResponseComplaintCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution**
> VerveResponseSolution update_solution(solution_id, solution, logged_in_user_id, access_token, client_token, fields=fields)

Update solution

Allows the user to update solution. Returns the updated solution

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
api_instance = iengage_client.ComplaintApi()
solution_id = 789 # int | solutionId
solution = 'solution_example' # str | solution
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'solutionId,solutionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/><b>A) Available values -</b> <br/>1)solutionId<br/>2)solutionDescription<br/>3)createdDate<br/>4)complaintId<br/>5)solvingUser<br/>6)isMarkedSolution<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to solutionId,solutionDescription,createdDate)

try: 
    # Update solution
    api_response = api_instance.update_solution(solution_id, solution, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplaintApi->update_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | **int**| solutionId | 
 **solution** | **str**| solution | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)solutionId&lt;br/&gt;2)solutionDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)complaintId&lt;br/&gt;5)solvingUser&lt;br/&gt;6)isMarkedSolution&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to solutionId,solutionDescription,createdDate]

### Return type

[**VerveResponseSolution**](VerveResponseSolution.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

