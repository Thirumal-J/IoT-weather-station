# MIC-Weather

1) Clone or download the project using the github link
2) In your local, use command line and change directory to MIC-Weather folder
3) Run the following command: pip install -r requirements.txt 
  (All the required packages has been mentioned in this text file)
4) Run the following services to make the backend server up:
    a) python .\app\controllers\livedata_controller.py
    b) python .\app\controllers\temperature_controller.py
    c) python .\app\controllers\pressure_controller.py
    d) python .\app\controllers\humidity_controller.py
    e) python .\app\mqtt\mqtt_client_handler.py
    
    All these are microservices, so it should be live and running, then only you can access all the APIs.

NOTE:-
Since postgres maynot be available in your system, pressure microservice might not work, but other databases are part of the project, all other services will work as expected.
Will update further for the changes related to pressure microservice.

API DETAILS:

https://drive.google.com/file/d/1yz5QTghhUQ9B08QfM4rf7Ixc8GOt2jQm/view?usp=sharing

1) Download Postman, an easy app to test the backend APIs.
2) Download the above mentioned file from the drive and import it into your postman and check the functionality of the services.

