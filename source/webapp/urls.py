from django.urls import path
from webapp.views import index, create_cat, cat_actions

urlpatterns = [
    path('', index),
    path('cat/create/', create_cat),
    path('cat/action/', cat_actions)
]
