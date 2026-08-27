FROM python:3.12-alpine3.24

WORKDIR /lab

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    sudo \
    vim \
    curl && \
    rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
