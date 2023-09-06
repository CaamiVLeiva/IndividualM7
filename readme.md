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

## Realización del Proyecto (Versión 4.0)

En esta cuarta versión del proyecto, hemos realizado mejoras y correcciones para garantizar un funcionamiento más fluido y una experiencia de usuario aún mejor. Además de las actualizaciones mencionadas anteriormente, hemos abordado los siguientes puntos:

### Mejora en la Interfaz de Usuario
Hemos optimizado la interfaz de usuario para que sea más intuitiva y agradable. Se han realizado ajustes en la disposición de elementos y se ha trabajado en la usabilidad general de la aplicación.

### Corrección de Errores
Se han solucionado pequeños problemas que se encontraron en versiones anteriores, como errores de redirección.

### Función de Filtro Avanzado
Ahora, en la vista de listado de tareas pendientes, los usuarios pueden utilizar un filtro avanzado para buscar tareas específicas según criterios como etiquetas, estado y fecha de vencimiento. Esto facilita la gestión de tareas cuando hay muchas en la lista.

### Mejoras en la Creación y Edición de Tareas
La vista de creación y edición de tareas ha sido perfeccionada para que sea más eficiente y precisa. Ahora puedes seleccionar múltiples etiquetas para una tarea y definir el estado de manera más sencilla.

### Función de Observaciones
Respondiendo a la solicitud del cliente, hemos añadido un campo de observaciones en la vista de visualización de tareas. Los usuarios pueden registrar observaciones detalladas sobre cada tarea, y estas observaciones son editables en cualquier momento. Esto permite un mejor seguimiento y documentación de las tareas.

## Realización del Proyecto (Versión 5.0)

En esta quinta versión del proyecto, se han realizado las siguientes mejoras y adiciones:

### Habilitación del Filtro en la Vista de Listado

Se ha habilitado una función de filtro en la vista de listado de tareas. Con esta funcionalidad, los usuarios pueden aplicar filtros basados en diferentes criterios, como etiquetas, estado y fecha de vencimiento. Cada vez que se realice un cambio en los filtros, el listado mostrará las tareas activas del usuario que cumplan con las condiciones ingresadas y/o seleccionadas. Esto simplifica la gestión de tareas cuando se necesita buscar tareas específicas en una lista extensa.

### Vista de Edición de Tareas

Se ha implementado una vista de edición de tareas que permite a los usuarios modificar los datos de una tarea existente. En esta vista, se presentan los datos del formulario correspondiente, incluyendo la opción de seleccionar la etiqueta a la que corresponde la tarea. Es importante destacar que esta vista de edición comparte el mismo template con la vista de creación de tareas, lo que facilita la navegación y la interacción del usuario.

### Implementación de la Vista de Edición

Desde la vista de edición de tareas, los usuarios pueden realizar cambios en los datos de una tarea y guardar esos cambios. Una vez que los cambios se guardan correctamente, el sistema redirecciona al usuario a la vista de visualización de la tarea, donde pueden revisar los detalles actualizados. Esta funcionalidad proporciona a los usuarios una manera eficaz de editar y actualizar sus tareas de manera flexible.

## Realización del Proyecto (Versión 6.0)

En esta sexta versión del proyecto, se han incorporado nuevas funcionalidades en la vista de Visualización de Tareas para mejorar la interacción y la gestión de tareas. A continuación, se describen las adiciones realizadas:

### Registro de Observaciones en la Vista de Visualización

Se ha agregado un formulario en la vista de Visualización de Tareas que permite a los usuarios registrar observaciones sobre la tarea que están visualizando. Este formulario incluye un campo de texto en el que los usuarios pueden ingresar sus observaciones. Además, se ha incorporado un botón "Guardar Observaciones" que permite registrar estas observaciones en la base de datos. Al cargar la vista de Visualización, el campo de texto mostrará las observaciones previamente registradas, lo que facilita el seguimiento y la documentación detallada de las tareas.

### Acciones en la Vista de Visualización de Tareas

En la vista de Visualización de Tareas, se han agregado las siguientes acciones:

- **Eliminar**: Esta acción permite a los usuarios eliminar el registro de la tarea que están visualizando. Una vez confirmada la eliminación, el registro se borrará de la base de datos, y luego se redireccionará al usuario a la vista de Listado de Tareas.

- **Completar**: Con esta acción, los usuarios pueden cambiar el estado de la tarea de "pendiente" a "terminado". Después de que se haya realizado esta actualización en la base de datos, se redireccionará automáticamente al usuario a la vista de Listado de Tareas.

Estas nuevas funcionalidades en la vista de Visualización de Tareas brindan a los usuarios un mayor control sobre la gestión de sus tareas y la capacidad de registrar observaciones importantes para cada tarea.