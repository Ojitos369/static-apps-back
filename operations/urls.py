from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import path, re_path
from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

app_name = 'operations'
urlpatterns = [
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('sum/<str:data_1>/<str:data_2>', views.sum_matrix, name='sum'),
    path('sub/<str:data_1>/<str:data_2>', views.sub_matrix, name='sub'),
    path('mult/escalar/<str:escalar>/<str:data>', views.escalar_multiply, name='multiply_escalar'),
    path('mult/matrix/<str:data_1>/<str:data_2>', views.matrix_multiply, name='multiply_matrix'),
    path('trans/<str:data>', views.trans_matrix, name='transpose')
]
