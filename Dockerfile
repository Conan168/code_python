FROM python:3.12-alpine3.24

WORKDIR /lab

RUN apk add --no-cache \
    sudo \
    vim \
    curl \
    bash

CMD ["/bin/bash"]
