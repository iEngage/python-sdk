# iengage_client.AugmentedIntelligenceApi

All URIs are relative to *https://api.iengage.io:8243/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classify**](AugmentedIntelligenceApi.md#classify) | **POST** /ml/classifier/classify | Classifies using your classifier
[**get_entities**](AugmentedIntelligenceApi.md#get_entities) | **POST** /ml/ner/classify | Extracts entities from text
[**get_interaction_type**](AugmentedIntelligenceApi.md#get_interaction_type) | **POST** /ml/interactionType | Returns the type of interaction
[**get_keywords**](AugmentedIntelligenceApi.md#get_keywords) | **POST** /ml/keywords | Returns the keywords of the sentence
[**get_popular_tag**](AugmentedIntelligenceApi.md#get_popular_tag) | **GET** /analytics/popular/tags | Get list of popular tag of interactions
[**get_sentiment**](AugmentedIntelligenceApi.md#get_sentiment) | **GET** /analytics/sentiments | Get sentiment count of interactions
[**get_tag_entity_sentiments**](AugmentedIntelligenceApi.md#get_tag_entity_sentiments) | **GET** /analytics/tag/entitySentiment | Get list of tag entity sentiment
[**sentiment**](AugmentedIntelligenceApi.md#sentiment) | **POST** /ml/sentiment | Analyzes the sentiment of the content


# **classify**
> VerveResponseTextClassificationList classify(text, id, client_token)

Classifies using your classifier

Returns a classification based on your training in the Classifier Admin Panel. More than one classifier may be trained. Use the correct ID from the Admin Panel to get the corresponding classification

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
api_instance = iengage_client.AugmentedIntelligenceApi()
text = 'text_example' # str | Text you want classified
id = 789 # int | Classifier ID from the Admin Panel
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Classifies using your classifier
    api_response = api_instance.classify(text, id, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AugmentedIntelligenceApi->classify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Text you want classified | 
 **id** | **int**| Classifier ID from the Admin Panel | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseTextClassificationList**](VerveResponseTextClassificationList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entities**
> VerveResponseEntitiesClassifiedList get_entities(id, text, client_token)

Extracts entities from text

Classifies each word of the text as an entity based on your training in the NER Admin panel. More than one classifier may be trained. Use the correct ID from the Admin Panel to get the corresponding classification

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
api_instance = iengage_client.AugmentedIntelligenceApi()
id = 789 # int | NER ID present from the Admin Panel
text = 'text_example' # str | Text from which to extract entities
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Extracts entities from text
    api_response = api_instance.get_entities(id, text, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AugmentedIntelligenceApi->get_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| NER ID present from the Admin Panel | 
 **text** | **str**| Text from which to extract entities | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseEntitiesClassifiedList**](VerveResponseEntitiesClassifiedList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interaction_type**
> VerveResponseFlowFinder get_interaction_type(text, client_token)

Returns the type of interaction

Classifies text to question, complaint, appreciation, suggestion or comment. This is the default classification we assign to the type field of an Interaction

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
api_instance = iengage_client.AugmentedIntelligenceApi()
text = 'text_example' # str | Text that is to be classified by type
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Returns the type of interaction
    api_response = api_instance.get_interaction_type(text, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AugmentedIntelligenceApi->get_interaction_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Text that is to be classified by type | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseFlowFinder**](VerveResponseFlowFinder.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keywords**
> VerveResponseKeyword get_keywords(text, client_token)

Returns the keywords of the sentence

Extracts the keywords of a sentence. This could be used for example as tags.

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
api_instance = iengage_client.AugmentedIntelligenceApi()
text = 'text_example' # str | Content whose keywords are to be found out
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Returns the keywords of the sentence
    api_response = api_instance.get_keywords(text, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AugmentedIntelligenceApi->get_keywords: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Content whose keywords are to be found out | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseKeyword**](VerveResponseKeyword.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_popular_tag**
> VerveResponseTagList get_popular_tag(start_time, end_time, start, end, requester_id, client_token, interaction_type=interaction_type, sentiment_type=sentiment_type, additional_information=additional_information, association=association, category_id=category_id, access_token=access_token)

Get list of popular tag of interactions

Return the most popular tag of given interaction type

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
api_instance = iengage_client.AugmentedIntelligenceApi()
start_time = 789 # int | start time
end_time = 789 # int | end time
start = 56 # int | start
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | Interaction Type <br/>1)Question<br/>2)Complaint<br/>3)Idea<br/>4)Blog<br/>5)Discussion (optional)
sentiment_type = 'sentiment_type_example' # str | Sentiment Type <br/>1)Positive<br/>2)Negative<br/> 3)Neutral (optional)
additional_information = 'additional_information_example' # str | additional information (optional)
association = 'association_example' # str | association (optional)
category_id = 789 # int | categoryId (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of popular tag of interactions
    api_response = api_instance.get_popular_tag(start_time, end_time, start, end, requester_id, client_token, interaction_type=interaction_type, sentiment_type=sentiment_type, additional_information=additional_information, association=association, category_id=category_id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AugmentedIntelligenceApi->get_popular_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| start time | 
 **end_time** | **int**| end time | 
 **start** | **int**| start | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| Interaction Type &lt;br/&gt;1)Question&lt;br/&gt;2)Complaint&lt;br/&gt;3)Idea&lt;br/&gt;4)Blog&lt;br/&gt;5)Discussion | [optional] 
 **sentiment_type** | **str**| Sentiment Type &lt;br/&gt;1)Positive&lt;br/&gt;2)Negative&lt;br/&gt; 3)Neutral | [optional] 
 **additional_information** | **str**| additional information | [optional] 
 **association** | **str**| association | [optional] 
 **category_id** | **int**| categoryId | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseTagList**](VerveResponseTagList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sentiment**
> VerveResponseSentimentAnalytics get_sentiment(start_time, end_time, requester_id, client_token, interaction_type=interaction_type, additional_information=additional_information, association=association, category_id=category_id, access_token=access_token)

Get sentiment count of interactions

Returns the sum of the sentiment count of given interaction type

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
api_instance = iengage_client.AugmentedIntelligenceApi()
start_time = 789 # int | start time
end_time = 789 # int | end time
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | Interaction Type <br/>1)Question<br/>2)Complaint<br/>3)Idea<br/>4)Blog<br/>5)Discussion (optional)
additional_information = 'additional_information_example' # str | additional information (optional)
association = 'association_example' # str | association (optional)
category_id = 789 # int | categoryId (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get sentiment count of interactions
    api_response = api_instance.get_sentiment(start_time, end_time, requester_id, client_token, interaction_type=interaction_type, additional_information=additional_information, association=association, category_id=category_id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AugmentedIntelligenceApi->get_sentiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| start time | 
 **end_time** | **int**| end time | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| Interaction Type &lt;br/&gt;1)Question&lt;br/&gt;2)Complaint&lt;br/&gt;3)Idea&lt;br/&gt;4)Blog&lt;br/&gt;5)Discussion | [optional] 
 **additional_information** | **str**| additional information | [optional] 
 **association** | **str**| association | [optional] 
 **category_id** | **int**| categoryId | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseSentimentAnalytics**](VerveResponseSentimentAnalytics.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_entity_sentiments**
> VerveResponseEntitySentimentList get_tag_entity_sentiments(tag_name, start_time, end_time, start, end, requester_id, client_token, sentiment_type=sentiment_type, additional_information=additional_information, association=association, interaction_type=interaction_type, category_id=category_id, access_token=access_token)

Get list of tag entity sentiment

Return the list of tag entity sentiments

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
api_instance = iengage_client.AugmentedIntelligenceApi()
tag_name = 'tag_name_example' # str | tag name
start_time = 789 # int | start time
end_time = 789 # int | end time
start = 56 # int | start
end = 56 # int | end
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
sentiment_type = 'sentiment_type_example' # str | Sentiment Type <br/>1)Positive<br/>2)Negative<br/>3)Neutral (optional)
additional_information = 'additional_information_example' # str | additional information (optional)
association = 'association_example' # str | association (optional)
interaction_type = 'interaction_type_example' # str | Interaction Type <br/>1)Question<br/>2)Complaint<br/>3)Idea<br/>4)Blog<br/>5)Discussion (optional)
category_id = 789 # int | categoryId (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of tag entity sentiment
    api_response = api_instance.get_tag_entity_sentiments(tag_name, start_time, end_time, start, end, requester_id, client_token, sentiment_type=sentiment_type, additional_information=additional_information, association=association, interaction_type=interaction_type, category_id=category_id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AugmentedIntelligenceApi->get_tag_entity_sentiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| tag name | 
 **start_time** | **int**| start time | 
 **end_time** | **int**| end time | 
 **start** | **int**| start | 
 **end** | **int**| end | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **sentiment_type** | **str**| Sentiment Type &lt;br/&gt;1)Positive&lt;br/&gt;2)Negative&lt;br/&gt;3)Neutral | [optional] 
 **additional_information** | **str**| additional information | [optional] 
 **association** | **str**| association | [optional] 
 **interaction_type** | **str**| Interaction Type &lt;br/&gt;1)Question&lt;br/&gt;2)Complaint&lt;br/&gt;3)Idea&lt;br/&gt;4)Blog&lt;br/&gt;5)Discussion | [optional] 
 **category_id** | **int**| categoryId | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseEntitySentimentList**](VerveResponseEntitySentimentList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sentiment**
> VerveResponseSentiment sentiment(text, client_token)

Analyzes the sentiment of the content

The response will be a Sentiment Weightage. -1 is most negative and +1 is most positive. 0 will be neutral

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
api_instance = iengage_client.AugmentedIntelligenceApi()
text = 'text_example' # str | Sentence whose sentiment is to be found out
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Analyzes the sentiment of the content
    api_response = api_instance.sentiment(text, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AugmentedIntelligenceApi->sentiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Sentence whose sentiment is to be found out | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseSentiment**](VerveResponseSentiment.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

