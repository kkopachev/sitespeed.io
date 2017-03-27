FROM python:2

ENV PYTHONPATH="/opt/graphite/lib/:/opt/graphite/webapp/"

RUN apt-get update \
    && apt-get install -y python-dev libcairo2-dev libffi-dev \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir gunicorn scandir \
         https://github.com/graphite-project/graphite-web/tarball/1.0.0-pre1 \
         https://github.com/graphite-project/whisper/tarball/1.0.0-pre1 \
    && apt-get clean\
    && rm -rf /root/.cache /var/lib/apt/lists/*


COPY graphite.wsgi /wsgi.py
COPY local_settings.py /opt/graphite/webapp/graphite/local_settings.py

EXPOSE 8080

ENV CLUSTER_SERVERS="carbon:8080"

VOLUME /opt/graphite/storage

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "wsgi"]
