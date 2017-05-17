FROM golang:1.8 as builder
RUN go get -d -v github.com/dgryski/carbonapi && \
    GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -a --installsuffix cgo --ldflags="-s" github.com/dgryski/carbonapi

FROM alpine:latest
COPY --from=builder /go/carbonapi /bin/carbonapi

EXPOSE 8080

ENTRYPOINT ["/bin/carbonapi"]
CMD ["-v"]
