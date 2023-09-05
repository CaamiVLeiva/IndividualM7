### Realización del Proyecto

Para esta primera versión del proyecto, se realizaron las siguientes tareas:

- Se creó un proyecto en Django llamado 'task_tracker', incluyendo las aplicaciones necesarias para abordar el problema descrito en las especificaciones. (python, django, django-bootstrap4, pyscopg2)

- Se conectó el proyecto a una base de datos en PostgreSQL. 

- Se realizó la migración inicial para asegurar que los cambios en el modelo se reflejen en la base de datos PostgreSQL.

- Se definieron usuarios de tipo superuser y modelo usuario de Django para creacion de usuarios que podrán interactuar con sus propias tareas.
    El superusuario se creó con el nombre de usuario 'admin' y la contraseña 'admin' para facilitar el acceso a la administración del sistema.

    Se creó un usuario de prueba con el nombre de usuario 'test_user' y la contraseña 'contraseñatestuser' para permitir la prueba de las funciones del sistema.

- La página principal se diseñó como una página con el logo e imagen representativa de la aplicación, y se agregó un enlace que lleva al Login de usuario y al registro de usuario.

- Se implementaron páginas de login y logout de usuarios. El login lleva a una página simple de Bienvenida ('landing'), donde posteriormente se implementará la vista de Listado de Tareas Pendientes. El logout redirige a la página de inicio definida anteriormente.

## Realización del Proyecto (Versión 2.0)

En esta segunda versión del proyecto, se llevaron a cabo las siguientes tareas adicionales:

1. **Actualización del Modelo de Datos:** Se realizó una actualización en el modelo de datos para incorporar dos campos esenciales en la entidad "Task". Cada tarea ahora cuenta con un campo "estado" que puede ser "pendiente", "en progreso" o "completada", además de un campo "tags" que permite asociar una o varias etiquetas, como "trabajo", "hogar" o "estudio".

2. **Migración de la Base de Datos:** Para reflejar estos cambios en el modelo, se procedió a modificar la migración de la base de datos PostgreSQL, asegurando así que los nuevos campos sean debidamente implementados.

3. **Gestión de Etiquetas:** Se habilitó la gestión del modelo "Tags" desde la interfaz de administración de Django. Esto permite la creación y administración de etiquetas de manera sencilla.

4. **Requisitos de Tareas:** Se garantizó que cada tarea esté compuesta por un título, descripción, fecha de vencimiento, estado (que puede ser "pendiente", "en progreso" o "completada") y una etiqueta (por ejemplo, "trabajo", "hogar" o "estudio").

Puedes consultar los detalles del modelo de datos actualizado en el código fuente del proyecto.
