#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

buildBinary() {
    DIRECTORY=$1
    PACKAGE=$2

    echo "Building $PACKAGE"

    docker run --rm -it -v "$DIRECTORY/dist":/app -w /app golang:1.8 \
    sh -c "go get $PACKAGE && GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -a --installsuffix cgo --ldflags=\"-s\" $PACKAGE"
}

buildBinary "$DIR/carbon" "github.com/lomik/go-carbon"

