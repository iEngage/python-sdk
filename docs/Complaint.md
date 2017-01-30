# Complaint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complaint_id** | **int** |  | [optional] 
**complaint_title** | **str** |  | [optional] 
**complaint_description** | **str** |  | [optional] 
**issuer** | [**User**](User.md) |  | [optional] 
**no_of_solutions** | **int** |  | [optional] 
**is_closed** | **bool** |  | [optional] [default to False]
**created_date** | **datetime** |  | [optional] 
**last_updated_date** | **datetime** |  | [optional] 
**video_id** | **str** |  | [optional] 
**file_url** | **str** |  | [optional] 
**file_entity_name** | **str** |  | [optional] 
**is_subscribed** | **bool** |  | [optional] [default to False]
**sentiment** | **str** |  | [optional] 
**sentiment_details** | [**Sentiment**](Sentiment.md) |  | [optional] 
**sentiment_weightage** | **float** |  | [optional] 
**entity** | [**list[NER]**](NER.md) |  | [optional] 
**attachment_list** | [**list[Multimedia]**](Multimedia.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


