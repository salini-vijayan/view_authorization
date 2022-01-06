from django.urls import path, include
# from core import views as core_views
from core import views

urlpatterns = [
    path('', views.listing, name='listing'),
    path('view/<int:blog_id>', views.view_blog, name='view_blog'),
    path('see-request/', views.see_request, name='see_request'),
    path('user-info/', views.user_info, name='user-info'),
    path('private-place/', views.private_place, name='private-place'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("staff_place/", views.staff_place),
    path("add_messages/", views.add_messages),

]
# view can be defined in this way also...
# path('view/<int:blog_id>', core_views.listing, name='view_blog'),
