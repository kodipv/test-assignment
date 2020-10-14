FROM python:3.7.4

ARG user=uwsgi
ARG group=uwsgi
RUN groupadd ${group}
RUN useradd --home-dir /home/${user} -g ${group} ${user}

ENV LANG=ru_RU.UTF-8 \
    LANGUAGE=ru_RU.UTF-8

RUN apt-get update -y \
    && apt-get install -y \
    libsasl2-dev \
    python-dev \
    libssl-dev \
    python3-dev \
    libpcre3-dev

ENV CONFIG_LEVEL docker
ENV PROJECT_ROOT /usr/app/src
ENV PYTHONPATH "${PYTHONPATH}:${PROJECT_ROOT}"

RUN mkdir -p ${PROJECT_ROOT}
COPY ./src/ ${PROJECT_ROOT}
COPY ./requirements.txt ${PROJECT_ROOT}
WORKDIR ${PROJECT_ROOT}

RUN pip install -r requirements.txt

EXPOSE 3000

CMD [ "uwsgi", "--ini", "uwsgi.ini"]
