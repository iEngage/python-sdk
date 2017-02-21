# iengage_client.QuestionApi

All URIs are relative to *https://api.iengage.io:8243/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_answer**](QuestionApi.md#add_answer) | **POST** /questions/{questionId}/answers | Answer the specified question
[**add_question**](QuestionApi.md#add_question) | **POST** /questions | Share question without attachment
[**add_question_0**](QuestionApi.md#add_question_0) | **POST** /questions/attachment | Share question with attachment
[**create_question_category**](QuestionApi.md#create_question_category) | **POST** /questions/categories | Create question category
[**delete_answer**](QuestionApi.md#delete_answer) | **DELETE** /questions/answers/{answerId} | Delete answer
[**delete_question**](QuestionApi.md#delete_question) | **DELETE** /questions/{questionId} | Delete question
[**delete_question_category**](QuestionApi.md#delete_question_category) | **DELETE** /questions/categories/{categoryId} | Delete question category
[**dislike_answer**](QuestionApi.md#dislike_answer) | **POST** /questions/{questionId}/answers/{answerId}/dislike | Dislike answer
[**get_answers**](QuestionApi.md#get_answers) | **GET** /questions/{questionId}/answers | Get list of answers by questionId
[**get_friends_questions**](QuestionApi.md#get_friends_questions) | **GET** /questions/friends | Get list of questions shared by friends
[**get_question**](QuestionApi.md#get_question) | **GET** /questions/{questionId} | Get question by id
[**get_question_categories**](QuestionApi.md#get_question_categories) | **GET** /questions/categories | Get the list of question categories
[**get_questions_for_user**](QuestionApi.md#get_questions_for_user) | **GET** /questions | Get list of all questions visible to the user
[**get_recommend_question**](QuestionApi.md#get_recommend_question) | **GET** /questions/recommend | Get list of recommended questions
[**get_recommended_questions_from_db**](QuestionApi.md#get_recommended_questions_from_db) | **GET** /questions/{userId}/recommendedQuestions | Get list of recommended questions from DB
[**get_recommended_users_from_db**](QuestionApi.md#get_recommended_users_from_db) | **GET** /questions/{questionId}/recommendedUsers | Get list of recommended Users from DB
[**get_user_questions**](QuestionApi.md#get_user_questions) | **GET** /questions/{userId}/shared | Get list of questions shared by user
[**get_user_subscribed_question_categories**](QuestionApi.md#get_user_subscribed_question_categories) | **GET** /questions/categories/{userId}/subscribe | Get list of question categories subscribed by the user
[**get_user_subscribed_questions**](QuestionApi.md#get_user_subscribed_questions) | **GET** /questions/{userId}/subscribe | Get list of questions subscribed by user
[**like_answer**](QuestionApi.md#like_answer) | **POST** /questions/{questionId}/answers/{answerId}/like | Like answer
[**mark_as_an_answer**](QuestionApi.md#mark_as_an_answer) | **POST** /questions/{questionId}/answers/{answerId}/mark | Mark answer as a answer
[**search_questions**](QuestionApi.md#search_questions) | **GET** /questions/search | Get list of matching questions
[**subscribe_question**](QuestionApi.md#subscribe_question) | **POST** /questions/{questionId}/subscribe | Subscribe question
[**subscribe_question_category**](QuestionApi.md#subscribe_question_category) | **POST** /questions/categories/{categoryId}/subscribe | Subscribe question category
[**unmark_as_an_answer**](QuestionApi.md#unmark_as_an_answer) | **POST** /questions/{questionId}/answers/{answerId}/unmark | Unmark answer as a answer
[**unsubscribe_question**](QuestionApi.md#unsubscribe_question) | **POST** /questions/{questionId}/unsubscribe | Unsubscribe question
[**unsubscribe_question_category**](QuestionApi.md#unsubscribe_question_category) | **POST** /questions/categories/{categoryId}/unsubscribe | Unsubscribe question category
[**update_answer**](QuestionApi.md#update_answer) | **PUT** /questions/answers/{answerId} | Update answer
[**update_question**](QuestionApi.md#update_question) | **PUT** /questions/{questionId} | Update question
[**update_question_category**](QuestionApi.md#update_question_category) | **PUT** /questions/categories/{categoryId} | Update question category


# **add_answer**
> VerveResponseAnswer add_answer(question_id, answer, logged_in_user_id, access_token, client_token, fields=fields)

Answer the specified question

Allows the user to answer the question

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
answer = 'answer_example' # str | answer
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'answerId,answerDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/><b>A) Available values -</b><br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/>4)questionId<br/>5)answeringUser<br/>6)isMarkedAnswer<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to answerId,answerDescription,createdDate)

try: 
    # Answer the specified question
    api_response = api_instance.add_answer(question_id, answer, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->add_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
 **answer** | **str**| answer | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)questionId&lt;br/&gt;5)answeringUser&lt;br/&gt;6)isMarkedAnswer&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to answerId,answerDescription,createdDate]

### Return type

[**VerveResponseAnswer**](VerveResponseAnswer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_question**
> VerveResponseQuestion add_question(category_id, question_title, question_description, logged_in_user_id, access_token, client_token)

Share question without attachment

Allows the user to share question without attachment. Returns the question object

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
api_instance = iengage_client.QuestionApi()
category_id = 789 # int | categoryId
question_title = 'question_title_example' # str | Question Title
question_description = 'question_description_example' # str | Describe question
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Share question without attachment
    api_response = api_instance.add_question(category_id, question_title, question_description, logged_in_user_id, access_token, client_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->add_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **question_title** | **str**| Question Title | 
 **question_description** | **str**| Describe question | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseQuestion**](VerveResponseQuestion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_question_0**
> VerveResponseQuestion add_question_0(body, body2, body3, logged_in_user_id, access_token, client_token, body4=body4)

Share question with attachment

Allows the user to share question with attachment. Returns the question object

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
api_instance = iengage_client.QuestionApi()
body = 789 # int | categoryId
body2 = 'body_example' # str | questionTitle
body3 = 'body_example' # str | questionDescription
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
body4 = [iengage_client.Attachment()] # list[Attachment] |  (optional)

try: 
    # Share question with attachment
    api_response = api_instance.add_question_0(body, body2, body3, logged_in_user_id, access_token, client_token, body4=body4)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->add_question_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **int**| categoryId | 
 **body2** | **str**| questionTitle | 
 **body3** | **str**| questionDescription | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **body4** | [**list[Attachment]**](Attachment.md)|  | [optional] 

### Return type

[**VerveResponseQuestion**](VerveResponseQuestion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_question_category**
> VerveResponseQuestionCategory create_question_category(name, description, logged_in_user_id, access_token, client_token, organization_id=organization_id, fields=fields)

Create question category

Creates a question category. Returns the created question category

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
api_instance = iengage_client.QuestionApi()
name = 'name_example' # str | Name
description = 'description_example' # str | description
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
organization_id = 789 # int | OrganizationId (optional)
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Create question category
    api_response = api_instance.create_question_category(name, description, logged_in_user_id, access_token, client_token, organization_id=organization_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->create_question_category: %s\n" % e)
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
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseQuestionCategory**](VerveResponseQuestionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_answer**
> VerveResponseAnswer delete_answer(answer_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete answer

Allows the user to delete an answer. Returns the deleted answer

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
api_instance = iengage_client.QuestionApi()
answer_id = 789 # int | answerId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'answerId,answerDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/><b>A) Available values -</b><br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/>4)questionId<br/>5)answeringUser<br/>6)isMarkedAnswer<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to answerId,answerDescription,createdDate)

try: 
    # Delete answer
    api_response = api_instance.delete_answer(answer_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->delete_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **answer_id** | **int**| answerId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)questionId&lt;br/&gt;5)answeringUser&lt;br/&gt;6)isMarkedAnswer&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to answerId,answerDescription,createdDate]

### Return type

[**VerveResponseAnswer**](VerveResponseAnswer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_question**
> VerveResponseQuestion delete_question(question_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete question

Allows the user to delete a question. Returns the deleted answer

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Delete question
    api_response = api_instance.delete_question(question_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->delete_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestion**](VerveResponseQuestion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_question_category**
> VerveResponseQuestionCategory delete_question_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)

Delete question category

Allows the user to delete the question category. Returns the deleted question category

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
api_instance = iengage_client.QuestionApi()
category_id = 789 # int | categoryId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Delete question category
    api_response = api_instance.delete_question_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->delete_question_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseQuestionCategory**](VerveResponseQuestionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dislike_answer**
> VerveResponseAnswer dislike_answer(question_id, answer_id, logged_in_user_id, access_token, client_token, fields=fields)

Dislike answer

Allows the user to dislike the answer.

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
answer_id = 789 # int | answerId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'answerId,answerDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/><b>A) Available values -</b><br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/>4)questionId<br/>5)answeringUser<br/>6)isMarkedAnswer<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to answerId,answerDescription,createdDate)

try: 
    # Dislike answer
    api_response = api_instance.dislike_answer(question_id, answer_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->dislike_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
 **answer_id** | **int**| answerId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)questionId&lt;br/&gt;5)answeringUser&lt;br/&gt;6)isMarkedAnswer&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to answerId,answerDescription,createdDate]

### Return type

[**VerveResponseAnswer**](VerveResponseAnswer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_answers**
> VerveResponseAnswerList get_answers(question_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of answers by questionId

Returns the list of answers by questionId

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'answerId,answerDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/><b>A) Available values -</b><br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/>4)questionId<br/>5)answeringUser<br/>6)isMarkedAnswer<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to answerId,answerDescription,createdDate)

try: 
    # Get list of answers by questionId
    api_response = api_instance.get_answers(question_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_answers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)questionId&lt;br/&gt;5)answeringUser&lt;br/&gt;6)isMarkedAnswer&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to answerId,answerDescription,createdDate]

### Return type

[**VerveResponseAnswerList**](VerveResponseAnswerList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_friends_questions**
> VerveResponseQuestionList get_friends_questions(question_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)

Get list of questions shared by friends

Returns the list of questions shared by friends

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
api_instance = iengage_client.QuestionApi()
question_status = 'question_status_example' # str | Question status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Get list of questions shared by friends
    api_response = api_instance.get_friends_questions(question_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_friends_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_status** | **str**| Question status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestionList**](VerveResponseQuestionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question**
> VerveResponseQuestion get_question(question_id, logged_in_user_id, access_token, client_token, fields=fields)

Get question by id

Returns the question by id

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Get question by id
    api_response = api_instance.get_question(question_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestion**](VerveResponseQuestion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question_categories**
> VerveResponseQuestionCategoryList get_question_categories(start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get the list of question categories

Returns the list of question categories

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
api_instance = iengage_client.QuestionApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Get the list of question categories
    api_response = api_instance.get_question_categories(start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_question_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseQuestionCategoryList**](VerveResponseQuestionCategoryList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_questions_for_user**
> VerveResponseQuestionList get_questions_for_user(question_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)

Get list of all questions visible to the user

Returns the list of all questions visible to the user

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
api_instance = iengage_client.QuestionApi()
question_status = 'question_status_example' # str | Question status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Get list of all questions visible to the user
    api_response = api_instance.get_questions_for_user(question_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_questions_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_status** | **str**| Question status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestionList**](VerveResponseQuestionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommend_question**
> VerveResponseQuestionList get_recommend_question(start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of recommended questions

Returns the list of recommended questions

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
api_instance = iengage_client.QuestionApi()
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Get list of recommended questions
    api_response = api_instance.get_recommend_question(start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_recommend_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestionList**](VerveResponseQuestionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_questions_from_db**
> VerveResponseQuestionList get_recommended_questions_from_db(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of recommended questions from DB

Returns the list of recommended questions from DB

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
api_instance = iengage_client.QuestionApi()
user_id = 789 # int | userId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Get list of recommended questions from DB
    api_response = api_instance.get_recommended_questions_from_db(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_recommended_questions_from_db: %s\n" % e)
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
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestionList**](VerveResponseQuestionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_users_from_db**
> VerveResponseUserList get_recommended_users_from_db(question_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'userId,firstName,lastName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)profileImage<br/><b>A) Available values-</b><br/>1)userId<br/>2)firstName<br/>3)lastName<br/>4)emailId<br/>5)profileImage<br/>6)birthDate<br/>7)currentUserFollowing<br/>8)currentUserFriend<br/>9)equityScore (optional) (default to userId,firstName,lastName)

try: 
    # Get list of recommended Users from DB
    api_response = api_instance.get_recommended_users_from_db(question_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_recommended_users_from_db: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
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

# **get_user_questions**
> VerveResponseQuestionList get_user_questions(user_id, question_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)

Get list of questions shared by user

Returns the list of questions shared by specific user

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
api_instance = iengage_client.QuestionApi()
user_id = 789 # int | userId
question_status = 'question_status_example' # str | Question status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Get list of questions shared by user
    api_response = api_instance.get_user_questions(user_id, question_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_user_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **question_status** | **str**| Question status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestionList**](VerveResponseQuestionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscribed_question_categories**
> VerveResponseQuestionCategoryList get_user_subscribed_question_categories(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of question categories subscribed by the user

Returns the list of question categories subscribed by the user

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
api_instance = iengage_client.QuestionApi()
user_id = 789 # int | userId
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Get list of question categories subscribed by the user
    api_response = api_instance.get_user_subscribed_question_categories(user_id, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_user_subscribed_question_categories: %s\n" % e)
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
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseQuestionCategoryList**](VerveResponseQuestionCategoryList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscribed_questions**
> VerveResponseQuestionList get_user_subscribed_questions(user_id, question_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)

Get list of questions subscribed by user

Returns the list of questions subscribed by specific user

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
api_instance = iengage_client.QuestionApi()
user_id = 789 # int | userId
question_status = 'question_status_example' # str | Question status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
category_id = 789 # int | categoryId (optional)
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Get list of questions subscribed by user
    api_response = api_instance.get_user_subscribed_questions(user_id, question_status, start, end, logged_in_user_id, access_token, client_token, category_id=category_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_user_subscribed_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **question_status** | **str**| Question status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **category_id** | **int**| categoryId | [optional] 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestionList**](VerveResponseQuestionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **like_answer**
> VerveResponseAnswer like_answer(question_id, answer_id, logged_in_user_id, access_token, client_token, fields=fields)

Like answer

Allows the user to like the answer.

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
answer_id = 789 # int | answerId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'answerId,answerDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/><b>A) Available values -</b><br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/>4)questionId<br/>5)answeringUser<br/>6)isMarkedAnswer<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to answerId,answerDescription,createdDate)

try: 
    # Like answer
    api_response = api_instance.like_answer(question_id, answer_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->like_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
 **answer_id** | **int**| answerId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)questionId&lt;br/&gt;5)answeringUser&lt;br/&gt;6)isMarkedAnswer&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to answerId,answerDescription,createdDate]

### Return type

[**VerveResponseAnswer**](VerveResponseAnswer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_as_an_answer**
> VerveResponseAnswer mark_as_an_answer(question_id, answer_id, logged_in_user_id, access_token, client_token, fields=fields)

Mark answer as a answer

Marks the answer as accepted. This means the user is satisfied with the answer & then the question will go into closed state

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
answer_id = 789 # int | answerId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'answerId,answerDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/><b>A) Available values -</b><br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/>4)questionId<br/>5)answeringUser<br/>6)isMarkedAnswer<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to answerId,answerDescription,createdDate)

try: 
    # Mark answer as a answer
    api_response = api_instance.mark_as_an_answer(question_id, answer_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->mark_as_an_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
 **answer_id** | **int**| answerId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)questionId&lt;br/&gt;5)answeringUser&lt;br/&gt;6)isMarkedAnswer&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to answerId,answerDescription,createdDate]

### Return type

[**VerveResponseAnswer**](VerveResponseAnswer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_questions**
> VerveResponseQuestionList search_questions(search_text, question_status, start, end, logged_in_user_id, access_token, client_token, fields=fields)

Get list of matching questions

Returns the list of matching questions

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
api_instance = iengage_client.QuestionApi()
search_text = 'search_text_example' # str | Search Text, keywords to search
question_status = 'question_status_example' # str | Question status <br/> 1) ALL <br/> 2)  UNREPLIED <br/> 3)  REPLIED <br/> 4)  CLOSED
start = 56 # int | start, initial value start from 0
end = 56 # int | end
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Get list of matching questions
    api_response = api_instance.search_questions(search_text, question_status, start, end, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->search_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Search Text, keywords to search | 
 **question_status** | **str**| Question status &lt;br/&gt; 1) ALL &lt;br/&gt; 2)  UNREPLIED &lt;br/&gt; 3)  REPLIED &lt;br/&gt; 4)  CLOSED | 
 **start** | **int**| start, initial value start from 0 | 
 **end** | **int**| end | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestionList**](VerveResponseQuestionList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_question**
> VerveResponseQuestion subscribe_question(question_id, logged_in_user_id, access_token, client_token, fields=fields)

Subscribe question

Allows the user to subscribe a question

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Subscribe question
    api_response = api_instance.subscribe_question(question_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->subscribe_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestion**](VerveResponseQuestion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_question_category**
> VerveResponseQuestionCategory subscribe_question_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)

Subscribe question category

Returns the subscribed question category

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
api_instance = iengage_client.QuestionApi()
category_id = 789 # int | categoryId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Subscribe question category
    api_response = api_instance.subscribe_question_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->subscribe_question_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseQuestionCategory**](VerveResponseQuestionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-www-form-urlencoded

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmark_as_an_answer**
> VerveResponseAnswer unmark_as_an_answer(question_id, answer_id, logged_in_user_id, access_token, client_token, fields=fields)

Unmark answer as a answer

Unmarks the answer. This will remove the marked answer.

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
answer_id = 789 # int | answerId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'answerId,answerDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/><b>A) Available values -</b><br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/>4)questionId<br/>5)answeringUser<br/>6)isMarkedAnswer<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to answerId,answerDescription,createdDate)

try: 
    # Unmark answer as a answer
    api_response = api_instance.unmark_as_an_answer(question_id, answer_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->unmark_as_an_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
 **answer_id** | **int**| answerId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)questionId&lt;br/&gt;5)answeringUser&lt;br/&gt;6)isMarkedAnswer&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to answerId,answerDescription,createdDate]

### Return type

[**VerveResponseAnswer**](VerveResponseAnswer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_question**
> VerveResponseQuestion unsubscribe_question(question_id, logged_in_user_id, access_token, client_token, fields=fields)

Unsubscribe question

Allows the user to unsubscribe a question

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Unsubscribe question
    api_response = api_instance.unsubscribe_question(question_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->unsubscribe_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestion**](VerveResponseQuestion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_question_category**
> VerveResponseQuestionCategory unsubscribe_question_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)

Unsubscribe question category

Returns the unsubscribed question category

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
api_instance = iengage_client.QuestionApi()
category_id = 789 # int | categoryId
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Unsubscribe question category
    api_response = api_instance.unsubscribe_question_category(category_id, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->unsubscribe_question_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseQuestionCategory**](VerveResponseQuestionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_answer**
> VerveResponseAnswer update_answer(answer_id, answer, logged_in_user_id, access_token, client_token, fields=fields)

Update answer

Allows the user to update an answer. Returns the updated answer

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
api_instance = iengage_client.QuestionApi()
answer_id = 789 # int | answerId
answer = 'answer_example' # str | answer
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'answerId,answerDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/><b>A) Available values -</b><br/>1)answerId<br/>2)answerDescription<br/>3)createdDate<br/>4)questionId<br/>5)answeringUser<br/>6)isMarkedAnswer<br/>7)noOfLikes<br/>8)noOfDislikes<br/>9)replyCount<br/>10)isLiked<br/>11)isDisliked (optional) (default to answerId,answerDescription,createdDate)

try: 
    # Update answer
    api_response = api_instance.update_answer(answer_id, answer, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->update_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **answer_id** | **int**| answerId | 
 **answer** | **str**| answer | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt;&lt;br/&gt;1)answerId&lt;br/&gt;2)answerDescription&lt;br/&gt;3)createdDate&lt;br/&gt;4)questionId&lt;br/&gt;5)answeringUser&lt;br/&gt;6)isMarkedAnswer&lt;br/&gt;7)noOfLikes&lt;br/&gt;8)noOfDislikes&lt;br/&gt;9)replyCount&lt;br/&gt;10)isLiked&lt;br/&gt;11)isDisliked | [optional] [default to answerId,answerDescription,createdDate]

### Return type

[**VerveResponseAnswer**](VerveResponseAnswer.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_question**
> VerveResponseQuestion update_question(question_id, question_title, question_description, logged_in_user_id, access_token, client_token, fields=fields)

Update question

Allows the user to update question. Returns the updated question

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
api_instance = iengage_client.QuestionApi()
question_id = 789 # int | questionId
question_title = 'question_title_example' # str | Question Title
question_description = 'question_description_example' # str | Describe Question
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'questionId,questionTitle,questionDescription,createdDate' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)createdDate<br/><b>A) Available values-</b><br/>1)questionId<br/>2)questionTitle<br/>3)questionDescription<br/>4)issuer<br/>5)noOfAnswers<br/>6)isClosed<br/>7)createdDate<br/>8)lastUpdatedDate<br/>9)videoId<br/>10)fileURL<br/>11)isSubscribed<br/>12)sentiment</br>13)entity (optional) (default to questionId,questionTitle,questionDescription,createdDate)

try: 
    # Update question
    api_response = api_instance.update_question(question_id, question_title, question_description, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->update_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| questionId | 
 **question_title** | **str**| Question Title | 
 **question_description** | **str**| Describe Question | 
 **logged_in_user_id** | **str**| User id of logged / authenticated user | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)createdDate&lt;br/&gt;&lt;b&gt;A) Available values-&lt;/b&gt;&lt;br/&gt;1)questionId&lt;br/&gt;2)questionTitle&lt;br/&gt;3)questionDescription&lt;br/&gt;4)issuer&lt;br/&gt;5)noOfAnswers&lt;br/&gt;6)isClosed&lt;br/&gt;7)createdDate&lt;br/&gt;8)lastUpdatedDate&lt;br/&gt;9)videoId&lt;br/&gt;10)fileURL&lt;br/&gt;11)isSubscribed&lt;br/&gt;12)sentiment&lt;/br&gt;13)entity | [optional] [default to questionId,questionTitle,questionDescription,createdDate]

