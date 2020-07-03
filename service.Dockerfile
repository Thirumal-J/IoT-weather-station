FROM python:latest
#Install git
RUN apt-get update   
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone    
WORKDIR /backend
COPY requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt
COPY app /backend/app
COPY start-service.sh /backend/start-service.sh
EXPOSE 4001-4004
RUN ["chmod", "+x", "/backend/start-service.sh"]
ENTRYPOINT ["/backend/start-service.sh"]