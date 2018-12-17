import json

from pathlib import Path
from rest_framework import generics, response, exceptions
from django.conf import settings
from django.http import Http404
from . import serializers


class InitialMixin(object):
    def initial(self, request, *args, **kwargs):
        with open(settings.VULHUB['CONF_FILE'], 'r', encoding='utf-8') as f:
            self.environments = json.load(f)

        super().initial(request, *args, **kwargs)


class EnvironmentList(InitialMixin, generics.ListAPIView):
    serializer_class = serializers.EnvironmentSerializer

    def get_queryset(self):
        return self.environments


class EnvironmentDetail(InitialMixin, generics.RetrieveAPIView):
    serializer_class = serializers.EnvironmentSerializer

    def get_queryset(self):
        return self.environments

    def get_object(self):
        path = self.kwargs['path']
        meta = next((meta for meta in self.get_queryset() if path == meta['path']), None)

        if meta is None:
            raise Http404

        dockerfile_cn = Path(settings.VULHUB['VULHUB_DIR']).joinpath(meta['path'], 'README.zh-cn.md')
        dockerfile = Path(settings.VULHUB['VULHUB_DIR']).joinpath(meta['path'], 'README.md')
        if dockerfile_cn.exists():
            meta['description'] = dockerfile_cn.read_text(encoding='utf-8')
        elif dockerfile.exists():
            meta['description'] = dockerfile.read_text(encoding='utf-8')
        else:
            raise Http404

        return meta
