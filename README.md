# Hospital management
<div align='center'>
 
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)
![DjangoRestFramework](https://img.shields.io/badge/-Django%20Rest%20-880808?logo=django&logoColor=white&style=flat-square)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-3776AB?logo=postgresql&logoColor=white&style=flat-square)
![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white&style=flat-square) </div>

 _ _ _ _ _ _ _ _ _ _ _

#### For doctor
* Apointment list for today
* Can leave comment on patient's condition and add treatment conducted to patient during appointment
* Search and view all patient data

#### For admin
* Creating and assigning apointments to doctors.
* Create patient record

_ _ _ _ _ _ _ _ _ _ _ 
### Features
- [x] **JWT** authentication
- [x] **Search** for Patient Information
- [x] **Calculation** of treatment and services costs provided

_ _ _ _ _ _ _ _ _ _ _

### Build with
* Django REST
* Postgres
* Docker
* Unit testing
* Python
_ _ _ _ _ _ _ _ _ _ _

### Installation

1. Create '.env' file in settings.py root and paste this:

 ```
DEBUG=0
SECRET_KEY=your_secret_key

POSTGRES_NAME=your_postgres_name
POSTGRES_USER=your_postgres_username
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
   ```
2. Create a docker image and run:

```
docker-compose up --build
```
