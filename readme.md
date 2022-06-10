## How to run this django-react boilerplate code

Make sure that you have `docker` and `docker-compose` installed.

locate the directory with `docker-compose.yaml` file in the project. and from there run the following command:

`docker-compose up`

backend server will be expose on `localhost:8000` and react app will be available in on `localhost:3000`

The source code directories are added as volumes in docker containers so whatever change you do while running the dockerized apps, will be available after the container ends as well.