from django.urls import path
from . import views
urlpatterns = [
    path("user-signup/",views.userSignup),
    path("user-signin/",views.userLogin),
    path("messages/",views.MessageView.as_view()),
]
