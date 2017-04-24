to test: 
```bash
./build.sh
docker-compose up --build
# in separate window:
curl -v 'http://localhost:8080/metrics/find/?format=json&query=carbon.agents.*.*'
```

docker-compose stores whisper files in a volume. After restarting `docker-compose down; docker-compose up` given `curl` command will return some results.
Removing the volume will bring back original behavior: nothing is returned - `docker-compose down -v; docker-compose up` 