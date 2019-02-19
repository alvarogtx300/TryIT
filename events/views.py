import datetime
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from TryIT.settings_global import EDITION_YEAR
from events.models import Event
from events.templates.serializers import EventSerializer


class EscapeRoomSessionsView(ListAPIView):
    queryset = Event.objects.all().filter(type__id=1, edition__year=EDITION_YEAR) # 0 is the Escape room type
    serializer_class = EventSerializer
