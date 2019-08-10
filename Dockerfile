FROM python:3.6

WORKDIR /code

COPY requirements.txt /code

RUN pip install -r requirements.txt
COPY run.sh /code/

COPY build_json.py dtdd_api.py write_to_plex.py /code/
COPY apis/* /code/apis/
COPY config.py.example config.py* /code/
ENTRYPOINT ["python"]
