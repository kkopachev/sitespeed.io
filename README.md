# sitespeed.io

To run everything first thing you need to do is to build go-carbon and carbonapi:
```
./build.sh
```
This will create statically-linked binaries in `/carbon/dist` and `/carbonapi/dist`.
 
Then to run everything locally:
 1. run `docker-compose up -d` (make sure you run the [latest Docker compose](https://docs.docker.com/compose/install/) version)
 2. Run sitespeed to get some metrics: 
 ```
    docker-compose run sitespeed.io urls.txt \
        -c cable \
        -b chrome \
        --video \
        --speedIndex \
        --html.showAllWaterfallSummary true \
        --graphite.host=carbon
 ```
 3. Access the dashboard: [http://localhost:3000](http://localhost:3000). In grafana change datasource's host to `graphite-web:8000` and disable basic auth 
 4. When you are done you can shutdown and remove all the docker containers by running `docker-compose down -v && docker-compose rm`
 
Note: sitespeed.io assumes that carbon and graphite-web run on the same host, so annotations would not work as expected.
 