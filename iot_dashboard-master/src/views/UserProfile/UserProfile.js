import React from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import InputLabel from "@material-ui/core/InputLabel";
// core components
import GridItem from "../../components/Grid/GridItem.js";
import GridContainer from "../../components/Grid/GridContainer.js";
import CustomInput from "../../components/CustomInput/CustomInput.js";
import Button from "../../components/CustomButtons/Button.js";
import Card from "../../components/Card/Card.js";
import CardHeader from "../../components/Card/CardHeader.js";
import CardAvatar from "../../components/Card/CardAvatar.js";
import CardBody from "../../components/Card/CardBody.js";
import CardFooter from "../../components/Card/CardFooter.js";

import senseHat from "../../assets/img/sensehat3.png";

const styles = {
  cardCategoryWhite: {
    color: "rgba(255,255,255,.62)",
    margin: "0",
    fontSize: "14px",
    marginTop: "0",
    marginBottom: "0"
  },
  cardTitleWhite: {
    color: "#FFFFFF",
    marginTop: "0px",
    minHeight: "auto",
    fontWeight: "300",
    fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
    marginBottom: "3px",
    textDecoration: "none"
  },
  senseHatStyle: {
    height:"200px",
    align:"middle"
  }
};

const useStyles = makeStyles(styles);

export default function UserProfile() {
  const classes = useStyles();
  return (
    <div>
      <GridContainer>
        <GridItem xs={12} sm={12} md={8}>
          <Card>
            <CardHeader color="rose">
              <h4 className={classes.cardTitleWhite}>Abstract</h4>
              <p className={classes.cardCategoryWhite}></p>
            </CardHeader>
            <CardBody>
            <p>This IoT based Project aims to display the current humidity, temperature, and pressure parameters on the internet server using Raspberry Pi. This project is based on IoT and it functions as a weather monitoring station. It measures the humidity, pressure, and temperature of the environment.</p>
            <p>Raspberry Pi 3 is being used here along with sensehat to measure the temperature, pressure, and humidity.</p>
            <p>MQTT(MQ Telemetry Transport) is a network-based messaging protocol. It is used to establish a publisher-subscriber network protocol to capture the live data using the sensors mounted with the hardware and publish the data as message queues.</p>
            <p>Flask python and database Postgres is used as part of the backend. The client application is a react application.</p>
            <p>The microservice architecture in this project helps to interact with various components. The message queues from the MQTT broker can be subscribed by a backend microservice to fetch the live data and update the database.</p>
            <p>A live data microservice which routes the data subscribed from the MQTT broker to the react application is in place. There are different microservices to fetch the weekly and the last 24 hours of data from the database. This is to plot the graph for the temperature, pressure, and humidity in the react application.</p>
            <p>The client application dashboard is developed to display the live monitoring of the weather forecast. Also, to display a graphical view of the last 24hours and weekly data of temperature, pressure, and humidity.
The server configuration for this project is done in docker containers along with web configurations.</p>
            </CardBody>
            <CardFooter>
            </CardFooter>
          </Card>
        </GridItem>
        <GridItem>
          <Card profile>
            <CardAvatar senseHat>
            </CardAvatar>
            <CardHeader color="rose">
              <h4 className={classes.cardTitleWhite}>Hardware Setup</h4>
            </CardHeader>
            <CardBody senseHat>
              <img  className={classes.senseHatStyle} src={senseHat} alt="hardware setup" />
            </CardBody>
          </Card>
        </GridItem>
      </GridContainer>
    </div>
  );
}
