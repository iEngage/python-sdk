# iengage_client.UserAuthenticationApi

All URIs are relative to *https://api.iengage.io:8243/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_notification_registered_id**](UserAuthenticationApi.md#add_notification_registered_id) | **POST** /devices | Add device token
[**add_user**](UserAuthenticationApi.md#add_user) | **POST** /users | Add/Register new user
[**authenticate**](UserAuthenticationApi.md#authenticate) | **GET** /authenticate | Authenticate User
[**change_password**](UserAuthenticationApi.md#change_password) | **PUT** /users/password | Change password
[**create_association**](UserAuthenticationApi.md#create_association) | **POST** /associations | Create association
[**delete_user**](UserAuthenticationApi.md#delete_user) | **DELETE** /users/{userId} | Delete user
[**get_associations**](UserAuthenticationApi.md#get_associations) | **GET** /associations | Get list of associations
[**logout**](UserAuthenticationApi.md#logout) | **GET** /logout | Logout


# **add_notification_registered_id**
> bool add_notification_registered_id(registered_id, type, client_token, requester_id=requester_id, access_token=access_token)

Add device token

Add device token to push notification from server

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.UserAuthenticationApi()
registered_id = 'registered_id_example' # str | Registered device token to be added
type = 'type_example' # str | Type of device android, ios
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address. (optional)
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Add device token
    api_response = api_instance.add_notification_registered_id(registered_id, type, client_token, requester_id=requester_id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserAuthenticationApi->add_notification_registered_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registered_id** | **str**| Registered device token to be added | 
 **type** | **str**| Type of device android, ios | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **requester_id** | **str**| requesterId can be user id OR email address. | [optional] 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

**bool**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user**
> VerveResponseUser add_user(screen_name, email_id, password, client_token, first_name=first_name, middle_name=middle_name, last_name=last_name, birth_day=birth_day, birth_month=birth_month, birth_year=birth_year, addition_information=addition_information)

Add/Register new user

Add/Register new user. Returns the user

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.UserAuthenticationApi()
screen_name = 'screen_name_example' # str | unique ID of user
email_id = 'email_id_example' # str | email ID
password = 'password_example' # str | password
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
first_name = 'first_name_example' # str | first name (optional)
middle_name = 'middle_name_example' # str | middle name (optional)
last_name = 'last_name_example' # str | last name (optional)
birth_day = 56 # int | birth day (optional)
birth_month = 56 # int | birth month (optional)
birth_year = 56 # int | birth year (optional)
addition_information = 'addition_information_example' # str | addition information (optional)

try: 
    # Add/Register new user
    api_response = api_instance.add_user(screen_name, email_id, password, client_token, first_name=first_name, middle_name=middle_name, last_name=last_name, birth_day=birth_day, birth_month=birth_month, birth_year=birth_year, addition_information=addition_information)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserAuthenticationApi->add_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screen_name** | **str**| unique ID of user | 
 **email_id** | **str**| email ID | 
 **password** | **str**| password | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **first_name** | **str**| first name | [optional] 
 **middle_name** | **str**| middle name | [optional] 
 **last_name** | **str**| last name | [optional] 
 **birth_day** | **int**| birth day | [optional] 
 **birth_month** | **int**| birth month | [optional] 
 **birth_year** | **int**| birth year | [optional] 
 **addition_information** | **str**| addition information | [optional] 

### Return type

[**VerveResponseUser**](VerveResponseUser.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate**
> User authenticate(user_name, password, client_token)

Authenticate User

Authenticate with username & password

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.UserAuthenticationApi()
user_name = 'user_name_example' # str | User name
password = 'password_example' # str | Password
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Authenticate User
    api_response = api_instance.authenticate(user_name, password, client_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserAuthenticationApi->authenticate: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| User name | 
 **password** | **str**| Password | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**User**](User.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> bool change_password(current_password, new_password, requester_id, client_token, access_token=access_token)

Change password

Allows the user to change password. Returns true if successful

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.UserAuthenticationApi()
current_password = 'current_password_example' # str | Current password
new_password = 'new_password_example' # str | New password
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Change password
    api_response = api_instance.change_password(current_password, new_password, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserAuthenticationApi->change_password: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **current_password** | **str**| Current password | 
 **new_password** | **str**| New password | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

**bool**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_association**
> VerveResponseAssociation create_association(name, requester_id, client_token, access_token=access_token)

Create association

Create association. Returns the association

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.UserAuthenticationApi()
name = 'name_example' # str | association name
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Create association
    api_response = api_instance.create_association(name, requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserAuthenticationApi->create_association: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| association name | 
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseAssociation**](VerveResponseAssociation.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> VerveResponseUser delete_user(user_id, client_token)

Delete user

Allows the user to delete user. Returns the deleted user

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.UserAuthenticationApi()
user_id = 789 # int | userId
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs

try: 
    # Delete user
    api_response = api_instance.delete_user(user_id, client_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserAuthenticationApi->delete_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 

### Return type

[**VerveResponseUser**](VerveResponseUser.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associations**
> VerveResponseAssociationList get_associations(requester_id, client_token, access_token=access_token)

Get list of associations

Return the list of association

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.UserAuthenticationApi()
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Get list of associations
    api_response = api_instance.get_associations(requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserAuthenticationApi->get_associations: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

[**VerveResponseAssociationList**](VerveResponseAssociationList.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> bool logout(requester_id, client_token, access_token=access_token)

Logout

Logout rest api session. Returns true if successful

### Example 
```python
import time
import iengage_client
from iengage_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
iengage_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = iengage_client.UserAuthenticationApi()
requester_id = 'requester_id_example' # str | requesterId can be user id OR email address.
client_token = 'client_token_example' # str | Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs
access_token = 'access_token_example' # str | Unique session token for user. To get access token user will have to authenticate (optional)

try: 
    # Logout
    api_response = api_instance.logout(requester_id, client_token, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserAuthenticationApi->logout: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requester_id** | **str**| requesterId can be user id OR email address. | 
 **client_token** | **str**| Use the Client Token. Please generate it from the Applications section under the Production &amp; Sandbox tabs | 
 **access_token** | **str**| Unique session token for user. To get access token user will have to authenticate | [optional] 

### Return type

**bool**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

