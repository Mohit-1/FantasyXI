"""FantasyXI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from player.views import PlayerList, PlayerDetail
from team.views import TeamList, TeamDetail, TeamPlayerUpdate
from django.urls import include
from rest_framework_jwt.views import refresh_jwt_token
#from team.views import teamDetail, teamList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teams/', TeamList.as_view(), name='team_list'),
    path('players/', PlayerList.as_view(), name='player_list'),
    path('player/<int:pk>/', PlayerDetail.as_view(), name='player_detail'),
    path('team/<int:pk>/', TeamDetail.as_view(), name='team_detail'),
    path('team-players/update/', TeamPlayerUpdate.as_view(), name='team_player_update'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('refresh-token/', refresh_jwt_token),
]
