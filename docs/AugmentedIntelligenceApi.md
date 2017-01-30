# iengage-client.AugmentedIntelligenceApi

All URIs are relative to *https://api.iengage.io:8243/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_interaction**](AugmentedIntelligenceApi.md#get_interaction) | **GET** /machineLearning/interactionType | Get the type of interaction
[**get_popular_tag**](AugmentedIntelligenceApi.md#get_popular_tag) | **GET** /analytics/popular/tags | Get list of popular tag of interactions
[**get_sentiment**](AugmentedIntelligenceApi.md#get_sentiment) | **GET** /analytics/sentiments | Get sentiment count of interactions
[**get_tag_entity_sentiments**](AugmentedIntelligenceApi.md#get_tag_entity_sentiments) | **GET** /analytics/tag/entitySentiment | Get list of tag entity sentiment


# **get_interaction**
> VerveResponseNLCList get_interaction(text, logged_in_user_id, access_token, client_token)

Get the type of interaction

Classifies text to question, complaint or suggestion

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
api_instance = iengage-client.AugmentedIntelligenceApi()
text = 'text_example' # str | Text to be classified
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Get the type of interaction
    api_response = api_instance.get_interaction(text, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AugmentedIntelligenceApi->get_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Text to be classified | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseNLCList**](VerveResponseNLCList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_popular_tag**
> VerveResponseTagList get_popular_tag(start_time, end_time, start, end, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, sentiment_type=sentiment_type, additional_information=additional_information)

Get list of popular tag of interactions

Return the most popular tag of given interaction type

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
api_instance = iengage-client.AugmentedIntelligenceApi()
start_time = 789 # int | start time
end_time = 789 # int | end time
start = 56 # int | start
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | Interaction Type <br/>1)Question<br/>2)Complaint<br/>3)Idea<br/>4)Blog<br/>5)Discussion (optional)
sentiment_type = 'sentiment_type_example' # str | Sentiment Type <br/>1)Positive<br/>2)Negative<br/> 3)Neutral (optional)
additional_information = 'additional_information_example' # str | additional information (optional)

try: 
    # Get list of popular tag of interactions
    api_response = api_instance.get_popular_tag(start_time, end_time, start, end, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, sentiment_type=sentiment_type, additional_information=additional_information)
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
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| Interaction Type &lt;br/&gt;1)Question&lt;br/&gt;2)Complaint&lt;br/&gt;3)Idea&lt;br/&gt;4)Blog&lt;br/&gt;5)Discussion | [optional] 
 **sentiment_type** | **str**| Sentiment Type &lt;br/&gt;1)Positive&lt;br/&gt;2)Negative&lt;br/&gt; 3)Neutral | [optional] 
 **additional_information** | **str**| additional information | [optional] 

### Return type

[**VerveResponseTagList**](VerveResponseTagList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sentiment**
> VerveResponseSentimentAnalytics get_sentiment(start_time, end_time, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, additional_information=additional_information)

Get sentiment count of interactions

Returns the sum of the sentiment count of given interaction type

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
api_instance = iengage-client.AugmentedIntelligenceApi()
start_time = 789 # int | start time
end_time = 789 # int | end time
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
interaction_type = 'interaction_type_example' # str | Interaction Type <br/>1)Question<br/>2)Complaint<br/>3)Idea<br/>4)Blog<br/>5)Discussion (optional)
additional_information = 'additional_information_example' # str | additional information (optional)

try: 
    # Get sentiment count of interactions
    api_response = api_instance.get_sentiment(start_time, end_time, logged_in_user_id, access_token, client_token, interaction_type=interaction_type, additional_information=additional_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AugmentedIntelligenceApi->get_sentiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| start time | 
 **end_time** | **int**| end time | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **interaction_type** | **str**| Interaction Type &lt;br/&gt;1)Question&lt;br/&gt;2)Complaint&lt;br/&gt;3)Idea&lt;br/&gt;4)Blog&lt;br/&gt;5)Discussion | [optional] 
 **additional_information** | **str**| additional information | [optional] 

### Return type

[**VerveResponseSentimentAnalytics**](VerveResponseSentimentAnalytics.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_entity_sentiments**
> VerveResponseEntitySentimentList get_tag_entity_sentiments(tag_name, start_time, end_time, start, end, logged_in_user_id, access_token, client_token, sentiment_type=sentiment_type, additional_information=additional_information)

Get list of tag entity sentiment

Return the list of tag entity sentiments

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
api_instance = iengage-client.AugmentedIntelligenceApi()
tag_name = 'tag_name_example' # str | tag name
start_time = 789 # int | start time
end_time = 789 # int | end time
start = 56 # int | start
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
sentiment_type = 'sentiment_type_example' # str | Sentiment Type <br/>1)Positive<br/>2)Negative<br/>3)Neutral (optional)
additional_information = 'additional_information_example' # str | additional information (optional)

try: 
    # Get list of tag entity sentiment
    api_response = api_instance.get_tag_entity_sentiments(tag_name, start_time, end_time, start, end, logged_in_user_id, access_token, client_token, sentiment_type=sentiment_type, additional_information=additional_information)
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
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **sentiment_type** | **str**| Sentiment Type &lt;br/&gt;1)Positive&lt;br/&gt;2)Negative&lt;br/&gt;3)Neutral | [optional] 
 **additional_information** | **str**| additional information | [optional] 

### Return type

[**VerveResponseEntitySentimentList**](VerveResponseEntitySentimentList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

