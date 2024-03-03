FROM python:3.11

# # Directory in container for all project files
ENV DOCKYARD_SRVHOME=etl
# Copy application source code to SRCDIR
COPY . $DOCKYARD_SRVHOME/

WORKDIR $DOCKYARD_SRVHOME/src/

RUN apt-get --allow-releaseinfo-change update && \
    apt-get -y --no-install-recommends install apt-utils build-essential libpq-dev python3-dev \
    openjdk-11-jre g++ python3-dev &&  apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

ARG PYPI_USER=
ARG PYPI_PASSWORD=
ENV PYPI_USER=$PYPI_USER
ENV PYPI_PASSWORD=$PYPI_PASSWORD

RUN pip3 install -r ../requirements.txt

RUN chmod +x ../docker-entrypoint.sh
ENTRYPOINT ["../docker-entrypoint.sh"]