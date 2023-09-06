## Realización del Proyecto

Para esta primera versión del proyecto, se realizaron las siguientes tareas:

- Se creó un proyecto en Django llamado 'task_tracker', incluyendo las aplicaciones necesarias para abordar el problema descrito en las especificaciones (Python, Django, django-bootstrap4, psycopg2).

- Se conectó el proyecto a una base de datos en PostgreSQL.

- Se realizó la migración inicial para asegurar que los cambios en el modelo se reflejen en la base de datos PostgreSQL.

- Se definieron usuarios de tipo superusuario y modelo usuario de Django para la creación de usuarios que podrán interactuar con sus propias tareas. El superusuario se creó con el nombre de usuario 'admin' y la contraseña 'admin' para facilitar el acceso a la administración del sistema. También se creó un usuario de prueba con el nombre de usuario 'test_user' y la contraseña 'contraseñatestuser' para permitir la prueba de las funciones del sistema.

- La página principal se diseñó como una página con el logo e imagen representativa de la aplicación, y se agregó un enlace que lleva al login de usuario y al registro de usuario.

- Se implementaron páginas de login y logout de usuarios. El login lleva a una página simple de Bienvenida ('landing'), donde posteriormente se implementará la vista de Listado de Tareas Pendientes. El logout redirige a la página de inicio definida anteriormente.

## Realización del Proyecto (Versión 2.0)

En esta segunda versión del proyecto, se llevaron a cabo las siguientes tareas adicionales:

1. **Actualización del Modelo de Datos:** Se realizó una actualización en el modelo de datos para incorporar dos campos esenciales en la entidad "Task". Cada tarea ahora cuenta con un campo "estado" que puede ser "pendiente", "en progreso" o "completada", además de un campo "tags" que permite asociar una o varias etiquetas, como "trabajo", "hogar" o "estudio".

2. **Migración de la Base de Datos:** Para reflejar estos cambios en el modelo, se procedió a modificar la migración de la base de datos PostgreSQL, asegurando así que los nuevos campos sean debidamente implementados.

3. **Gestión de Etiquetas:** Se habilitó la gestión del modelo "Tags" desde la interfaz de administración de Django. Esto permite la creación y administración de etiquetas de manera sencilla.

4. **Requisitos de Tareas:** Se garantizó que cada tarea esté compuesta por un título, descripción, fecha de vencimiento, estado (que puede ser "pendiente", "en progreso" o "completada") y una etiqueta (por ejemplo, "trabajo", "hogar" o "estudio").

## Realización del Proyecto (Versión 3.0)

En esta tercera versión del proyecto, se implementaron las siguientes mejoras y cambios:

- **Administración de Etiquetas:** Desde la administración de Django, ahora es posible agregar etiquetas que sean estrictamente necesarias según la historia del proyecto. Esto permite un control más granular sobre las etiquetas disponibles para las tareas.

- **Vista de Listado de Tareas Pendientes:** Se generó una vista que muestra todas las tareas pendientes del usuario actual, ordenadas por fecha de vencimiento. En la parte superior de esta vista, encontrarás un botón "Agregar Tarea" que te llevará a la ventana de creación de tareas. Cada tarea en la lista tiene un botón "Ver" que te lleva a la vista de visualización de la tarea correspondiente.

- **Vista de Visualización de Tarea:** En esta vista, puedes ver todos los detalles relacionados con una tarea seleccionada. En la parte superior, hemos agregado botones que te permiten realizar las siguientes acciones:

  - **Editar Tarea:** Te lleva a la vista de edición de la tarea.
  - **Eliminar:** Elimina la tarea después de la confirmación del usuario.
  - **Completar:** Cambia el estado de la tarea de "pendiente" a "completada".
  - **Retornar:** Te lleva de vuelta a la vista de listado de tareas.

- **Carga de Datos en la Vista de Listado:** La vista de listado de tareas pendientes ahora carga los datos directamente desde la base de datos. Si no hay datos en la tabla correspondiente, puedes agregarlos directamente en la base de datos para ver reflejada la lista de tareas.

- **Tarea Ingresada por Base de Datos:** Una tarea llamada "tareadb" fue creada por el usuario "admin" y se encuentra en la base de datos como parte de la demostración del proyecto.

Estos cambios mejoran significativamente la funcionalidad de nuestro proyecto de gestión de tareas, permitiéndote administrar y visualizar tus tareas de manera más efectiva. ¡Esperamos que estos cambios sean útiles para ti!
