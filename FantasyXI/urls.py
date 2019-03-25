from django.contrib import admin
from django.urls import path
from player import views as player_views
from team import views as team_views
from django.urls import include
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teams/', team_views.ListCreateTeam.as_view()),
    path('team/<int:pk>/', team_views.TeamDetail.as_view()),
    path('edit-team/<int:pk>/', team_views.EditTeam.as_view()),
    path('lineup/<int:pk>/', team_views.LineUp.as_view()),
    path('add-player/', team_views.AddPlayerToTeam.as_view()),
    path('remove-player/', team_views.RemovePlayerFromTeam.as_view()),
    # path('make-captain/', , ),
    path('players/', player_views.ListCreatePlayer.as_view()),
    path('edit-player/<int:pk>/', player_views.EditPlayer.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('refresh-token/', refresh_jwt_token),
]
