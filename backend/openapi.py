from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

view_swagger = get_schema_view(
    openapi.Info(
        title='Notebook API',
        description='Esta aplicación permite a los usuarios gestionar notas personales de manera eficiente. Los usuarios pueden registrarse, iniciar sesión y realizar todas las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre sus notas. ',
        default_version='0.1',
    ),
    public=True,  # Hace que el esquema sea accesible públicamente
    permission_classes=[AllowAny],  # Permite acceso sin autenticación
)

