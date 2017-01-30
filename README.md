# iEngage.io python-SDK (Beta)
This API enables Intelligent Engagement for your Business. iEngage is a platform that combines process, augmented intelligence and rewards to help you intelligently engage customers.

- API version: 1.0
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import iengage-client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import iengage-client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
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

## Documentation for API Endpoints

All URIs are relative to *https://api.iengage.io:8243/api/1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AugmentedIntelligenceApi* | [**get_interaction**](docs/AugmentedIntelligenceApi.md#get_interaction) | **GET** /machineLearning/interactionType | Get the type of interaction
*AugmentedIntelligenceApi* | [**get_popular_tag**](docs/AugmentedIntelligenceApi.md#get_popular_tag) | **GET** /analytics/popular/tags | Get list of popular tag of interactions
*AugmentedIntelligenceApi* | [**get_sentiment**](docs/AugmentedIntelligenceApi.md#get_sentiment) | **GET** /analytics/sentiments | Get sentiment count of interactions
*AugmentedIntelligenceApi* | [**get_tag_entity_sentiments**](docs/AugmentedIntelligenceApi.md#get_tag_entity_sentiments) | **GET** /analytics/tag/entitySentiment | Get list of tag entity sentiment
*BPMApi* | [**assign_wf_task**](docs/BPMApi.md#assign_wf_task) | **POST** /bpm/tasks/{taskId}/assign | Assign task
*BPMApi* | [**complete_wf_task**](docs/BPMApi.md#complete_wf_task) | **POST** /bpm/tasks/{taskId}/complete | Complete task
*BPMApi* | [**get_bpm_tasks**](docs/BPMApi.md#get_bpm_tasks) | **GET** /bpm/tasks/{taskId} | Get task by task id
*BPMApi* | [**get_search_task**](docs/BPMApi.md#get_search_task) | **GET** /bpm/{userId}/tasks/name | Get list of BPM task assigned to user
*BPMApi* | [**get_tasks_by_entity**](docs/BPMApi.md#get_tasks_by_entity) | **GET** /bpm/{userId}/tasks/{entityId} | Get list of BPM task assigned to user
*BPMApi* | [**get_user_bpm_tasks**](docs/BPMApi.md#get_user_bpm_tasks) | **GET** /bpm/{userId}/tasks | Get list of BPM task assigned to user
*BPMApi* | [**get_user_roles_bpm_tasks**](docs/BPMApi.md#get_user_roles_bpm_tasks) | **GET** /bpm/{userId}/roles/tasks | Get list of BPM task assigned to user roles
*CollaborationApi* | [**add_comment_blog**](docs/CollaborationApi.md#add_comment_blog) | **POST** /collaborations/blogs/{blogId}/comments | Comment on posted blog
*CollaborationApi* | [**add_comment_discussion**](docs/CollaborationApi.md#add_comment_discussion) | **POST** /collaborations/discussions/{discussionId}/comments | Comment on discussion
*CollaborationApi* | [**delete_blog**](docs/CollaborationApi.md#delete_blog) | **DELETE** /collaborations/blogs/{blogId} | Delete blog
*CollaborationApi* | [**delete_blog_comment**](docs/CollaborationApi.md#delete_blog_comment) | **DELETE** /collaborations/blogs/comments/{commentId} | Delete blog comment
*CollaborationApi* | [**delete_discussion**](docs/CollaborationApi.md#delete_discussion) | **DELETE** /collaborations/discussions/{discussionId} | Delete discussion
*CollaborationApi* | [**delete_discussion_comment**](docs/CollaborationApi.md#delete_discussion_comment) | **DELETE** /collaborations/discussions/comments/{commentId} | Delete discussion comment
*CollaborationApi* | [**get_blog_comments**](docs/CollaborationApi.md#get_blog_comments) | **GET** /collaborations/blogs/{blogId}/comments | Get list of comments on blog
*CollaborationApi* | [**get_blogs**](docs/CollaborationApi.md#get_blogs) | **GET** /collaborations/blogs | Get list of blogs
*CollaborationApi* | [**get_discussion_comments**](docs/CollaborationApi.md#get_discussion_comments) | **GET** /collaborations/discussions/{discussionId}/comments | Get list of comments on discussion
*CollaborationApi* | [**get_discussions**](docs/CollaborationApi.md#get_discussions) | **GET** /collaborations/discussions | Get list of discussions
*CollaborationApi* | [**get_user_subscribed_blogs**](docs/CollaborationApi.md#get_user_subscribed_blogs) | **GET** /collaborations/blogs/{userId}/subscribe | Get list of blogs subscribed by user
*CollaborationApi* | [**get_user_subscribed_discussions**](docs/CollaborationApi.md#get_user_subscribed_discussions) | **GET** /collaborations/discussions/{userId}/subscribe | Get list of discussions subscribed by user
*CollaborationApi* | [**post_blog**](docs/CollaborationApi.md#post_blog) | **POST** /collaborations/blogs | Post blog
*CollaborationApi* | [**start_discussion**](docs/CollaborationApi.md#start_discussion) | **POST** /collaborations/discussions | Start discussion
*CollaborationApi* | [**subscribe_blog**](docs/CollaborationApi.md#subscribe_blog) | **POST** /collaborations/blogs/{blogId}/subscribe | Subscribe blog
*CollaborationApi* | [**subscribe_discussion**](docs/CollaborationApi.md#subscribe_discussion) | **POST** /collaborations/discussions/{discussionId}/subscribe | Subscribe discussion
*CollaborationApi* | [**unsubscribe_blog**](docs/CollaborationApi.md#unsubscribe_blog) | **POST** /collaborations/blogs/{blogId}/unsubscribe | Unsubscribe blog
*CollaborationApi* | [**unsubscribe_discussion**](docs/CollaborationApi.md#unsubscribe_discussion) | **POST** /collaborations/discussions/{discussionId}/unsubscribe | Unsubscribe discussion
*CollaborationApi* | [**update_blog**](docs/CollaborationApi.md#update_blog) | **PUT** /collaborations/blogs/{blogId} | Update blog
*CollaborationApi* | [**update_blog_comment**](docs/CollaborationApi.md#update_blog_comment) | **PUT** /collaborations/blogs/comments/{commentId} | Update blog comment
*CollaborationApi* | [**update_discussion**](docs/CollaborationApi.md#update_discussion) | **PUT** /collaborations/discussions/{discussionId} | Update discussion
*CollaborationApi* | [**update_discussion_comment**](docs/CollaborationApi.md#update_discussion_comment) | **PUT** /collaborations/discussions/comments/{commentId} | Update discussion comment
*ComplaintApi* | [**add_complaint**](docs/ComplaintApi.md#add_complaint) | **POST** /complaints | Share complaint without attachment
*ComplaintApi* | [**add_complaint_0**](docs/ComplaintApi.md#add_complaint_0) | **POST** /complaints/attachment | Share complaint with attachment
*ComplaintApi* | [**add_solution**](docs/ComplaintApi.md#add_solution) | **POST** /complaints/{complaintId}/solutions | Share solution on complaint
*ComplaintApi* | [**create_complaint_category**](docs/ComplaintApi.md#create_complaint_category) | **POST** /complaints/categories | Create complaint category
*ComplaintApi* | [**delete_complaint**](docs/ComplaintApi.md#delete_complaint) | **DELETE** /complaints/{complaintId} | Delete complaint
*ComplaintApi* | [**delete_complaint_category**](docs/ComplaintApi.md#delete_complaint_category) | **DELETE** /complaints/categories/{categoryId} | Delete complaint cotegory
*ComplaintApi* | [**delete_solution**](docs/ComplaintApi.md#delete_solution) | **DELETE** /complaints/solutions/{solutionId} | Delete solution
*ComplaintApi* | [**dislike_solution**](docs/ComplaintApi.md#dislike_solution) | **POST** /complaints/{complaintId}/solutions/{solutionId}/dislike | Dislike Solution
*ComplaintApi* | [**get_complaint**](docs/ComplaintApi.md#get_complaint) | **GET** /complaints/{complaintId} | Get complaint by id
*ComplaintApi* | [**get_complaint_categories**](docs/ComplaintApi.md#get_complaint_categories) | **GET** /complaints/categories | Get list of complaint category
*ComplaintApi* | [**get_complaints_for_user**](docs/ComplaintApi.md#get_complaints_for_user) | **GET** /complaints | Get list of all complaint visible for user
*ComplaintApi* | [**get_friends_complaints**](docs/ComplaintApi.md#get_friends_complaints) | **GET** /complaints/friends | Get list of complaints shared by your friends
*ComplaintApi* | [**get_recommend_complaint**](docs/ComplaintApi.md#get_recommend_complaint) | **GET** /complaints/recommend | Get list of recommended complaints
*ComplaintApi* | [**get_recommended_complaints_from_db**](docs/ComplaintApi.md#get_recommended_complaints_from_db) | **GET** /complaints/{userId}/recommendedComplaints | Get list of recommended complaints from DB
*ComplaintApi* | [**get_recommended_users_from_db**](docs/ComplaintApi.md#get_recommended_users_from_db) | **GET** /complaints/{complaintId}/recommendedUsers | Get list of recommended Users from DB
*ComplaintApi* | [**get_solutions**](docs/ComplaintApi.md#get_solutions) | **GET** /complaints/{complaintId}/solutions | Get list of solutions by ComplaintId
*ComplaintApi* | [**get_user_complaints**](docs/ComplaintApi.md#get_user_complaints) | **GET** /complaints/{userId}/shared | Get list of complaints shared by user
*ComplaintApi* | [**get_user_subscribed_complaint_categories**](docs/ComplaintApi.md#get_user_subscribed_complaint_categories) | **GET** /complaints/categories/{userId}/subscribe | Get list of Complaint categories subscribed by user
*ComplaintApi* | [**get_user_subscribed_complaints**](docs/ComplaintApi.md#get_user_subscribed_complaints) | **GET** /complaints/{userId}/subscribe | Get list of complaints subscribed by user
*ComplaintApi* | [**like_solution**](docs/ComplaintApi.md#like_solution) | **POST** /complaints/{complaintId}/solutions/{solutionId}/like | Like solution
*ComplaintApi* | [**mark_as_an_solution**](docs/ComplaintApi.md#mark_as_an_solution) | **POST** /complaints/{complaintId}/solutions/{solutionId}/mark | Mark solution as a solution
*ComplaintApi* | [**search_complaints**](docs/ComplaintApi.md#search_complaints) | **GET** /complaints/search | Get list of complaints by search
*ComplaintApi* | [**subscribe_complaint**](docs/ComplaintApi.md#subscribe_complaint) | **POST** /complaints/{complaintId}/subscribe | Subscribe complaint
*ComplaintApi* | [**subscribe_complaint_category**](docs/ComplaintApi.md#subscribe_complaint_category) | **POST** /complaints/categories/{categoryId}/subscribe | Subscribe complaint category
*ComplaintApi* | [**unmark_as_an_solution**](docs/ComplaintApi.md#unmark_as_an_solution) | **POST** /complaints/{complaintId}/solutions/{solutionId}/unmark | Unmark solution as a solution
*ComplaintApi* | [**unsubscribe_complaint**](docs/ComplaintApi.md#unsubscribe_complaint) | **POST** /complaints/{complaintId}/unsubscribe | Unsubscribe Complaint
*ComplaintApi* | [**unsubscribe_complaint_category**](docs/ComplaintApi.md#unsubscribe_complaint_category) | **POST** /complaints/categories/{categoryId}/unsubscribe | Unsubscribe complaint category
*ComplaintApi* | [**update_complaint**](docs/ComplaintApi.md#update_complaint) | **PUT** /complaints/{complaintId} | Update complaint
*ComplaintApi* | [**update_complaint_category**](docs/ComplaintApi.md#update_complaint_category) | **PUT** /complaints/categories/{categoryId} | Update complaint category
*ComplaintApi* | [**update_solution**](docs/ComplaintApi.md#update_solution) | **PUT** /complaints/solutions/{solutionId} | Update solution
*GroupApi* | [**create_group**](docs/GroupApi.md#create_group) | **POST** /groups | Create group
*GroupApi* | [**delete_group**](docs/GroupApi.md#delete_group) | **DELETE** /groups/{groupId} | Delete group
*GroupApi* | [**follow_group**](docs/GroupApi.md#follow_group) | **POST** /groups/{groupId}/follow | Follow group
*GroupApi* | [**get_group_followers**](docs/GroupApi.md#get_group_followers) | **GET** /groups/{groupId}/followers | Get the list of followers for the group
*GroupApi* | [**get_group_ideas**](docs/GroupApi.md#get_group_ideas) | **GET** /groups/{groupId}/ideas | Get list of all ideas in a group
*GroupApi* | [**get_groups**](docs/GroupApi.md#get_groups) | **GET** /groups | Get the list of groups visible for user
*GroupApi* | [**get_recommendation_group**](docs/GroupApi.md#get_recommendation_group) | **GET** /groups/recommend | Get list of recommended groups
*GroupApi* | [**get_user_following_groups**](docs/GroupApi.md#get_user_following_groups) | **GET** /groups/{userId}/following | Get list of groups that a user is following
*GroupApi* | [**search_groups**](docs/GroupApi.md#search_groups) | **GET** /groups/search | Get list of matching groups
*GroupApi* | [**unfollow_group**](docs/GroupApi.md#unfollow_group) | **POST** /groups/{groupId}/unfollow | Unfollow group
*GroupApi* | [**update_group**](docs/GroupApi.md#update_group) | **PUT** /groups/{groupId} | Update group
*IdeaApi* | [**delete_comment**](docs/IdeaApi.md#delete_comment) | **DELETE** /ideas/comments/{commentId} | Delete comment
*IdeaApi* | [**delete_idea**](docs/IdeaApi.md#delete_idea) | **DELETE** /ideas/{ideaId} | Delete idea
*IdeaApi* | [**follow_idea**](docs/IdeaApi.md#follow_idea) | **POST** /ideas/{ideaId}/follow | Follow idea
*IdeaApi* | [**get_all_ideas**](docs/IdeaApi.md#get_all_ideas) | **GET** /ideas | Get list of Ideas
*IdeaApi* | [**get_following_ideas**](docs/IdeaApi.md#get_following_ideas) | **GET** /ideas/{userId}/following | Get list of ideas that users are following
*IdeaApi* | [**get_group_ideas**](docs/IdeaApi.md#get_group_ideas) | **GET** /ideas/getGroupIdeas | Get list of ideas in group
*IdeaApi* | [**get_idea**](docs/IdeaApi.md#get_idea) | **GET** /ideas/{ideaId} | Get idea by id
*IdeaApi* | [**get_idea_comment**](docs/IdeaApi.md#get_idea_comment) | **GET** /ideas/{ideaId}/comments | Get list of comments on idea
*IdeaApi* | [**get_idea_followers**](docs/IdeaApi.md#get_idea_followers) | **GET** /ideas/{ideaId}/followers | Get list of followers for this idea
*IdeaApi* | [**get_idea_rating_parameters**](docs/IdeaApi.md#get_idea_rating_parameters) | **GET** /ideas/getIdeaRatingParameters | Get rating parameters of idea by user
*IdeaApi* | [**get_idea_ratings**](docs/IdeaApi.md#get_idea_ratings) | **GET** /ideas/getIdeaUserRating | Get list of ideas that are rated by user 
*IdeaApi* | [**get_recommend_ideas**](docs/IdeaApi.md#get_recommend_ideas) | **GET** /ideas/recommend | Get the list of recommended ideas
*IdeaApi* | [**get_top_ideas**](docs/IdeaApi.md#get_top_ideas) | **GET** /ideas/top | Get the list of top ideas
*IdeaApi* | [**get_user_ideas**](docs/IdeaApi.md#get_user_ideas) | **GET** /ideas/{userId}/shared | Get list of ideas shared by user
*IdeaApi* | [**get_user_rate_ideas**](docs/IdeaApi.md#get_user_rate_ideas) | **GET** /ideas/{userId}/rated | Get list of ideas rated by user
*IdeaApi* | [**rate_idea**](docs/IdeaApi.md#rate_idea) | **POST** /ideas/rateIdea | Rate an idea
*IdeaApi* | [**rate_idea_0**](docs/IdeaApi.md#rate_idea_0) | **GET** /ideas/rateIdeaByParameter | Give rating on idea
*IdeaApi* | [**search_ideas**](docs/IdeaApi.md#search_ideas) | **GET** /ideas/search | Get list of matching ideas
*IdeaApi* | [**share_form_idea**](docs/IdeaApi.md#share_form_idea) | **POST** /ideas/attachment | Share Idea with attachments
*IdeaApi* | [**share_idea**](docs/IdeaApi.md#share_idea) | **POST** /ideas | Share idea  
*IdeaApi* | [**share_idea_comment**](docs/IdeaApi.md#share_idea_comment) | **POST** /ideas/{ideaId}/comments | Comment on shared idea
*IdeaApi* | [**unfollow_idea**](docs/IdeaApi.md#unfollow_idea) | **POST** /ideas/{ideaId}/unfollow | Unfollow idea
*IdeaApi* | [**update_commet**](docs/IdeaApi.md#update_commet) | **PUT** /ideas/comments/{commentId} | Update comment
*IdeaApi* | [**update_idea**](docs/IdeaApi.md#update_idea) | **PUT** /ideas/{ideaId} | Update idea
*InteractionApi* | [**add_interaction**](docs/InteractionApi.md#add_interaction) | **POST** /interactions | Share interaction without attachment
*InteractionApi* | [**add_interaction_0**](docs/InteractionApi.md#add_interaction_0) | **POST** /interactions/attachment | Share interaction with attachment
*InteractionApi* | [**add_response**](docs/InteractionApi.md#add_response) | **POST** /interactions/{interactionId}/responses | Response the specified interaction
*InteractionApi* | [**create_interaction_category**](docs/InteractionApi.md#create_interaction_category) | **POST** /interactions/categories | Create interaction category
*InteractionApi* | [**delete_interaction**](docs/InteractionApi.md#delete_interaction) | **DELETE** /interactions/{interactionId} | Delete interaction
*InteractionApi* | [**delete_interaction_category**](docs/InteractionApi.md#delete_interaction_category) | **DELETE** /interactions/categories/{categoryId} | Delete interaction category
*InteractionApi* | [**delete_response**](docs/InteractionApi.md#delete_response) | **DELETE** /interactions/responses/{responseId} | Delete response
*InteractionApi* | [**dislike_response**](docs/InteractionApi.md#dislike_response) | **POST** /interactions/{interactionId}/responses/{responseId}/dislike | Dislike response
*InteractionApi* | [**get_friends_interactions**](docs/InteractionApi.md#get_friends_interactions) | **GET** /interactions/friends | Get list of interactions shared by friends
*InteractionApi* | [**get_interaction**](docs/InteractionApi.md#get_interaction) | **GET** /interactions/{interactionId} | Get interaction by id
*InteractionApi* | [**get_interaction_categories**](docs/InteractionApi.md#get_interaction_categories) | **GET** /interactions/categories | Get the list of interaction categories
*InteractionApi* | [**get_interactions_for_user**](docs/InteractionApi.md#get_interactions_for_user) | **GET** /interactions | Get list of all interactions visible to the user
*InteractionApi* | [**get_recommend_interactions**](docs/InteractionApi.md#get_recommend_interactions) | **GET** /interactions/recommend | Get list of recommended interactions
*InteractionApi* | [**get_recommended_interactins_from_db**](docs/InteractionApi.md#get_recommended_interactins_from_db) | **GET** /interactions/{userId}/recommendedInteractions | Get list of recommended interactions from DB
*InteractionApi* | [**get_recommended_users_from_db**](docs/InteractionApi.md#get_recommended_users_from_db) | **GET** /interactions/{interactionId}/recommendedUsers | Get list of recommended Users from DB
*InteractionApi* | [**get_responses**](docs/InteractionApi.md#get_responses) | **GET** /interactions/{interactionId}/responses | Get list of responses by interactionId
*InteractionApi* | [**get_user_interactions**](docs/InteractionApi.md#get_user_interactions) | **GET** /interactions/{userId}/shared | Get list of interactions shared by user
*InteractionApi* | [**get_user_subscribed_interaction_categories**](docs/InteractionApi.md#get_user_subscribed_interaction_categories) | **GET** /interactions/categories/{userId}/subscribe | Get list of interaction categories subscribed by the user
*InteractionApi* | [**get_user_subscribed_interactions**](docs/InteractionApi.md#get_user_subscribed_interactions) | **GET** /interactions/{userId}/subscribe | Get list of interactions subscribed by user
*InteractionApi* | [**like_response**](docs/InteractionApi.md#like_response) | **POST** /interactions/{interactionId}/responses/{responseId}/like | Like response
*InteractionApi* | [**mark_as_an_response**](docs/InteractionApi.md#mark_as_an_response) | **POST** /interactions/{interactionId}/responses/{responseId}/mark | Mark response as a response
*InteractionApi* | [**search_interactions**](docs/InteractionApi.md#search_interactions) | **GET** /interactions/search | Get list of matching interactions
*InteractionApi* | [**subscribe_interactin_category**](docs/InteractionApi.md#subscribe_interactin_category) | **POST** /interactions/categories/{categoryId}/subscribe | Subscribe interaction category
*InteractionApi* | [**subscribe_interaction**](docs/InteractionApi.md#subscribe_interaction) | **POST** /interactions/{interactionId}/subscribe | Subscribe interaction
*InteractionApi* | [**unmark_as_an_response**](docs/InteractionApi.md#unmark_as_an_response) | **POST** /interactions/{interactionId}/responses/{responseId}/unmark | Unmark response as a response
*InteractionApi* | [**unsubscribe_interactin_category**](docs/InteractionApi.md#unsubscribe_interactin_category) | **POST** /interactions/categories/{categoryId}/unsubscribe | Unsubscribe interaction category
*InteractionApi* | [**unsubscribe_interaction**](docs/InteractionApi.md#unsubscribe_interaction) | **POST** /interactions/{interactionId}/unsubscribe | Unsubscribe interaction
*InteractionApi* | [**update_interaction**](docs/InteractionApi.md#update_interaction) | **PUT** /interactions/{interactionId} | Update interaction
*InteractionApi* | [**update_interaction_category**](docs/InteractionApi.md#update_interaction_category) | **PUT** /interactions/categories/{categoryId} | Update interaction category
*InteractionApi* | [**update_response**](docs/InteractionApi.md#update_response) | **PUT** /interactions/responses/{responseId} | Update response
*NotificationApi* | [**get_notifications**](docs/NotificationApi.md#get_notifications) | **GET** /notifications | Get list of notifications
*NotificationApi* | [**mark_all_notification_as_read**](docs/NotificationApi.md#mark_all_notification_as_read) | **POST** /notifications/read/all | Mark all notification as read
*NotificationApi* | [**mark_notification_as_read**](docs/NotificationApi.md#mark_notification_as_read) | **POST** /notifications/read/{notificationId} | Mark notification as read
*NotificationApi* | [**notification_count**](docs/NotificationApi.md#notification_count) | **GET** /notifications/count | Get notifications count
*ProjectManagementApi* | [**add_milestone_comment**](docs/ProjectManagementApi.md#add_milestone_comment) | **POST** /milestones/{milestoneId}/comments | Comment on milestone
*ProjectManagementApi* | [**add_task_comment**](docs/ProjectManagementApi.md#add_task_comment) | **POST** /milestones/tasks/{taskId}/comments | Comment on task
*ProjectManagementApi* | [**create_milestone**](docs/ProjectManagementApi.md#create_milestone) | **POST** /milestones | Create milestone
*ProjectManagementApi* | [**create_task**](docs/ProjectManagementApi.md#create_task) | **POST** /milestones/{milestoneId}/tasks | Create task
*ProjectManagementApi* | [**delete_milestone**](docs/ProjectManagementApi.md#delete_milestone) | **DELETE** /milestones/{milestoneId} | Delete milestone
*ProjectManagementApi* | [**delete_task**](docs/ProjectManagementApi.md#delete_task) | **DELETE** /milestones/tasks/{taskId} | Delete task
*ProjectManagementApi* | [**get_milestones**](docs/ProjectManagementApi.md#get_milestones) | **GET** /milestones | Get list of milestones
*ProjectManagementApi* | [**get_milestones_comments**](docs/ProjectManagementApi.md#get_milestones_comments) | **GET** /milestones/{milestoneId}/comments | Get list of comments written on Milestones
*ProjectManagementApi* | [**get_task_comments**](docs/ProjectManagementApi.md#get_task_comments) | **GET** /milestones/tasks/{taskId}/comments | Get list of Comments written on task
*ProjectManagementApi* | [**get_user_tasks**](docs/ProjectManagementApi.md#get_user_tasks) | **GET** /milestones/tasks/{userId}/assigned | Get list of task assigned to user
*ProjectManagementApi* | [**update_milestone**](docs/ProjectManagementApi.md#update_milestone) | **PUT** /milestones/{milestoneId} | Update milestone
*ProjectManagementApi* | [**update_task**](docs/ProjectManagementApi.md#update_task) | **PUT** /milestones/tasks/{taskId} | Update task
*ProjectManagementApi* | [**update_task_status**](docs/ProjectManagementApi.md#update_task_status) | **PUT** /milestones/tasks/{taskId}/status | Update task status
*QuestionApi* | [**add_answer**](docs/QuestionApi.md#add_answer) | **POST** /questions/{questionId}/answers | Answer the specified question
*QuestionApi* | [**add_question**](docs/QuestionApi.md#add_question) | **POST** /questions | Share question without attachment
*QuestionApi* | [**add_question_0**](docs/QuestionApi.md#add_question_0) | **POST** /questions/attachment | Share question with attachment
*QuestionApi* | [**create_question_category**](docs/QuestionApi.md#create_question_category) | **POST** /questions/categories | Create question category
*QuestionApi* | [**delete_answer**](docs/QuestionApi.md#delete_answer) | **DELETE** /questions/answers/{answerId} | Delete answer
*QuestionApi* | [**delete_question**](docs/QuestionApi.md#delete_question) | **DELETE** /questions/{questionId} | Delete question
*QuestionApi* | [**delete_question_category**](docs/QuestionApi.md#delete_question_category) | **DELETE** /questions/categories/{categoryId} | Delete question category
*QuestionApi* | [**dislike_answer**](docs/QuestionApi.md#dislike_answer) | **POST** /questions/{questionId}/answers/{answerId}/dislike | Dislike answer
*QuestionApi* | [**get_answers**](docs/QuestionApi.md#get_answers) | **GET** /questions/{questionId}/answers | Get list of answers by questionId
*QuestionApi* | [**get_friends_questions**](docs/QuestionApi.md#get_friends_questions) | **GET** /questions/friends | Get list of questions shared by friends
*QuestionApi* | [**get_question**](docs/QuestionApi.md#get_question) | **GET** /questions/{questionId} | Get question by id
*QuestionApi* | [**get_question_categories**](docs/QuestionApi.md#get_question_categories) | **GET** /questions/categories | Get the list of question categories
*QuestionApi* | [**get_questions_for_user**](docs/QuestionApi.md#get_questions_for_user) | **GET** /questions | Get list of all questions visible to the user
*QuestionApi* | [**get_recommend_question**](docs/QuestionApi.md#get_recommend_question) | **GET** /questions/recommend | Get list of recommended questions
*QuestionApi* | [**get_recommended_questions_from_db**](docs/QuestionApi.md#get_recommended_questions_from_db) | **GET** /questions/{userId}/recommendedQuestions | Get list of recommended questions from DB
*QuestionApi* | [**get_recommended_users_from_db**](docs/QuestionApi.md#get_recommended_users_from_db) | **GET** /questions/{questionId}/recommendedUsers | Get list of recommended Users from DB
*QuestionApi* | [**get_user_questions**](docs/QuestionApi.md#get_user_questions) | **GET** /questions/{userId}/shared | Get list of questions shared by user
*QuestionApi* | [**get_user_subscribed_question_categories**](docs/QuestionApi.md#get_user_subscribed_question_categories) | **GET** /questions/categories/{userId}/subscribe | Get list of question categories subscribed by the user
*QuestionApi* | [**get_user_subscribed_questions**](docs/QuestionApi.md#get_user_subscribed_questions) | **GET** /questions/{userId}/subscribe | Get list of questions subscribed by user
*QuestionApi* | [**like_answer**](docs/QuestionApi.md#like_answer) | **POST** /questions/{questionId}/answers/{answerId}/like | Like answer
*QuestionApi* | [**mark_as_an_answer**](docs/QuestionApi.md#mark_as_an_answer) | **POST** /questions/{questionId}/answers/{answerId}/mark | Mark answer as a answer
*QuestionApi* | [**search_questions**](docs/QuestionApi.md#search_questions) | **GET** /questions/search | Get list of matching questions
*QuestionApi* | [**subscribe_question**](docs/QuestionApi.md#subscribe_question) | **POST** /questions/{questionId}/subscribe | Subscribe question
*QuestionApi* | [**subscribe_question_category**](docs/QuestionApi.md#subscribe_question_category) | **POST** /questions/categories/{categoryId}/subscribe | Subscribe question category
*QuestionApi* | [**unmark_as_an_answer**](docs/QuestionApi.md#unmark_as_an_answer) | **POST** /questions/{questionId}/answers/{answerId}/unmark | Unmark answer as a answer
*QuestionApi* | [**unsubscribe_question**](docs/QuestionApi.md#unsubscribe_question) | **POST** /questions/{questionId}/unsubscribe | Unsubscribe question
*QuestionApi* | [**unsubscribe_question_category**](docs/QuestionApi.md#unsubscribe_question_category) | **POST** /questions/categories/{categoryId}/unsubscribe | Unsubscribe question category
*QuestionApi* | [**update_answer**](docs/QuestionApi.md#update_answer) | **PUT** /questions/answers/{answerId} | Update answer
*QuestionApi* | [**update_question**](docs/QuestionApi.md#update_question) | **PUT** /questions/{questionId} | Update question
*QuestionApi* | [**update_question_category**](docs/QuestionApi.md#update_question_category) | **PUT** /questions/categories/{categoryId} | Update question category
*RewardsApi* | [**get_top_friends**](docs/RewardsApi.md#get_top_friends) | **GET** /rewards/points/top/friends | Get list of top friends
*RewardsApi* | [**get_top_users**](docs/RewardsApi.md#get_top_users) | **GET** /rewards/points/top | Get list of top users
*RewardsApi* | [**get_user_points**](docs/RewardsApi.md#get_user_points) | **GET** /rewards/points/{userId} | Get list of user points
*SocialApi* | [**add_friend**](docs/SocialApi.md#add_friend) | **POST** /social/friends/add | Add Friend
*SocialApi* | [**confirm_friend_request**](docs/SocialApi.md#confirm_friend_request) | **POST** /social/friends/request/action | confirm/ignore friend request
*SocialApi* | [**follow**](docs/SocialApi.md#follow) | **POST** /social/follow | Follow user
*SocialApi* | [**get_user**](docs/SocialApi.md#get_user) | **GET** /social/users/{userId} | Get user by id 
*SocialApi* | [**get_user_detail**](docs/SocialApi.md#get_user_detail) | **GET** /social/userDetail | Get user details 
*SocialApi* | [**get_user_followers**](docs/SocialApi.md#get_user_followers) | **GET** /social/followers/{userId} | Get list of followers
*SocialApi* | [**get_user_following**](docs/SocialApi.md#get_user_following) | **GET** /social/following/{userId} | Get list of users that are being followed
*SocialApi* | [**get_user_friends**](docs/SocialApi.md#get_user_friends) | **GET** /social/friends{userId} | Get list of friends
*SocialApi* | [**remove_friend**](docs/SocialApi.md#remove_friend) | **POST** /social/friends/remove | Remove friend 
*SocialApi* | [**request_friend**](docs/SocialApi.md#request_friend) | **POST** /social/friends/request | Send friend request
*SocialApi* | [**requests_for_me**](docs/SocialApi.md#requests_for_me) | **GET** /social/friends/request | Get list of friend requests
*SocialApi* | [**unfollow**](docs/SocialApi.md#unfollow) | **POST** /social/unfollow | Unfollow user
*UserAuthenticationApi* | [**add_notification_registered_id**](docs/UserAuthenticationApi.md#add_notification_registered_id) | **POST** /devices | Add device token
*UserAuthenticationApi* | [**add_user**](docs/UserAuthenticationApi.md#add_user) | **POST** /users | Add/Register new user
*UserAuthenticationApi* | [**authenticate**](docs/UserAuthenticationApi.md#authenticate) | **GET** /authenticate | Authenticate User
*UserAuthenticationApi* | [**change_password**](docs/UserAuthenticationApi.md#change_password) | **PUT** /users/password | Change password
*UserAuthenticationApi* | [**delete_user**](docs/UserAuthenticationApi.md#delete_user) | **DELETE** /users/{userId} | Delete user
*UserAuthenticationApi* | [**get_organizations**](docs/UserAuthenticationApi.md#get_organizations) | **GET** /organizations | Get list of organizations
*UserAuthenticationApi* | [**logout**](docs/UserAuthenticationApi.md#logout) | **GET** /logout | Logout


## Documentation For Models

 - [Answer](docs/Answer.md)
 - [Attachment](docs/Attachment.md)
 - [Blog](docs/Blog.md)
 - [Bucket](docs/Bucket.md)
 - [CommandInfo](docs/CommandInfo.md)
 - [Comment](docs/Comment.md)
 - [Complaint](docs/Complaint.md)
 - [ComplaintCategory](docs/ComplaintCategory.md)
 - [ContentDisposition](docs/ContentDisposition.md)
 - [DataFlavor](docs/DataFlavor.md)
 - [DataHandler](docs/DataHandler.md)
 - [DataSource](docs/DataSource.md)
 - [Discussion](docs/Discussion.md)
 - [Entity](docs/Entity.md)
 - [EntitySentiment](docs/EntitySentiment.md)
 - [Group](docs/Group.md)
 - [Idea](docs/Idea.md)
 - [IdeaUserRating](docs/IdeaUserRating.md)
 - [InputStream](docs/InputStream.md)
 - [Interaction](docs/Interaction.md)
 - [InteractionCategory](docs/InteractionCategory.md)
 - [InteractionResponse](docs/InteractionResponse.md)
 - [MediaType](docs/MediaType.md)
 - [Multimedia](docs/Multimedia.md)
 - [NER](docs/NER.md)
 - [NLC](docs/NLC.md)
 - [Notification](docs/Notification.md)
 - [Organization](docs/Organization.md)
 - [OutputStream](docs/OutputStream.md)
 - [ProjectManagement](docs/ProjectManagement.md)
 - [Question](docs/Question.md)
 - [QuestionCategory](docs/QuestionCategory.md)
 - [RequestForMe](docs/RequestForMe.md)
 - [Sentiment](docs/Sentiment.md)
 - [SentimentAnalytics](docs/SentimentAnalytics.md)
 - [Solution](docs/Solution.md)
 - [Tag](docs/Tag.md)
 - [Task](docs/Task.md)
 - [User](docs/User.md)
 - [UserDetail](docs/UserDetail.md)
 - [UserPoints](docs/UserPoints.md)
 - [VerveResponseAnswer](docs/VerveResponseAnswer.md)
 - [VerveResponseAnswerList](docs/VerveResponseAnswerList.md)
 - [VerveResponseBlog](docs/VerveResponseBlog.md)
 - [VerveResponseBlogList](docs/VerveResponseBlogList.md)
 - [VerveResponseComment](docs/VerveResponseComment.md)
 - [VerveResponseCommentList](docs/VerveResponseCommentList.md)
 - [VerveResponseComplaint](docs/VerveResponseComplaint.md)
 - [VerveResponseComplaintCategory](docs/VerveResponseComplaintCategory.md)
 - [VerveResponseComplaintCategoryList](docs/VerveResponseComplaintCategoryList.md)
 - [VerveResponseComplaintList](docs/VerveResponseComplaintList.md)
 - [VerveResponseDiscussion](docs/VerveResponseDiscussion.md)
 - [VerveResponseDiscussionList](docs/VerveResponseDiscussionList.md)
 - [VerveResponseEntitySentimentList](docs/VerveResponseEntitySentimentList.md)
 - [VerveResponseGroup](docs/VerveResponseGroup.md)
 - [VerveResponseGroupList](docs/VerveResponseGroupList.md)
 - [VerveResponseIdea](docs/VerveResponseIdea.md)
 - [VerveResponseIdeaList](docs/VerveResponseIdeaList.md)
 - [VerveResponseIdeaUserRatingList](docs/VerveResponseIdeaUserRatingList.md)
 - [VerveResponseInteraction](docs/VerveResponseInteraction.md)
 - [VerveResponseInteractionCategory](docs/VerveResponseInteractionCategory.md)
 - [VerveResponseInteractionCategoryList](docs/VerveResponseInteractionCategoryList.md)
 - [VerveResponseInteractionList](docs/VerveResponseInteractionList.md)
 - [VerveResponseInteractionResponse](docs/VerveResponseInteractionResponse.md)
 - [VerveResponseInteractionResponseList](docs/VerveResponseInteractionResponseList.md)
 - [VerveResponseMilestone](docs/VerveResponseMilestone.md)
 - [VerveResponseMilestoneList](docs/VerveResponseMilestoneList.md)
 - [VerveResponseNLCList](docs/VerveResponseNLCList.md)
 - [VerveResponseNotificationList](docs/VerveResponseNotificationList.md)
 - [VerveResponseOrganizationList](docs/VerveResponseOrganizationList.md)
 - [VerveResponseQuestion](docs/VerveResponseQuestion.md)
 - [VerveResponseQuestionCategory](docs/VerveResponseQuestionCategory.md)
 - [VerveResponseQuestionCategoryList](docs/VerveResponseQuestionCategoryList.md)
 - [VerveResponseQuestionList](docs/VerveResponseQuestionList.md)
 - [VerveResponseRequestForMeList](docs/VerveResponseRequestForMeList.md)
 - [VerveResponseSentimentAnalytics](docs/VerveResponseSentimentAnalytics.md)
 - [VerveResponseSolution](docs/VerveResponseSolution.md)
 - [VerveResponseSolutionList](docs/VerveResponseSolutionList.md)
 - [VerveResponseString](docs/VerveResponseString.md)
 - [VerveResponseTagList](docs/VerveResponseTagList.md)
 - [VerveResponseTask](docs/VerveResponseTask.md)
 - [VerveResponseTaskList](docs/VerveResponseTaskList.md)
 - [VerveResponseUser](docs/VerveResponseUser.md)
 - [VerveResponseUserDetail](docs/VerveResponseUserDetail.md)
 - [VerveResponseUserList](docs/VerveResponseUserList.md)
 - [VerveResponseUserPoints](docs/VerveResponseUserPoints.md)
 - [VerveResponseUserPointsList](docs/VerveResponseUserPointsList.md)
 - [VerveResponseWFTask](docs/VerveResponseWFTask.md)
 - [VerveResponseWFTaskList](docs/VerveResponseWFTaskList.md)
 - [WFTask](docs/WFTask.md)


## Documentation For Authorization


## default

- **Type**: OAuth
- **Flow**: implicit
- **Scopes**: N/A


## Author

[iEngage.io](http://iengage.io/)  [Aikon Labs Pvt Ltd](http://aikonlabs.com)

