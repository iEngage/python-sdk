# iengage-client.InteractionApi

All URIs are relative to *https://api.iengage.io:8243/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_interaction**](InteractionApi.md#add_interaction) | **POST** /interactions | Share interaction without attachment
[**add_interaction_0**](InteractionApi.md#add_interaction_0) | **POST** /interactions/attachment | Share interaction with attachment
[**add_response**](InteractionApi.md#add_response) | **POST** /interactions/{interactionId}/responses | Response the specified interaction
[**create_interaction_category**](InteractionApi.md#create_interaction_category) | **POST** /interactions/categories | Create interaction category
[**delete_interaction**](InteractionApi.md#delete_interaction) | **DELETE** /interactions/{interactionId} | Delete interaction
[**delete_interaction_category**](InteractionApi.md#delete_interaction_category) | **DELETE** /interactions/categories/{categoryId} | Delete interaction category
[**delete_response**](InteractionApi.md#delete_response) | **DELETE** /interactions/responses/{responseId} | Delete response
[**dislike_response**](InteractionApi.md#dislike_response) | **POST** /interactions/{interactionId}/responses/{responseId}/dislike | Dislike response
[**get_friends_interactions**](InteractionApi.md#get_friends_interactions) | **GET** /interactions/friends | Get list of interactions shared by friends
[**get_interaction**](InteractionApi.md#get_interaction) | **GET** /interactions/{interactionId} | Get interaction by id
[**get_interaction_categories**](InteractionApi.md#get_interaction_categories) | **GET** /interactions/categories | Get the list of interaction categories
[**get_interactions_for_user**](InteractionApi.md#get_interactions_for_user) | **GET** /interactions | Get list of all interactions visible to the user
[**get_recommend_interactions**](InteractionApi.md#get_recommend_interactions) | **GET** /interactions/recommend | Get list of recommended interactions
[**get_recommended_interactins_from_db**](InteractionApi.md#get_recommended_interactins_from_db) | **GET** /interactions/{userId}/recommendedInteractions | Get list of recommended interactions from DB
[**get_recommended_users_from_db**](InteractionApi.md#get_recommended_users_from_db) | **GET** /interactions/{interactionId}/recommendedUsers | Get list of recommended Users from DB
[**get_responses**](InteractionApi.md#get_responses) | **GET** /interactions/{interactionId}/responses | Get list of responses by interactionId
[**get_user_interactions**](InteractionApi.md#get_user_interactions) | **GET** /interactions/{userId}/shared | Get list of interactions shared by user
[**get_user_subscribed_interaction_categories**](InteractionApi.md#get_user_subscribed_interaction_categories) | **GET** /interactions/categories/{userId}/subscribe | Get list of interaction categories subscribed by the user
[**get_user_subscribed_interactions**](InteractionApi.md#get_user_subscribed_interactions) | **GET** /interactions/{userId}/subscribe | Get list of interactions subscribed by user
[**like_response**](InteractionApi.md#like_response) | **POST** /interactions/{interactionId}/responses/{responseId}/like | Like response
[**mark_as_an_response**](InteractionApi.md#mark_as_an_response) | **POST** /interactions/{interactionId}/responses/{responseId}/mark | Mark response as a response
[**search_interactions**](InteractionApi.md#search_interactions) | **GET** /interactions/search | Get list of matching interactions
[**subscribe_interactin_category**](InteractionApi.md#subscribe_interactin_category) | **POST** /interactions/categories/{categoryId}/subscribe | Subscribe interaction category
[**subscribe_interaction**](InteractionApi.md#subscribe_interaction) | **POST** /interactions/{interactionId}/subscribe | Subscribe interaction
[**unmark_as_an_response**](InteractionApi.md#unmark_as_an_response) | **POST** /interactions/{interactionId}/responses/{responseId}/unmark | Unmark response as a response
[**unsubscribe_interactin_category**](InteractionApi.md#unsubscribe_interactin_category) | **POST** /interactions/categories/{categoryId}/unsubscribe | Unsubscribe interaction category
[**unsubscribe_interaction**](InteractionApi.md#unsubscribe_interaction) | **POST** /interactions/{interactionId}/unsubscribe | Unsubscribe interaction
[**update_interaction**](InteractionApi.md#update_interaction) | **PUT** /interactions/{interactionId} | Update interaction
[**update_interaction_category**](InteractionApi.md#update_interaction_category) | **PUT** /interactions/categories/{categoryId} | Update interaction category
[**update_response**](InteractionApi.md#update_response) | **PUT** /interactions/responses/{responseId} | Update response


# **add_interaction**
> VerveResponseInteraction add_interaction(interaction_title, logged_in_user_id, access_token, client_token, category_id=category_id, interaction_type=interaction_type, interaction_description=interaction_description)

Share interaction without attachment

Allows the user to share interaction without attachment. Returns the interaction object

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
api_instance = iengage-client.InteractionApi()
interaction_title = 'interaction_title_example' # str | Interaction Title
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
interaction_description = 'interaction_description_example' # str | Describe interaction (optional)

try: 
    # Share interaction without attachment
    api_response = api_instance.add_interaction(interaction_title, logged_in_user_id, access_token, client_token, category_id=category_id, interaction_type=interaction_type, interaction_description=interaction_description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->add_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_title** | **str**| Interaction Title | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **interaction_description** | **str**| Describe interaction | [optional] 

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_interaction_0**
> VerveResponseInteraction add_interaction_0(body3, logged_in_user_id, access_token, client_token, body=body, body2=body2, body4=body4, body5=body5)

Share interaction with attachment

Allows the user to share interaction with attachment. Returns the interaction object

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
api_instance = iengage-client.InteractionApi()
body3 = 'body_example' # str | interactionTitle
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body = 789 # int | categoryId (optional)
body2 = 'body_example' # str | Interaction Type (optional)
body4 = 'body_example' # str | interactionDescription (optional)
body5 = [iengage-client.Attachment()] # list[Attachment] |  (optional)

try: 
    # Share interaction with attachment
    api_response = api_instance.add_interaction_0(body3, logged_in_user_id, access_token, client_token, body=body, body2=body2, body4=body4, body5=body5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->add_interaction_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body3** | **str**| interactionTitle | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body** | **int**| categoryId | [optional] 
 **body2** | **str**| Interaction Type | [optional] 
 **body4** | **str**| interactionDescription | [optional] 
 **body5** | [**list[Attachment]**](Attachment.md)|  | [optional] 

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_response**
> VerveResponseInteractionResponse add_response(interaction_id, response, logged_in_user_id, access_token, client_token, fields=fields)

Response the specified interaction

Allows the user to response the interaction

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
response = 'response_example' # str | response
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)

try: 
    # Response the specified interaction
    api_response = api_instance.add_response(interaction_id, response, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->add_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **response** | **str**| response | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_interaction_category**
> VerveResponseInteractionCategory create_interaction_category(interaction_type, name, description, logged_in_user_id, access_token, client_token, organization_id=organization_id, fields=fields)

Create interaction category

Creates a interaction category. Returns the created interaction category

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
api_instance = iengage-client.InteractionApi()
interaction_type = 'interaction_type_example' # str | Interaction Type
name = 'name_example' # str | Name
description = 'description_example' # str | description
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
organization_id = 789 # int | OrganizationId (optional)
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)

try: 
    # Create interaction category
    api_response = api_instance.create_interaction_category(interaction_type, name, description, logged_in_user_id, access_token, client_token, organization_id=organization_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->create_interaction_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_type** | **str**| Interaction Type | 
 **name** | **str**| Name | 
 **description** | **str**| description | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **organization_id** | **int**| OrganizationId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]

### Return type

[**VerveResponseInteractionCategory**](VerveResponseInteractionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_interaction**
> VerveResponseInteraction delete_interaction(interaction_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete interaction

Allows the user to delete a interaction. Returns the deleted response

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType)

try: 
    # Delete interaction
    api_response = api_instance.delete_interaction(interaction_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->delete_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_interaction_category**
> VerveResponseInteractionCategory delete_interaction_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete interaction category

Allows the user to delete the interaction category. Returns the deleted interaction category

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
api_instance = iengage-client.InteractionApi()
category_id = 789 # int | categoryId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)

try: 
    # Delete interaction category
    api_response = api_instance.delete_interaction_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->delete_interaction_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]

### Return type

[**VerveResponseInteractionCategory**](VerveResponseInteractionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_response**
> VerveResponseInteractionResponse delete_response(response_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete response

Allows the user to delete an response. Returns the deleted response

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
api_instance = iengage-client.InteractionApi()
response_id = 789 # int | responseId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)

try: 
    # Delete response
    api_response = api_instance.delete_response(response_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->delete_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| responseId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dislike_response**
> VerveResponseInteractionResponse dislike_response(interaction_id, response_id, logged_in_user_id, access_token, client_token, fields=fields)

Dislike response

Allows the user to dislike the response.

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
response_id = 789 # int | responseId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)

try: 
    # Dislike response
    api_response = api_instance.dislike_response(interaction_id, response_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->dislike_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **response_id** | **int**| responseId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_friends_interactions**
> VerveResponseInteractionList get_friends_interactions(interaction_status, start, end, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, category_id=category_id, fields=fields)

Get list of interactions shared by friends

Returns the list of interactions shared by friends

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
api_instance = iengage-client.InteractionApi()
interaction_status = 'interaction_status_example' # str | Interaction status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
category_id = 789 # int | categoryId (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType)

try: 
    # Get list of interactions shared by friends
    api_response = api_instance.get_friends_interactions(interaction_status, start, end, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, category_id=category_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_friends_interactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_status** | **str**| Interaction status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **category_id** | **int**| categoryId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interaction**
> VerveResponseInteraction get_interaction(interaction_id, logged_in_user_id, access_token, client_token, fields=fields)

Get interaction by id

Returns the interaction by id

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType)

try: 
    # Get interaction by id
    api_response = api_instance.get_interaction(interaction_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interaction_categories**
> VerveResponseInteractionCategoryList get_interaction_categories(start, end, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, fields=fields)

Get the list of interaction categories

Returns the list of interaction categories

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
api_instance = iengage-client.InteractionApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)

try: 
    # Get the list of interaction categories
    api_response = api_instance.get_interaction_categories(start, end, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_interaction_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]

### Return type

[**VerveResponseInteractionCategoryList**](VerveResponseInteractionCategoryList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interactions_for_user**
> VerveResponseInteractionList get_interactions_for_user(interaction_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, interaction_type=interaction_type, fields=fields)

Get list of all interactions visible to the user

Returns the list of all interactions visible to the user

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
api_instance = iengage-client.InteractionApi()
interaction_status = 'interaction_status_example' # str | Interaction status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType)

try: 
    # Get list of all interactions visible to the user
    api_response = api_instance.get_interactions_for_user(interaction_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, interaction_type=interaction_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_interactions_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_status** | **str**| Interaction status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommend_interactions**
> VerveResponseInteractionList get_recommend_interactions(start, end, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, fields=fields)

Get list of recommended interactions

Returns the list of recommended interactions

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
api_instance = iengage-client.InteractionApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | interactionType (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType)

try: 
    # Get list of recommended interactions
    api_response = api_instance.get_recommend_interactions(start, end, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_recommend_interactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| interactionType | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_interactins_from_db**
> VerveResponseInteractionList get_recommended_interactins_from_db(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of recommended interactions from DB

Returns the list of recommended interactions from DB

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
api_instance = iengage-client.InteractionApi()
user_id = 789 # int | userId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,,interactionType)

try: 
    # Get list of recommended interactions from DB
    api_response = api_instance.get_recommended_interactins_from_db(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_recommended_interactins_from_db: %s\n" % e)
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
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,,interactionType]

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_users_from_db**
> VerveResponseUserList get_recommended_users_from_db(interaction_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of recommended Users from DB

Returns the list of recommended users from DB

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'userId,firstName,lastName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)profileImage<br/><b>A) Available values-</b><br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)emailId<br/>5)profileImage<br/>6)birthDate<br/>7)currentUserFollowing<br/>8)currentUserFriend<br/>9)equityScore (optional) (default to userId,firstName,lastName)

try: 
    # Get list of recommended Users from DB
    api_response = api_instance.get_recommended_users_from_db(interaction_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_recommended_users_from_db: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
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

# **get_responses**
> VerveResponseInteractionResponseList get_responses(interaction_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of responses by interactionId

Returns the list of responses by interactionId

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)

try: 
    # Get list of responses by interactionId
    api_response = api_instance.get_responses(interaction_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_responses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionResponseList**](VerveResponseInteractionResponseList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_interactions**
> VerveResponseInteractionList get_user_interactions(user_id, interaction_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, interaction_type=interaction_type, fields=fields)

Get list of interactions shared by user

Returns the list of interactions shared by specific user

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
api_instance = iengage-client.InteractionApi()
user_id = 789 # int | userId
interaction_status = 'interaction_status_example' # str | Interaction status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType)

try: 
    # Get list of interactions shared by user
    api_response = api_instance.get_user_interactions(user_id, interaction_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, interaction_type=interaction_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_user_interactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **interaction_status** | **str**| Interaction status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscribed_interaction_categories**
> VerveResponseInteractionCategoryList get_user_subscribed_interaction_categories(user_id, interaction_type, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of interaction categories subscribed by the user

Returns the list of interaction categories subscribed by the user

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
api_instance = iengage-client.InteractionApi()
user_id = 789 # int | userId
interaction_type = 'interaction_type_example' # str | interactionType
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)

try: 
    # Get list of interaction categories subscribed by the user
    api_response = api_instance.get_user_subscribed_interaction_categories(user_id, interaction_type, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_user_subscribed_interaction_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **interaction_type** | **str**| interactionType | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]

### Return type

[**VerveResponseInteractionCategoryList**](VerveResponseInteractionCategoryList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscribed_interactions**
> VerveResponseInteractionList get_user_subscribed_interactions(user_id, interaction_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, interaction_type=interaction_type, fields=fields)

Get list of interactions subscribed by user

Returns the list of interactions subscribed by specific user

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
api_instance = iengage-client.InteractionApi()
user_id = 789 # int | userId
interaction_status = 'interaction_status_example' # str | Interaction status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType)

try: 
    # Get list of interactions subscribed by user
    api_response = api_instance.get_user_subscribed_interactions(user_id, interaction_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, interaction_type=interaction_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_user_subscribed_interactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **interaction_status** | **str**| Interaction status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **like_response**
> VerveResponseInteractionResponse like_response(interaction_id, response_id, logged_in_user_id, access_token, client_token, fields=fields)

Like response

Allows the user to like the response.

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
response_id = 789 # int | responseId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)

try: 
    # Like response
    api_response = api_instance.like_response(interaction_id, response_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->like_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **response_id** | **int**| responseId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_as_an_response**
> VerveResponseInteractionResponse mark_as_an_response(interaction_id, response_id, logged_in_user_id, access_token, client_token, fields=fields)

Mark response as a response

Marks the response as accepted. This means the user is satisfied with the response & then the interaction will go into closed state

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
response_id = 789 # int | responseId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)

try: 
    # Mark response as a response
    api_response = api_instance.mark_as_an_response(interaction_id, response_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->mark_as_an_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **response_id** | **int**| responseId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_interactions**
> VerveResponseInteractionList search_interactions(search_text, interaction_status, start, end, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, fields=fields)

Get list of matching interactions

Returns the list of matching interactions

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
api_instance = iengage-client.InteractionApi()
search_text = 'search_text_example' # str | Search Text, keywords to search
interaction_status = 'interaction_status_example' # str | Interaction status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType)

try: 
    # Get list of matching interactions
    api_response = api_instance.search_interactions(search_text, interaction_status, start, end, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->search_interactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Search Text, keywords to search | 
 **interaction_status** | **str**| Interaction status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_interactin_category**
> VerveResponseInteractionCategory subscribe_interactin_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)

Subscribe interaction category

Returns the subscribed interaction category

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
api_instance = iengage-client.InteractionApi()
category_id = 789 # int | categoryId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)

try: 
    # Subscribe interaction category
    api_response = api_instance.subscribe_interactin_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->subscribe_interactin_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]

### Return type

[**VerveResponseInteractionCategory**](VerveResponseInteractionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_interaction**
> VerveResponseInteraction subscribe_interaction(interaction_id, logged_in_user_id, access_token, client_token, fields=fields)

Subscribe interaction

Allows the user to subscribe a interaction

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType)

try: 
    # Subscribe interaction
    api_response = api_instance.subscribe_interaction(interaction_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->subscribe_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmark_as_an_response**
> VerveResponseInteractionResponse unmark_as_an_response(interaction_id, response_id, logged_in_user_id, access_token, client_token, fields=fields)

Unmark response as a response

Unmarks the response. This will remove the marked response.

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
response_id = 789 # int | responseId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)

try: 
    # Unmark response as a response
    api_response = api_instance.unmark_as_an_response(interaction_id, response_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->unmark_as_an_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **response_id** | **int**| responseId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_interactin_category**
> VerveResponseInteractionCategory unsubscribe_interactin_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)

Unsubscribe interaction category

Returns the unsubscribed interaction category

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
api_instance = iengage-client.InteractionApi()
category_id = 789 # int | categoryId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)

try: 
    # Unsubscribe interaction category
    api_response = api_instance.unsubscribe_interactin_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->unsubscribe_interactin_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]

### Return type

[**VerveResponseInteractionCategory**](VerveResponseInteractionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_interaction**
> VerveResponseInteraction unsubscribe_interaction(interaction_id, logged_in_user_id, access_token, client_token, fields=fields)

Unsubscribe interaction

Allows the user to unsubscribe a interaction

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType)

try: 
    # Unsubscribe interaction
    api_response = api_instance.unsubscribe_interaction(interaction_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->unsubscribe_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_interaction**
> VerveResponseInteraction update_interaction(interaction_id, interaction_title, interaction_description, logged_in_user_id, access_token, client_token, fields=fields)

Update interaction

Allows the user to update interaction. Returns the updated interaction

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
api_instance = iengage-client.InteractionApi()
interaction_id = 789 # int | interactionId
interaction_title = 'interaction_title_example' # str | Interaction Title
interaction_description = 'interaction_description_example' # str | Describe Interaction
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType)

try: 
    # Update interaction
    api_response = api_instance.update_interaction(interaction_id, interaction_title, interaction_description, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->update_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **interaction_title** | **str**| Interaction Title | 
 **interaction_description** | **str**| Describe Interaction | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_interaction_category**
> VerveResponseInteractionCategory update_interaction_category(category_id, category_name, category_description, logged_in_user_id, access_token, client_token, fields=fields)

Update interaction category

Allows the user to update the interaction category. Returns the updated interaction category

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
api_instance = iengage-client.InteractionApi()
category_id = 789 # int | categoryId
category_name = 'category_name_example' # str | Category Name
category_description = 'category_description_example' # str | Describe category
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)

try: 
    # Update interaction category
    api_response = api_instance.update_interaction_category(category_id, category_name, category_description, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->update_interaction_category: %s\n" % e)
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
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]

### Return type

[**VerveResponseInteractionCategory**](VerveResponseInteractionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_response**
> VerveResponseInteractionResponse update_response(response_id, response, logged_in_user_id, access_token, client_token, fields=fields)

Update response

Allows the user to update an response. Returns the updated response

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
api_instance = iengage-client.InteractionApi()
response_id = 789 # int | responseId
response = 'response_example' # str | response
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)

try: 
    # Update response
    api_response = api_instance.update_response(response_id, response, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->update_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| responseId | 
 **response** | **str**| response | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

