import os
import json

from rest_framework import generics, response
from django.conf import settings
from . import serializers


class InitialMixin(object):
    def initial(self, request, *args, **kwargs):
        with open(settings.VULHUB['CONF_FILE'], 'r', encoding='utf-8') as f:
            self.environments = json.load(f)

        super().initial(request, *args, **kwargs)


class EnvironmentList(InitialMixin, generics.GenericAPIView):
    serializer_class = serializers.EnvironmentSerializer

    def get_queryset(self):
        return self.environments

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    # def list(self, request, *args, **kwargs):
    #     return self.environments
