from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.homepage,name="homepage"),
    path("Email",views.Email_tab,name="Email_tab"),
    path("Email/<side_tab>",views.Email_tabs,name="Email_tabs"),
    path("Email/Create_campaign/<campaign_name>",views.create_campaign,
         name="create_campaign"),
    path("Email/<side_tab>/<sub_side_tab>", views.sub_side_tab,
         name="sub_side_tab"),

]
