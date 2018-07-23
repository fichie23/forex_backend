# forex_backend

## Prerequisites ##

### Docker

I used docker for development and deployment as well. To install docker on your machine with specific OS you can follow steps explained [here](https://docs.docker.com/install/)

## How to Run

Build the image first

```
$ docker build -t forex:latest .
```

Run container

```
$ docker run -d --name forex_api -p 8000:8000 forex:latest
```

## How to Test

Execute command below, make sure your container name `forex_api` is the correct target
```
$ docker exec -it forex_api python manage.py test
```

### API Documentation

You can find the API docs [here](https://github.com/fichie23/forex_backend/blob/master/docs/APIDocs.md)
