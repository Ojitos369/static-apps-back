from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import path, re_path

from .api import (generate_names)

from .api import test


schema_view = get_schema_view(
    openapi.Info(
        title="Names for Static Apps",
        default_version='v1',
        description="Apis para la app de names",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


app_name = 'names'

urlpatterns = [
    # -------------------   DOCS URLS   -------------------
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path('generate_names/', generate_names, name='generate_names'),
    
    path('test/', test, name='test'),
]
