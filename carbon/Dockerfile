FROM golang:1.8 as builder
RUN go get -d -v github.com/lomik/go-carbon && \
    GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -a --installsuffix cgo --ldflags="-s" github.com/lomik/go-carbon

FROM alpine:latest
WORKDIR /root/
COPY --from=builder /go/go-carbon /root/go-carbon

EXPOSE 2003 2003/udp 2004 7002 7007 8080
VOLUME /data/graphite/whisper/

ENTRYPOINT ["/root/go-carbon"]
CMD ["--help"]

COPY carbon.conf .
COPY storage-schemas.conf /data/graphite/schemas.conf
COPY storage-aggregation.conf /data/graphite/aggregation.conf
