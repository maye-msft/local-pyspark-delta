# local-pyspark-delta

## Git clone

```text
git clone https://github.com/maye-msft/local-pyspark-delta /path/to/local-pyspark-delta
```

## Build image

```text
docker build . -t my-pyspark:0.0.1
```

## Build container and enter  it

```text
docker run -it -v /path/to/local-pyspark-delta:/app --name=pyspark my-pyspark:0.0.1 bash
```

## Run a test

```text
cd /app/tests
pytest
```

## Save container

```text
docker stop pyspark
docker commit github-local-pyspark-delta pyspark_container_image
docker save pyspark_container_image | gzip > pyspark_container_image.tar.gz
```

## Clone container in another machine and enter  it

```text
docker load -i pyspark_container_image.tar.gz
docker run -it -v /path/to/local-pyspark-delta:/app --name=pyspark pyspark_container_image bash
```

## Run a test again

```text
cd /app/tests
pytest
```

## Notes

### Re-enter a stopped container

```text
docker start pyspark
docker exec -it pyspark bash
```

### An exception

When reading a not existing folder of delta, the following error will occurr.

```text
java.lang.IllegalArgumentException: argument "src" is null
        at com.fasterxml.jackson.databind.ObjectMapper._assertNotNull(ObjectMapper.java:4757)
        at com.fasterxml.jackson.databind.ObjectMapper.readValue(ObjectMapper.java:3489)
        at org.apache.spark.sql.delta.DeltaThrowableHelper$.<init>(DeltaThrowableHelper.scala:53)
        at org.apache.spark.sql.delta.DeltaThrowableHelper$.<clinit>(DeltaThrowableHelper.scala)
```
