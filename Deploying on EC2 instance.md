# Streamlit app Docker Image

## 1. Login with your AWS console and launch an EC2 instance
## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone "your-project"
```

```bash
docker build -t miguelhermar/streamlit_app_test:latest .
```

```bash
docker images -a  
```

```bash
docker run -d -p 8501:8501 miguelhermar/streamlit_app_test
```
-d for dettach mode: if you close the terminal it will keep running


```bash
docker ps  
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login 
```

```bash
docker push docker push miguelhermar/streamlit_app_test:latest 
```

```bash
docker rmi miguelhermar/streamlit_app_test:latest
```

```bash
docker pull miguelhermar/streamlit_app_test:latest 
```






