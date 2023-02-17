## 📁 Acceso al proyecto

**Para iniciar en el proyecto necesitamos tener descargado y actualizado PYTHON, PIP y Django. En este caso cree un entorno virtual el cual contiene todo lo necesario para inicializar el proyecto. El entorno virtual se llama "venv" para inicializarlo nos ubicamos en la terminal en el proyecto despues ingresamos el siguiente comando:**

**$-venv/Script/activate.bat**

**Verificamos que esten descargados y actualizados correctamente con --version**
![image](https://user-images.githubusercontent.com/64494150/219547262-b1b8508b-4361-4a12-8a0f-09769824562b.png)

**Se creo una Base de Datos llamado "test_developer" en PostgreSQL, para poder crear la conexion entre Django y PostgreSQL necesitamos una libreria llamada "psycopg2" se instala con PIP de la siguiente forma:**

![image](https://user-images.githubusercontent.com/64494150/219547996-19051095-f2d3-494d-a9d0-d9664d929bea.png)

**Podemos observar todos los archivos que contiene el proyecto**


![image](https://user-images.githubusercontent.com/64494150/219548540-28457e27-f5dc-450b-9bf8-d09d6e26fc5c.png)

**Para la configuracion de la conexion a la Base de datos de Posgresql en Django en el archivo settings.py encontramos lo siguiente:**

![image](https://user-images.githubusercontent.com/64494150/219549804-77cac557-0a39-4d4d-8e0a-a0fdc3efc71d.png)

**Hay una clase con el modulo TASK el cual es el que vamos a utilizar para la creacion de la aplicacion**

![image](https://user-images.githubusercontent.com/64494150/219550059-ece8d087-b842-473b-a8e0-20b3d14dcb63.png)

**Importante crear la migraciones de django a la base de datos ejecutando los siguientes comandos en la terminal:**

**$-python manage.py makemigrations**

**$-python manage.py migrate**

![image](https://user-images.githubusercontent.com/64494150/219550349-e5ee8438-2ba3-46da-83fe-90e3492fb85b.png)

**Ejecutamos el siguiente comando para iniciar el servidor:**

**$-python manage.py runserver**

![image](https://user-images.githubusercontent.com/64494150/219550618-4ebe4493-ba99-4457-b630-2a29a179b33e.png)

**Al iniciar el servidor ingresamos en la siguiente url la cual nos de una primera vista de la aplicacion:**

**URL: http://127.0.0.1:8000/app_crud/**

![image](https://user-images.githubusercontent.com/64494150/219551034-e2abbf00-e735-4b9c-b48a-f4c7f17f0675.png)

**Cuando no hay ninguna tarea guardade en la Base de datos nos indica un mensaje de que no se encuentra ninguna tarea**

**Aqui observamos los campos que podemos ingresar para crear una nueva tarea, la cual se puede eliminar y editar**

![image](https://user-images.githubusercontent.com/64494150/219551273-c968d727-222a-44d6-b65f-cb9db991a93d.png)

**Al actualizar la tarea aparece de la siguiente forma:**

![image](https://user-images.githubusercontent.com/64494150/219551661-ab90461b-2381-457d-9e6f-f0ec943e3a74.png)

![image](https://user-images.githubusercontent.com/64494150/219551719-a95b4a85-fdc9-4cd5-bd8e-4dc4f6b2a046.png)





## :hammer:Funcionalidades del proyecto

- `Funcionalidad 1`: descripción de la funcionalidad 1- `Funcionalidad 2`: descripción de la funcionalidad 2- `Funcionalidad 2a`: descripción de la funcionalidade 2a relacionada con la funcionalidad 2- `Funcionalidad 3`: descripción de la funcionalidad 3


x

## 🛠️ Abre y ejecuta el proyecto

**Muestra las instrucciones necesarias para abrir y ejecutar el proyecto**
