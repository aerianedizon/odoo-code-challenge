## odoo-code-challenge
  This the repository for the 24 hour code challenge in Python Odoo.

# Odoo Installation


## Requirements
 - Docker
     - [Ubuntu Linux](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
     - [Windows](https://docs.docker.com/docker-for-windows/install/)
 - Docker-compose
     - Linux: `sudo apt install docker-compose` 
     - Windows: already installed with Docker Desktop


## Getting Started
  
  ### Notes
  * Make sure you have sufficient free diskspace on your partition, recommendation around 2GB. Running docker-compose will eventually download 1.2GB at the minimum.

  * Make sure you have installed `docker` and `docker-compose` in your system

  ### Steps
  1. Create the following folder structure:
  odoo/
  |----> addons/
            |----> clone this repository here
  |----> enterprise/
            |----> clone the following repository here: `https://gitlab.com/wdmsyf/odoo-13-enterprise-modules`
  |----> config/
            |----> `odoo.conf`
  |----> `Dockerfile`
  |----> `docker-compose.yml`
  2. Contents of odoo.conf is as follows:
  ```
  [options]
  addons_path = /mnt/enterprise, /mnt/extra-addons
  data_dir = /var/lib/odoo
  ```
  3. Content of Dockerfile is as follows:
  ```
  From odoo:13.0
  USER root

  RUN pip3 install -U pip
  RUN pip3 install oauth2
  # password_security module
  RUN python3 -m pip install -U zxcvbn
  # auto_backup module
  RUN python3 -m pip install -U pysftp
  ```
  4. Contents of docker-compose.yml is as follows:
  ```
  version: '2'
  services:
    web:
      build: .
      #image: odoo:13.0
      depends_on:
        - db
      #command: odoo -d <database_name> -u all
      ports:
        - "8069:8069"
      volumes:
        - odoo-web-data:/var/lib/odoo
        - ./config:/etc/odoo
        - ./enterprise:/mnt/enterprise
        - ./addons/odoo-code-challenge:/mnt/extra-addons
    db:
        image: postgres:10
      ports:
        - "5432:5432"
      environment:
        - POSTGRES_DB=postgres
        - POSTGRES_PASSWORD=odoo
        - POSTGRES_USER=odoo
        - PGDATA=/var/lib/postgresql/data/pgdata
      volumes:
        - odoo-db-data:/var/lib/postgresql/data/pgdata
  volumes:
    odoo-web-data:
    odoo-db-data:
  ```
  5. Open up terminal on the working directory `cd odoo`
  6. execute `docker-compose up -d`
  7. Open your browser: `localhost:8069`


## Updating Modules
  1. Modify `docker-compose.yml` file
  2. Add the command line following line
  ```yml
  services:
  web:
    image: odoo:13.0
    depends_on:
      - db
    command: odoo -d <DB_NAME> -u <MODULE_NAME>
    ports:
      - "8069:8069"
  ``` 

## Docker Commands

  1. If Dockerfile has changed, need to rebuild the docker container:
     `docker-compose up --build`

  2. If docker-compose.yml file has changed, need to exec:
     `docker-compose up`
     Optional parameter is -d for detach if you don't want to see the logs: `docker-compose up -d`

  3. If only Odoo/UHH Modules or code has changed, just pull latest source code and restart the Odoo docker container. No need to exec docker-compose up.
     Here's the command: `docker-compose restart web`

