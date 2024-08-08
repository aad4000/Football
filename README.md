pip install -r requirements.txt

to run the application: 
python index.py

first pull mysql from docker hub 
then use this command : docker run --name mysql-container --network football_network -e MYSQL_ROOT_PASSWORD=Ali.ali. -e MYSQL_DATABASE=football -p 3307:3306 -d mysql:latest
after that build your flask by using this :  docker build -t flask-container .
then run it  : docker run --name flask-container --network football_network -p 5000:5000 -d football_flask_app
check active docker conatainers: docker logs <name of the file>

