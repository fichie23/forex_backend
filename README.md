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
