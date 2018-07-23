# forex_backend

## Prerequisites ##

### Docker

I used docker for development and deployment as well. To install docker on your machine with specific OS you can follow steps explained [here](https://docs.docker.com/install/)

## How to Run

Run using `docker-compose`, there will be 2 containers running, api and postgresql container. Two ports should be available before running the docker, port 8000 for api using default django port and port 5432 for postgres port

```
$ docker-compose up
```

## How to Test

Execute command below, make sure your container name `forex_api` is the correct target
```
$ docker exec -it forex_backend_api_1 python manage.py test

```

### API Documentation

You can find the API docs [here](https://github.com/fichie23/forex_backend/blob/master/docs/APIDocs.md)


### Database Documentation

You can find explanation about Database design documentation [here](https://github.com/fichie23/forex_backend/blob/master/docs/DBDocs.md)
