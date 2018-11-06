# Onkyo API
This is a RESTFull API for running commands on network-enabled Onkyo receivers based on [onkyo-eiscp](https://github.com/miracle2k/onkyo-eiscp) library.

# Installation
## prerequisite
- [Docker](https://www.docker.com/)

## Building

    git clone https://github.com/mtomran/onkyo-api.git
    cd onkyo-api
    docker build --rm -t onkyo-api .

## Running     

    docker run -d -it -p 8000:8000 --net=host --name onkyo onkyo-api
    
# Usage

    GET http://localhost:8000/api/v1/onkyo/<command>

example

    GET http://localhost:8000/api/v1/onkyo/power=on
    GET http://localhost:8000/api/v1/onkyo/--discover