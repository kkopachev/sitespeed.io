FROM scratch

EXPOSE 2003 2003/udp 2004 7002 7007 8080
VOLUME /data/graphite/whisper/

COPY dist/go-carbon /bin/go-carbon


ENTRYPOINT ["go-carbon"]
CMD ["--help"]

COPY carbon.conf .
COPY storage-schemas.conf /data/graphite/schemas.conf
COPY storage-aggregation.conf /data/graphite/aggregation.conf
