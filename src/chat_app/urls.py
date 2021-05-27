from django.urls import path
from chat_app.views import ChatGroupListCreateView, ChatGroupRetriveUpdateDestroyView


urlpatterns = [
    path("", ChatGroupListCreateView.as_view(), name='chat-list-create-api'),
    path("<int:pk>/", ChatGroupRetriveUpdateDestroyView.as_view(), name='chat-retrieve-update-destroy-create-api')
]
