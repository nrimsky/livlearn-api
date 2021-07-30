from django.urls import path
from django.contrib import admin
from livlearn.api import views


urlpatterns = [
    path('links/', views.LinkListView.as_view(), name='link-list'),
    path('tags/', views.TagListView.as_view(), name='tag-list'),
    path('submit-a-form/', views.FormSubmissionView.as_view(), name='form-submit')
]

urlpatterns += [
    path('admin/', admin.site.urls),
]
