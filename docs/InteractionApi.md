# iengage_client.InteractionApi

All URIs are relative to *https://api.iengage.io:8243/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_interaction**](InteractionApi.md#add_interaction) | **POST** /interactions | Share interaction without attachment
[**add_interaction_0**](InteractionApi.md#add_interaction_0) | **POST** /interactions/attachment | Share interaction with attachment
[**add_response**](InteractionApi.md#add_response) | **POST** /interactions/{interactionId}/responses | Response the specified interaction
[**change_interaction_category**](InteractionApi.md#change_interaction_category) | **PUT** /interactions/{interactionId}/{categoryId} | Change interaction category
[**change_interaction_type**](InteractionApi.md#change_interaction_type) | **PUT** /interactions/{interactionId}/type | Change interaction type
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
> VerveResponseInteraction add_interaction(requester_id, client_token, body=body, access_token=access_token)

Share interaction without attachment

This service allows a user to post an interaction. The following fields(key:value) are required to be present in the Interaction JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API.</br><b>Required fields </br>1. interactionTitle </br>

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
api_instance = iengage_client.InteractionApi()
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body = iengage_client.InteractionInputModel() # InteractionInputModel |  (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Share interaction without attachment
    api_response = api_instance.add_interaction(requester_id, client_token, body=body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->add_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body** | [**InteractionInputModel**](InteractionInputModel.md)|  | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_interaction_0**
> VerveResponseInteraction add_interaction_0(interaction_title, file, requester_id, client_token, category_id=category_id, interaction_type=interaction_type, interaction_description=interaction_description, association=association, access_token=access_token)

Share interaction with attachment

Allows the user to share interaction with attachment. Returns the interaction object

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
api_instance = iengage_client.InteractionApi()
interaction_title = 'interaction_title_example' # str | interactionTitle
file = '/path/to/file.txt' # file | file
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 'category_id_example' # str | categoryId (optional)
interaction_type = 'interaction_type_example' # str | interactionType (optional)
interaction_description = 'interaction_description_example' # str | interactionDescription (optional)
association = 'association_example' # str | association (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Share interaction with attachment
    api_response = api_instance.add_interaction_0(interaction_title, file, requester_id, client_token, category_id=category_id, interaction_type=interaction_type, interaction_description=interaction_description, association=association, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->add_interaction_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_title** | **str**| interactionTitle | 
 **file** | **file**| file | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **str**| categoryId | [optional] 
 **interaction_type** | **str**| interactionType | [optional] 
 **interaction_description** | **str**| interactionDescription | [optional] 
 **association** | **str**| association | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_response**
> VerveResponseInteractionResponse add_response(interaction_id, requester_id, client_token, body=body, access_token=access_token)

Response the specified interaction

This service allows a user to post a response on an interaction. The following fields(key:value) are required to be present in the Response JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API.</br><b>Required fields </br>1. interactionId (Path Parameter)</br>2. responseDescription </br>

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body = iengage_client.InteractionResponse() # InteractionResponse |  (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Response the specified interaction
    api_response = api_instance.add_response(interaction_id, requester_id, client_token, body=body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->add_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body** | [**InteractionResponse**](InteractionResponse.md)|  | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_interaction_category**
> VerveResponseInteraction change_interaction_category(interaction_id, category_id, requester_id, client_token, fields=fields, access_token=access_token)

Change interaction category

Allows the user to change the interaction category.

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
category_id = 789 # int | New interaction categoryId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Change interaction category
    api_response = api_instance.change_interaction_category(interaction_id, category_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->change_interaction_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **category_id** | **int**| New interaction categoryId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_interaction_type**
> VerveResponseInteraction change_interaction_type(interaction_id, interaction_type, requester_id, client_token, fields=fields, access_token=access_token)

Change interaction type

Allows the user to change the interaction type. Boolean value

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
interaction_type = 'interaction_type_example' # str | New interaction type
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Change interaction type
    api_response = api_instance.change_interaction_type(interaction_id, interaction_type, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->change_interaction_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **interaction_type** | **str**| New interaction type | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_interaction_category**
> VerveResponseInteractionCategory create_interaction_category(requester_id, client_token, body=body, access_token=access_token)

Create interaction category

This service allows a user to create a category. The following fields(key:value) are required to be present in the Category JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API.</br><b>Required fields </br>1. associationId </br>2. categoryName </br>3. interactionType </br>

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
api_instance = iengage_client.InteractionApi()
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body = iengage_client.InteractionCategory() # InteractionCategory |  (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Create interaction category
    api_response = api_instance.create_interaction_category(requester_id, client_token, body=body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->create_interaction_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body** | [**InteractionCategory**](InteractionCategory.md)|  | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionCategory**](VerveResponseInteractionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_interaction**
> VerveResponseInteraction delete_interaction(interaction_id, requester_id, client_token, fields=fields, access_token=access_token)

Delete interaction

Allows the user to delete a interaction. Returns the deleted response

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Delete interaction
    api_response = api_instance.delete_interaction(interaction_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->delete_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_interaction_category**
> VerveResponseInteractionCategory delete_interaction_category(category_id, requester_id, client_token, fields=fields, access_token=access_token)

Delete interaction category

Allows the user to delete the interaction category. Returns the deleted interaction category

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
api_instance = iengage_client.InteractionApi()
category_id = 789 # int | categoryId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Delete interaction category
    api_response = api_instance.delete_interaction_category(category_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->delete_interaction_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionCategory**](VerveResponseInteractionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_response**
> VerveResponseInteractionResponse delete_response(response_id, requester_id, client_token, fields=fields, access_token=access_token)

Delete response

Allows the user to delete an response. Returns the deleted response

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
api_instance = iengage_client.InteractionApi()
response_id = 789 # int | responseId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Delete response
    api_response = api_instance.delete_response(response_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->delete_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| responseId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dislike_response**
> VerveResponseInteractionResponse dislike_response(interaction_id, response_id, requester_id, client_token, fields=fields, access_token=access_token)

Dislike response

Allows the user to dislike the response.

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
response_id = 789 # int | responseId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Dislike response
    api_response = api_instance.dislike_response(interaction_id, response_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->dislike_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **response_id** | **int**| responseId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_friends_interactions**
> VerveResponseInteractionList get_friends_interactions(interaction_status, start, end, requester_id, client_token, interaction_type=interaction_type, category_id=category_id, association=association, fields=fields, access_token=access_token)

Get list of interactions shared by friends

Returns the list of interactions shared by friends

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
api_instance = iengage_client.InteractionApi()
interaction_status = 'interaction_status_example' # str | Interaction status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
category_id = 789 # int | categoryId (optional)
association = 'association_example' # str | association (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of interactions shared by friends
    api_response = api_instance.get_friends_interactions(interaction_status, start, end, requester_id, client_token, interaction_type=interaction_type, category_id=category_id, association=association, fields=fields, access_token=access_token)
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
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **category_id** | **int**| categoryId | [optional] 
 **association** | **str**| association | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interaction**
> VerveResponseInteraction get_interaction(interaction_id, requester_id, client_token, fields=fields, access_token=access_token)

Get interaction by id

Returns the interaction by id

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get interaction by id
    api_response = api_instance.get_interaction(interaction_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interaction_categories**
> VerveResponseInteractionCategoryList get_interaction_categories(start, end, requester_id, client_token, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)

Get the list of interaction categories

Returns the list of interaction categories

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
api_instance = iengage_client.InteractionApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
association = 'association_example' # str | association (optional)
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get the list of interaction categories
    api_response = api_instance.get_interaction_categories(start, end, requester_id, client_token, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_interaction_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **association** | **str**| association | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionCategoryList**](VerveResponseInteractionCategoryList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interactions_for_user**
> VerveResponseInteractionList get_interactions_for_user(interaction_status, start, end, requester_id, client_token, category_id=category_id, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)

Get list of all interactions visible to the user

Returns the list of all interactions visible to the user

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
api_instance = iengage_client.InteractionApi()
interaction_status = 'interaction_status_example' # str | Interaction status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
association = 'association_example' # str | association (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of all interactions visible to the user
    api_response = api_instance.get_interactions_for_user(interaction_status, start, end, requester_id, client_token, category_id=category_id, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)
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
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **association** | **str**| association | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommend_interactions**
> VerveResponseInteractionList get_recommend_interactions(start, end, requester_id, client_token, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)

Get list of recommended interactions

Returns the list of recommended interactions

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
api_instance = iengage_client.InteractionApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | interactionType (optional)
association = 'association_example' # str | association (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of recommended interactions
    api_response = api_instance.get_recommend_interactions(start, end, requester_id, client_token, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_recommend_interactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| interactionType | [optional] 
 **association** | **str**| association | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_interactins_from_db**
> VerveResponseInteractionList get_recommended_interactins_from_db(user_id, start, end, requester_id, client_token, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)

Get list of recommended interactions from DB

Returns the list of recommended interactions from DB

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
api_instance = iengage_client.InteractionApi()
user_id = 789 # int | User Id whose recommended interactions want to get
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
association = 'association_example' # str | association (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of recommended interactions from DB
    api_response = api_instance.get_recommended_interactins_from_db(user_id, start, end, requester_id, client_token, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_recommended_interactins_from_db: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id whose recommended interactions want to get | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **association** | **str**| association | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_users_from_db**
> VerveResponseUserList get_recommended_users_from_db(interaction_id, start, end, requester_id, client_token, association=association, fields=fields, access_token=access_token)

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
association = 'association_example' # str | association (optional)
fields = 'userId,firstName,lastName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)profileImage<br/><b>A) Available values-</b><br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)emailId<br/>5)profileImage<br/>6)birthDate<br/> (optional) (default to userId,firstName,lastName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of recommended Users from DB
    api_response = api_instance.get_recommended_users_from_db(interaction_id, start, end, requester_id, client_token, association=association, fields=fields, access_token=access_token)
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
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **association** | **str**| association | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)profileImage&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)userId&lt;br/&gt;2)firstName&lt;br/&gt;3)lastName&lt;br/&gt;4)emailId&lt;br/&gt;5)profileImage&lt;br/&gt;6)birthDate&lt;br/&gt; | [optional] [default to userId,firstName,lastName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseUserList**](VerveResponseUserList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_responses**
> VerveResponseInteractionResponseList get_responses(interaction_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)

Get list of responses by interactionId

Returns the list of responses by interactionId

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of responses by interactionId
    api_response = api_instance.get_responses(interaction_id, start, end, requester_id, client_token, fields=fields, access_token=access_token)
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
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionResponseList**](VerveResponseInteractionResponseList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_interactions**
> VerveResponseInteractionList get_user_interactions(user_id, interaction_status, start, end, requester_id, client_token, category_id=category_id, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)

Get list of interactions shared by user

Returns the list of interactions shared by specific user

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
api_instance = iengage_client.InteractionApi()
user_id = 789 # int | userId whose shared interactions want to get
interaction_status = 'interaction_status_example' # str | Interaction status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
association = 'association_example' # str | association (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of interactions shared by user
    api_response = api_instance.get_user_interactions(user_id, interaction_status, start, end, requester_id, client_token, category_id=category_id, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_user_interactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId whose shared interactions want to get | 
 **interaction_status** | **str**| Interaction status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **association** | **str**| association | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscribed_interaction_categories**
> VerveResponseInteractionCategoryList get_user_subscribed_interaction_categories(user_id, start, end, requester_id, client_token, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)

Get list of interaction categories subscribed by the user

Returns the list of interaction categories subscribed by the user

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
api_instance = iengage_client.InteractionApi()
user_id = 789 # int | User Id whose subcripbed category want to get
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | interactionType (optional)
association = 'association_example' # str | association (optional)
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of interaction categories subscribed by the user
    api_response = api_instance.get_user_subscribed_interaction_categories(user_id, start, end, requester_id, client_token, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_user_subscribed_interaction_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id whose subcripbed category want to get | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| interactionType | [optional] 
 **association** | **str**| association | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionCategoryList**](VerveResponseInteractionCategoryList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscribed_interactions**
> VerveResponseInteractionList get_user_subscribed_interactions(user_id, interaction_status, start, end, requester_id, client_token, category_id=category_id, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)

Get list of interactions subscribed by user

Returns the list of interactions subscribed by specific user

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
api_instance = iengage_client.InteractionApi()
user_id = 789 # int | User Id whose subcribed interactions wants to get
interaction_status = 'interaction_status_example' # str | Interaction status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
association = 'association_example' # str | association (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of interactions subscribed by user
    api_response = api_instance.get_user_subscribed_interactions(user_id, interaction_status, start, end, requester_id, client_token, category_id=category_id, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_user_subscribed_interactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id whose subcribed interactions wants to get | 
 **interaction_status** | **str**| Interaction status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **association** | **str**| association | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **like_response**
> VerveResponseInteractionResponse like_response(interaction_id, response_id, requester_id, client_token, fields=fields, access_token=access_token)

Like response

Allows the user to like the response.

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
response_id = 789 # int | responseId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Like response
    api_response = api_instance.like_response(interaction_id, response_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->like_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **response_id** | **int**| responseId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_as_an_response**
> VerveResponseInteractionResponse mark_as_an_response(interaction_id, response_id, requester_id, client_token, fields=fields, access_token=access_token)

Mark response as a response

Marks the response as accepted. This means the user is satisfied with the response & then the interaction will go into closed state

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
response_id = 789 # int | responseId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Mark response as a response
    api_response = api_instance.mark_as_an_response(interaction_id, response_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->mark_as_an_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **response_id** | **int**| responseId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_interactions**
> VerveResponseInteractionList search_interactions(search_text, interaction_status, start, end, requester_id, client_token, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)

Get list of matching interactions

Returns the list of matching interactions

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
api_instance = iengage_client.InteractionApi()
search_text = 'search_text_example' # str | Search Text, keywords to search
interaction_status = 'interaction_status_example' # str | Interaction status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | Interaction Type (optional)
association = 'association_example' # str | association (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of matching interactions
    api_response = api_instance.search_interactions(search_text, interaction_status, start, end, requester_id, client_token, interaction_type=interaction_type, association=association, fields=fields, access_token=access_token)
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
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| Interaction Type | [optional] 
 **association** | **str**| association | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionList**](VerveResponseInteractionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_interactin_category**
> VerveResponseInteractionCategory subscribe_interactin_category(category_id, requester_id, client_token, fields=fields, access_token=access_token)

Subscribe interaction category

Returns the subscribed interaction category

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
api_instance = iengage_client.InteractionApi()
category_id = 789 # int | categoryId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Subscribe interaction category
    api_response = api_instance.subscribe_interactin_category(category_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->subscribe_interactin_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionCategory**](VerveResponseInteractionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_interaction**
> VerveResponseInteraction subscribe_interaction(interaction_id, requester_id, client_token, fields=fields, access_token=access_token)

Subscribe interaction

Allows the user to subscribe a interaction

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Subscribe interaction
    api_response = api_instance.subscribe_interaction(interaction_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->subscribe_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmark_as_an_response**
> VerveResponseInteractionResponse unmark_as_an_response(interaction_id, response_id, requester_id, client_token, fields=fields, access_token=access_token)

Unmark response as a response

Unmarks the response. This will remove the marked response.

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
response_id = 789 # int | responseId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Unmark response as a response
    api_response = api_instance.unmark_as_an_response(interaction_id, response_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->unmark_as_an_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **response_id** | **int**| responseId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_interactin_category**
> VerveResponseInteractionCategory unsubscribe_interactin_category(category_id, requester_id, client_token, fields=fields, access_token=access_token)

Unsubscribe interaction category

Returns the unsubscribed interaction category

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
api_instance = iengage_client.InteractionApi()
category_id = 789 # int | categoryId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Unsubscribe interaction category
    api_response = api_instance.unsubscribe_interactin_category(category_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->unsubscribe_interactin_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionCategory**](VerveResponseInteractionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_interaction**
> VerveResponseInteraction unsubscribe_interaction(interaction_id, requester_id, client_token, fields=fields, access_token=access_token)

Unsubscribe interaction

Allows the user to unsubscribe a interaction

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Unsubscribe interaction
    api_response = api_instance.unsubscribe_interaction(interaction_id, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->unsubscribe_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_interaction**
> VerveResponseInteraction update_interaction(interaction_id, interaction_title, requester_id, client_token, interaction_description=interaction_description, fields=fields, access_token=access_token)

Update interaction

Allows the user to update interaction. Returns the updated interaction

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
api_instance = iengage_client.InteractionApi()
interaction_id = 789 # int | interactionId
interaction_title = 'interaction_title_example' # str | Interaction Title
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_description = 'interaction_description_example' # str | Describe Interaction (optional)
fields = 'interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)createdDate<br/>5)interactionType<br/><b>A) Available values-</b><br/>1)interactionId<br/>2)interactionTitle<br/>3)interactionDescription<br/>4)issuer<br/>5)noOfResponses<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity<br/>14)interactionType<br/>15)categoryId<br/>16)categoryName (optional) (default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Update interaction
    api_response = api_instance.update_interaction(interaction_id, interaction_title, requester_id, client_token, interaction_description=interaction_description, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->update_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **int**| interactionId | 
 **interaction_title** | **str**| Interaction Title | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_description** | **str**| Describe Interaction | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)interactionType&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)interactionId&lt;br/&gt;2)interactionTitle&lt;br/&gt;3)interactionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfResponses&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity&lt;br/&gt;14)interactionType&lt;br/&gt;15)categoryId&lt;br/&gt;16)categoryName | [optional] [default to interactionId,interactionTitle,interactionDescription,createdDate,interactionType,categoryName]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteraction**](VerveResponseInteraction.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_interaction_category**
> VerveResponseInteractionCategory update_interaction_category(category_id, category_name, requester_id, client_token, category_description=category_description, fields=fields, access_token=access_token)

Update interaction category

Allows the user to update the interaction category. Returns the updated interaction category

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
api_instance = iengage_client.InteractionApi()
category_id = 789 # int | categoryId
category_name = 'category_name_example' # str | Category Name
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_description = 'category_description_example' # str | Describe category (optional)
fields = 'categoryId,categoryName,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)interactionType<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed<br/>6)interactionType (optional) (default to categoryId,categoryName,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Update interaction category
    api_response = api_instance.update_interaction_category(category_id, category_name, requester_id, client_token, category_description=category_description, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->update_interaction_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **category_name** | **str**| Category Name | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_description** | **str**| Describe category | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed&lt;br/&gt;6)interactionType | [optional] [default to categoryId,categoryName,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionCategory**](VerveResponseInteractionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_response**
> VerveResponseInteractionResponse update_response(response_id, response, requester_id, client_token, fields=fields, access_token=access_token)

Update response

Allows the user to update an response. Returns the updated response

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
api_instance = iengage_client.InteractionApi()
response_id = 789 # int | responseId
response = 'response_example' # str | response
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'responseId,responseDescription,createdDate,interactionType' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionType<br/><b>A) Available values -</b><br/>1)responseId<br/>2)responseDescription<br/>3)createdDate<br/>4)interactionId<br/>5)respondingUser<br/>6)isMarkedResponse<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked<br/>12)interactionType (optional) (default to responseId,responseDescription,createdDate,interactionType)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Update response
    api_response = api_instance.update_response(response_id, response, requester_id, client_token, fields=fields, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->update_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| responseId | 
 **response** | **str**| response | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionType&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)responseId&lt;br/&gt;2)responseDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)interactionId&lt;br/&gt;5)respondingUser&lt;br/&gt;6)isMarkedResponse&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked&lt;br/&gt;12)interactionType | [optional] [default to responseId,responseDescription,createdDate,interactionType]
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseInteractionResponse**](VerveResponseInteractionResponse.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

