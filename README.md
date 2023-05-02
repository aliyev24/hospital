# Hospital management functions
#### For admin
* Creating and assigning apointments to doctors.
* Create patient record
#### For doctor
* Apointment list for today
* Doctor can leave comment on patient's condition and add treatment conducted or service provided to patient during appointment
* Search and view all patient data
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
