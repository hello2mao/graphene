From ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3 python3-pip && pip3 install sklearn numpy && mkdir -p /graphene/Examples

COPY sklearn/ /graphene/Examples

CMD ["python3"]