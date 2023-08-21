# Credit Card Register
 Challenge for the backend developer job

 Author: [Igor Santos Brito](https://www.linkedin.com/in/igor-brito-916a60b1/)

 ## About 
The challenge was building an API to register credit card information following rules related to the validation of the credit card data.

 ## Technologies
 - Python 3.9
 - Django
 - Django Rest Framework (DRF)
 - Docker
 - Docker Compose
 - PostgreSQL

 I developed a API using mainly Django and DRF and created a dockerized environment to make it easier for the developer to configure the project and to make everyone have a very similar environments

 ## Setup The project
 Create a .env file at the root directory and copy the content from the .env.example file to the .env file. 

#### OBS: The environment variables must be diferente from the ones at the production environment.

The project have a docker compose to run the project at a development environment. So you can choose rather run on a container or not.

### Docker environment

Create the project image then execute the docker compose.

```
make build_server_image
make docker_run_server
```  
after the command you will have two dokcer containers running one with the postgresql database and anothe with the aplication.

Now we need to execute the migrations to create the database tables. 
```
make docker_migrate
```
After that we have a database readly to use. Now we have to create a super user to access the endpoints
```
make docker_create_user
```

The command will create a user with username "admin" and password "1234". This user should be create only at development environment for test purpose.

#### We are ready to use it
This docker compose was made to be used at the development, so every change you do at the code will be reflected at the container. So you can develop while the container is running, there is no need to build another image.

You will need to build another image when installing a new dependency

### Local environment
At the root directory create a virtual env for python 3.9, activate it and install all requirements
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Initiate your local postgres and setup the connection data at the .env.

Now execute the migrations and create a superuser with the username as admin, and password 1234

```
python manage.py migrate
python manage.py createsuperuser
```

Now run the the project server
```
python manage.py runserver 0.0.0.0:8080
```

## Tests
The project have tests to ensure that the validation of the credit card data is working properly. As this is a sensitive matter, we must alway keep this tests updated.

To execute the tests at the docker container run

```
make docker_run_tests
```
<br/>


## API

We have 5 main endpoints 3 to create and access the credit card data, 1 to login with the user and another to logout.

To access any credit card endpoint a session token is required, it can be acquired at the login endpoint.

### User Endpoints
`User Login` [POST - /user/auth/login](#POST-/user/auth/login) <br/>
`User Logout` [GET -/user/auth/logout](#GET-/user/auth/logout) <br/>

### Credit Card endpoints
`List all credit cards ` [GET - /api/v1/credit-card](#GET-/api/v1/credit-card) <br/>
`Retrieve a single credit card by id ` [GET - /api/v1/credit-card/<pk>](#GET-/api/v1/credit-card/<pk>) <br/>
`Create a new credir card ` [POST - /api/v1/credit-card](#POST-/api/v1/credit-card) <br/>


___

### POST - /user/auth/login
At the login you will get the token required to access the credit card endpoints. <br/>
You can use the default user we created to test the api.

***Payload***
|          Name | Required |  Type   | Description                                                                                                                                                         |
| -------------:|:--------:|:-------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `username` | required | string  | user username. <br/> If you uses the super user default we created the value will be `admin`.                                                                   |
|    `password` | required | string  | user password. <br/> If you uses the super user default we created the value will be `1234`.          |

***Response***
```
{
    "token": <token_key>
}

```


### GET - /user/auth/logout
At this endpoint you will make invalid the authentication token you already have. <br/>
To access this endpoint you will need to at the follow key value to the request hearder
***Request Header***
```
{
...
"Authorization": "Token <token_key>
}

```

### GET - /api/v1/credit-card
At this endpoint you will list all the credit card registered. <br/>
To access this endpoint you will need to at the follow key value to the request hearder
***Request Header***
```
{
...
"Authorization": "Token <token_key>
}

```

*** Response ***
```
[
    {
        "id": 1,
        "holder": "name owner 1",
        "number": "*************486",
        "brand": "visa",
        "created_at": "2023-08-21T02:11:30.960385Z",
        "updated_at": "2023-08-21T02:11:30.960446Z"
    },
    {
        "id": 2,
        "holder": "name owner 2",
        "number": "*************486",
        "brand": "mastercard",
        "created_at": "2023-08-21T02:21:45.351515Z",
        "updated_at": "2023-08-21T02:21:45.351591Z"
    },
]

```

### GET - /api/v1/credit-card/<pk>
At this endpoint you will retrieve a single credit card by the id. <br/>
To access this endpoint you will need to at the follow key value to the request hearder
***Payload***
|          Name | Required |  Type   | Description                                                                                                                                                         |
| -------------:|:--------:|:-------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `holder` | required | string  | Name of the credit card owner. Must be a string with more than 3 characters                                               |
|    `number` | required | string  | Number of the credit card (this value will be encrypted at the database)          |
|    `cvv` | optionl | string  | The numbers behide the card it is optional, but if you add this key at the payload it must have a valid value. with 3 or 4 characters.        |
|    `exp_date` | required | string  | Expiration date, must be a string with the month and year at the following format  `02/206`          |

***Request Header***
```
{
...
"Authorization": "Token <token_key>
}

```

*** Response ***
```
[
    {
        "id": 1,
        "holder": "name owner 1",
        "number": "*************486",
        "brand": "visa",
        "created_at": "2023-08-21T02:11:30.960385Z",
        "updated_at": "2023-08-21T02:11:30.960446Z"
    },
]

```

### POST - /api/v1/credit-card/
At this endpoint you will be able to create a credit card. <br/>
To access this endpoint you will need to at the follow key value to the request hearder
***Request Header***
```
{
...
"Authorization": "Token <token_key>
}

```

*** Response ***
```
[
    {
        "id": 1,
        "holder": "name owner 1",
        "number": "*************486",
        "brand": "visa",
        "created_at": "2023-08-21T02:11:30.960385Z",
        "updated_at": "2023-08-21T02:11:30.960446Z"
    },
]

```