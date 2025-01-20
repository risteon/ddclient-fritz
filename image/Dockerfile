FROM ubuntu:24.04
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
  ddclient \
  iproute2 \
  curl \
  libio-socket-ssl-perl \
  ca-certificates \
  python3-full \ 
  python3-pip \
  && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /fritzconnection
RUN /fritzconnection/bin/python -m pip install fritzconnection

COPY ddclient_entrypoint.sh .
CMD [ "./ddclient_entrypoint.sh" ]
