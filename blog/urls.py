from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv_view/', views.cv_view, name='cv_view'),
    path('cv_view/contact_details', views.contact_details, name='contact_details'),
    path('cv_view/personal_profile', views.personal_profile, name='personal_profile'),
    path('cv_view/education', views.education, name='education'),
    path('cv_view/work_experience', views.work_experience, name='work_experience'),
    path('cv_view/interests_achievements', views.interests_achievements, name='interests_achievements'),
]
