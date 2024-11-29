from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

view_swagger = get_schema_view(
    openapi.Info(
        title='DRF Boilerplate',
        description='Documentación de las APIs de Boilerplate',
        default_version='0.1',
    ),
    public=True,  # Hace que el esquema sea accesible públicamente
    permission_classes=[AllowAny],  # Permite acceso sin autenticación
)

