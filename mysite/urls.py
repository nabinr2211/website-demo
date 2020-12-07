from django.urls import path

from mysite import views

app_name = 'site'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/add_category/', views.add_category, name='add_category'),
    path('dashboard/add_tag/', views.add_tag, name='add_tag'),
    path('dashboard/add_member/', views.add_member, name='add_member'),
    path('dashboard/add_post/', views.add_post, name='add_post'),
    path('dashboard/edit_post/<int:id>', views.edit_post, name='edit_post'),
    path('dashboard/delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('contact/', views.contact, name='contact'),

]
