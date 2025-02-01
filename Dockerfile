ARG MELTANO_IMAGE=meltano/meltano:latest-python3.12
FROM $MELTANO_IMAGE

WORKDIR /project


COPY . /project
RUN meltano install

RUN apt-get update && apt-get install -y tzdata

ENV TZ="America/Sao_Paulo"

ENV MELTANO_PROJECT_READONLY=1

EXPOSE 5000

ENTRYPOINT ["meltano"]
