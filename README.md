# Weather CLI
![color picker](weather-api.gif)
### Description
The Weather CLI is an application that provides weather information for cities worldwide. \
It utilizes the Weatherbit API under its free plan, which allows up to 50 requests per day.

### Installing

* **Install docker:**
```bash
sudo apt install docker-ce docker-ce-cli containerd.io
```
_Note: If you are under proxy modify the Dockerfile with the corresponding template \
for http_proxy and https_proxy and uncomment it, this is needed for installing \
python requests package, otherwise delete both of the proxy envirables._

* **Create image:**
```bash
docker build -t <IMAGE_NAME:TAG> .
```
* **Start container instance from the image:**
```bash
docker run -d --name <CONTAINER_NAME> <IMAGE_NAME:TAG> tail -f /dev/null
```
* **Examples for above commands:**
```bash
docker build -t weather_service:01 .
docker run -d --name docker-01 weather_service:01 tail -f /dev/null
```
### Execute the service

* **Execute databese unit tests script:**
```bash
sudo docker exec -it <CONTAINER_NAME> sh -c "python3 weather-db-unittest.py"
```
* **Execute weather script:**

_Note: You will be asked to enter city name. It should be with Capital letter - Sofia for example)_
```bash
sudo docker exec -it <CONTAINER_NAME> sh -c "python3 weather-request.py"
```

* **Check the data from json log**
```bash
sudo docker exec -it <CONTAINER_NAME> sh -c "cat weather_data.log"
```


* **Start sqlite3 instance:**
```bash
sudo docker exec -it <CONTAINER_NAME> sh -c "sqlite3 weather_data.db"
```

* **Examples for above commands:**
```bash
sudo docker exec -it docker-01 sh -c "python3 weather-db-unittest.py"
sudo docker exec -it docker-01 sh -c "python3 weather-request.py"
sudo docker exec -it docker-01 sh -c "cat weather_data.log"
sudo docker exec -it docker-01 sh -c "sqlite3 weather_data.db"
```

* **Select query:**
```bash
  SELECT * FROM weather;
```

* **Quit the sqlite3 instance:**
```bash
.quit
```