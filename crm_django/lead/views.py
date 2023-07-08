from django.shortcuts import render

from rest_framework import viewsets

from team.models import Team

from .models import Lead
from .serializers import LeadSerializer

# Create your views here.

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first() #se l'utente è nella lista ritorno il team
        return self.queryset.filter(team=team) #restituisco solo quelli del team a cui appartiene l'utente
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)