### Return type

[**VerveResponseQuestion**](VerveResponseQuestion.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_question_category**
> VerveResponseQuestionCategory update_question_category(category_id, category_name, category_description, logged_in_user_id, access_token, client_token, fields=fields)

Update question category

Allows the user to update the question category. Returns the updated question category

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
api_instance = iengage_client.QuestionApi()
category_id = 789 # int | categoryId
category_name = 'category_name_example' # str | Category Name
category_description = 'category_description_example' # str | Describe category
logged_in_user_id = 'logged_in_user_id_example' # str | User id of logged / authenticated user
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
fields = 'categoryId,categoryName' # str | Filter fields in result list<br/> <b>A) Default values -</b> <br/>1)categoryId<br/>2)categoryName<br/><b>A) Available values -</b> <br/>1)categoryId<br/>2)categoryName<br/>3)categoryDescription<br/>4)createdDate<br/>5)isSubscribed (optional) (default to categoryId,categoryName)

try: 
    # Update question category
    api_response = api_instance.update_question_category(category_id, category_name, category_description, logged_in_user_id, access_token, client_token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->update_question_category: %s\n" % e)
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
 **fields** | **str**| Filter fields in result list&lt;br/&gt; &lt;b&gt;A) Default values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;&lt;b&gt;A) Available values -&lt;/b&gt; &lt;br/&gt;1)categoryId&lt;br/&gt;2)categoryName&lt;br/&gt;3)categoryDescription&lt;br/&gt;4)createdDate&lt;br/&gt;5)isSubscribed | [optional] [default to categoryId,categoryName]

### Return type

[**VerveResponseQuestionCategory**](VerveResponseQuestionCategory.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

