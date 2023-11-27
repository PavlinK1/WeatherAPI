FROM ubuntu:20.04
ENV  DEBIAN_FRONTEND=noninteractive
# Template for http_proxy and https_proxy - Use if needed!
# ENV http_proxy=
# ENV https_proxy=
WORKDIR /app
COPY .  /app
RUN apt-get update && apt-get upgrade -y && apt-get install -y  \
    python3                                                     \
    python3-pip                                                 \
    sqlite3                                                     \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install requests              \
&&  chmod +x weather-request.py        \
&&  chmod +x weather-db-unittest.py