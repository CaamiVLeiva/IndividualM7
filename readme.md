## Preguntas sobre Django

### 1. ¿Cuáles son las bases de datos soportadas por Django y en qué se diferencian?

Django admite varias bases de datos, incluyendo PostgreSQL, MySQL, SQLite y Oracle, entre otras. La diferencia principal radica en la gestión de la base de datos y las características específicas que cada sistema ofrece. Por ejemplo:

- **PostgreSQL**: Es una base de datos relacional de código abierto con un fuerte énfasis en la extensibilidad y la conformidad con los estándares.

- **MySQL**: Es otra base de datos relacional de código abierto, conocida por su rendimiento y velocidad.

- **SQLite**: Es una base de datos ligera, adecuada para aplicaciones pequeñas y de desarrollo rápido.

- **Oracle**: Es una base de datos empresarial con características avanzadas y orientadas a grandes empresas.

### 2. ¿Qué es una migración en Django y para qué se utiliza?

Una migración en Django es un proceso que permite realizar cambios en la estructura de la base de datos de una aplicación de manera controlada y mantenible. Se utiliza para crear, modificar o eliminar tablas, campos, índices y restricciones en la base de datos sin necesidad de escribir código SQL manualmente. Las migraciones son esenciales para mantener la consistencia entre el modelo de datos de la aplicación y la base de datos subyacente.

### 3. ¿Cuál es la diferencia entre usar consultas SQL y consultas ORM en Django?

- **Consultas SQL**: Las consultas SQL son consultas directas a la base de datos utilizando lenguaje SQL. Son flexibles pero pueden ser propensas a errores y más difíciles de mantener, especialmente en aplicaciones complejas. Se deben escribir manualmente y pueden variar según la base de datos utilizada.

- **Consultas ORM (Object-Relational Mapping)**: Django proporciona un ORM que permite realizar consultas utilizando objetos y métodos de Python en lugar de SQL directamente. Esto hace que las consultas sean más legibles, portátiles y menos propensas a errores. El ORM se encarga de generar SQL compatible con la base de datos subyacente.

### 4. ¿Cómo se instalan los paquetes de base de datos en Django y cuál es su importancia?

Los paquetes de base de datos en Django se instalan mediante el comando `pip install [nombre del paquete]`, donde `[nombre del paquete]` es el nombre del paquete de la base de datos que se desea utilizar, por ejemplo, `psycopg2` para PostgreSQL.

La importancia de instalar los paquetes de base de datos radica en la capacidad de Django para interactuar con la base de datos elegida

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

