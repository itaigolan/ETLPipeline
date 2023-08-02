run: 
	sudo docker-compose build && docker-compose up -d

post:
	curl -X POST -H HTTP/1.1 "localhost:5000"

get:
	curl -X GET -H HTTP/1.1 "localhost:5000"
