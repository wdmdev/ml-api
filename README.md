# MLapi

Learning containerization of ML model with Docker and Flask.

Just one of my own projects for fun and learning during my free time.

You might need to run sudo infront of the docker commands for administrator rights.

To build with Docker

```bash
docker build -t <your docker image name> .
```

To run with Docker

```bash
docker run -d -p  <your pc port>:<image port> <your docker image name>
```

for example:

```bash
docker build -t mlapi
```

and run with

``` bash
docker run -rm -d -p 5000:5001 mlapi
```

-d makes the process run as a background process (daemon) ans -p maps the pc port to the container port for communication with the api.

See running docker containers

``` bash
docker container list
```

Stop running docker container

```bash
docker stop <CONTAINER ID>
```

Get the CONTAINER ID from the docker container list command.