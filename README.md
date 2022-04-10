This project is developed using FastAPI and SQLAlchemy

Kindly setup the project using the _requirements_ file.
Then using any asgi server like uvicorn this app can be spin-up using below command.

`uvicorn app.main:app --reload`

This REST-API documentation can be found by navigating to the Home url of the application.
`http://127.0.0.1:8000/` or `http://127.0.0.1:8000/docs`

A docker image can also be built using the below command and the present Dockerfile:
`docker build -t fastapi_application_image .` 

Run a container using the below command:
`docker run --name fastapi_service_container -p 80:80 fastapi_application_image`
