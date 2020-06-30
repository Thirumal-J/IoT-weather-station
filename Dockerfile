FROM python:latest
#Install git
RUN apt-get update        
RUN apt-get install -y git
WORKDIR /MIC-Weather-master
COPY requirements.txt /MIC-Weather-master/requirements.txt
RUN pip install -r requirements.txt
COPY app /MIC-Weather-master/app
COPY start.sh /MIC-Weather-master/start.sh
EXPOSE 4001-4004
RUN ["chmod", "+x", "/MIC-Weather-master/start.sh"]
ENTRYPOINT ["/MIC-Weather-master/start.sh"]