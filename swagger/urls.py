from django.urls import path

from swagger.views import SwaggerSchemaView

urlpatterns = [
    path('', SwaggerSchemaView.as_view(), name='docs'),
]