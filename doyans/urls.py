from django.contrib import admin
from django.urls import path

from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# Swagger documentation setup
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Snippets API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

urlpatterns = [

    # admin
    path('admin/', admin.site.urls),

    # docs
    # path('docs/json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('docs/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('docs/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # api endpoints
    
]
