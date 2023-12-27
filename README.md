### step 0 - cleanup everything
#### docker stop $(docker ps -a -q)
#### docker rm $(docker ps -a -q)
#### docker network rm askme-network

### step 1 - copy project
#### copy the project to your local system

### step 2 - build from the project directory
#### docker build . -t askme:latest

### step 3 - create a network
#### docker network create askme-network

### step 4 - run UI Application
#### docker run --name askme -p 8080:8080 --network askme-network askme:latest

### Step 5 - use the app
#### open url http://localhost:8080

<hr>

### step 6 - run My SQL
#### docker run --name mysql --privileged -e GRANT_SUDO=yes --user root --network askme-network -p 3306:3306 -e MYSQL_ROOT_PASSWORD=abc --restart unless-stopped mysql

### step 7 - copy the script to SQL container
#### sudo docker cp /Users/mubarak/Documents/deck/ML/ml_demos/LLM/mysqlsampledatabase.sql 141b253b9656:/

### step 8 - get into the sql container
#### docker exec -it 8b8a101bf869 /bin/bash

### step 9 - run mysql inside the container
#### mysql -u root -p abc

### step 10 - import database
#### source mysqlsampledatabase.sql

### step 11 - check the db, there should be a new db called classicmodels 
#### show databases;

