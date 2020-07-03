import React, { Component } from "react";

// react plugin for creating charts
import ChartistGraph from "react-chartist";
// @material-ui/core
import { makeStyles } from "@material-ui/core/styles";
import Icon from "@material-ui/core/Icon";
// @material-ui/icons
import Store from "@material-ui/icons/Store";
import Warning from "@material-ui/icons/Warning";
import DateRange from "@material-ui/icons/DateRange";
import LocalOffer from "@material-ui/icons/LocalOffer";
import Update from "@material-ui/icons/Update";
import ArrowUpward from "@material-ui/icons/ArrowUpward";
import AccessTime from "@material-ui/icons/AccessTime";
import Accessibility from "@material-ui/icons/Accessibility";
import BugReport from "@material-ui/icons/BugReport";
import Code from "@material-ui/icons/Code";
import Cloud from "@material-ui/icons/Cloud";
// core components
import GridItem from "./Grid/GridItem.js";
import GridContainer from "./Grid/GridContainer.js";
import Table from "./Table/Table.js";
import Tasks from "./Tasks/Tasks.js";
import CustomTabs from "./CustomTabs/CustomTabs.js";
import Danger from "./Typography/Danger.js";
import Card from "./Card/Card.js";
import CardHeader from "./Card/CardHeader.js";
import CardIcon from "./Card/CardIcon.js";
import CardBody from "./Card/CardBody.js";
import CardFooter from "./Card/CardFooter.js";

import Temperature from "./temperatur.jsx";
import Pressure from "./pressure.jsx";
import Humidity from "./humidity.jsx";
import Clock from "./clock.jsx";
import TempGraph from "./Graphs/temperatureGraph.jsx";
import PressureGraph from "./Graphs/pressureGraph.jsx";
import HumidityGraph from "./Graphs/humidityGraph.jsx";
// import { bugs, website, server } from "./variables/general.js";

import axios from "axios";
import { FETCH_LIVEDATA_URL } from "./Constant/constants.jsx";

const serverUrl = FETCH_LIVEDATA_URL;
const http = axios.create({ baseUrl: serverUrl });

class FetchData extends Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 10,
      temperature: "fetching...",
      pressure: "fetching...",
      humidity: "fetching...",
      modifiedTime: "fetching...",
    };
    //console.log("inside constructor");
  }

  componentDidMount() {
    const getLiveData = () => {
      console.log("GetLiveData function is called.");
      const { counter } = this.state;
      //console.log(counter);
      const info = { counter: counter };
      axios
        .get(serverUrl)
        .then((response) => this.updateState(response.data))
        .catch((err) => console.log(err));
    };
    this._interval = window.setInterval(getLiveData, 5000);
  }

  updateState(resdata) {
    // console.log(resdata)
    this.setState({ counter: resdata.counter });
    this.setState({ temperature: resdata.temperature.value });
    this.setState({ pressure: resdata.pressure.value });
    this.setState({ humidity: resdata.humidity.value });
    this.setState({ modifiedTime: resdata.createdTime });
  }

  render() {
    const data = this.state;
    //console.log(data);
    return (
      <div>
        {" "}
        <GridContainer>
          <GridItem xs={12} sm={6} md={3}>
            <Temperature data={data} />
          </GridItem>
          <GridItem xs={12} sm={6} md={3}>
            <Pressure data={data} />
          </GridItem>
          <GridItem xs={12} sm={6} md={3}>
            <Humidity data={data} />
          </GridItem>
          <GridItem xs={12} sm={6} md={3}>
            <Clock data={data} />
          </GridItem>
        </GridContainer>
        <GridContainer>
          <GridItem xs={12} sm={12} md={8}>
            <Card chart>
              <CardHeader color="success">
                <TempGraph />
              </CardHeader>
              <CardBody>
                <h4>Temperature Graph</h4>
              </CardBody>
            </Card>
          </GridItem>
          <GridItem xs={12} sm={12} md={8}>
            <Card chart>
              <CardHeader color="warning">
                <PressureGraph />
              </CardHeader>
              <CardBody>
                <h4>Pressure Graph</h4>
              </CardBody>
            </Card>
          </GridItem>
          <GridItem xs={12} sm={12} md={8}>
            <Card chart>
              <CardHeader color="danger">
                <HumidityGraph />
              </CardHeader>
              <CardBody>
                <h4>Humidity Graph</h4>
              </CardBody>
            </Card>
          </GridItem>
        </GridContainer>
      </div>
    );
  }
}

export default FetchData;
