FROM python:3.7.5-slim-stretch as base
FROM base as builder
LABEL maintainer="mike.milord@gmail.com"
ARG BUILD_DATE
ARG BUILD_VERSION

LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.version=$BUILD_VERSION
LABEL org.label-schema.docker.cmd="docker run -v ~/shorten/rest:/app/restgateway -p 5050:5050 -d milguad/shorten"

RUN apt-get update && apt-get -y install python3-pip libpq-dev python3-dev \
        && pip3 install --upgrade pip \
        && apt-get -y install manpages manpages-dev \
        bzip2 file xz-utils build-essential python3-setuptools strace \
        python3-wheel \
        && rm -rf /var/lib/apt/lists/* \
        && pip install --upgrade pip

# Create the virtualenv
RUN python3 -m venv /opt/venv
# Make sure we use the virtualenv: (activate it)
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM base 
COPY --from=builder /opt/venv /opt/venv
COPY . /app/restgateway
WORKDIR /app/restgateway
## to make the boot.sh executable
RUN chmod a+x boot.sh
## below required to use the flask command
ENV FLASK_APP app.py

# expose port
EXPOSE 5050

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
ENTRYPOINT ["./boot.sh"]