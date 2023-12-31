from django.http import JsonResponse
from django.shortcuts import render
import requests

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User

from .models import Team
from .serializers import TeamSerializer

# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    serializer_class= TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        return self.queryset.filter(members__in=[self.request.user]).first()
    
    def perform_create(self, serializer):
        obj = serializer.save(created_by = self.request.user)
        obj.members.add(self.request.user)
        obj.save()


@api_view(['GET'])
def get_my_team(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    serializer = TeamSerializer(team)

    return Response(serializer.data)

@api_view(['POST'])
def add_member(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    username = request.data['username']

    print("Username", username)

    user = User.objects.get(username = username)

    team.members.add(user)
    team.save()

    return Response()
