import React, { Component } from "react";
import { Card, CardContent, Grid, Typography, Avatar } from "@material-ui/core";
//import MoneyIcon from '@material-ui/icons/Money';
import { makeStyles } from "@material-ui/styles";
import celsius from "./images/celsius.png";
//import dashboard from './dashboard.css';

class Temperature extends Component {
  constructor(props) {
    super(props);
    // console.log(props);
    //this.state = {counter: this.props.counter};
  }

  render() {
    return (
      <Card>
        <CardContent>
          <Grid>
            <Grid item>
              <Typography
                className="fontWeight:200"
                color="textSecondary"
                gutterBottom
                variant="body2"
                style={{ fontWeight: "bold" }}
              >
                Temperature
              </Typography>
              <Typography
                variant="h3"
                style={{
                  fontSize: "40px",
                  fontWeight: "bold",
                  padding: "10px",
                }}
              >
                {this.props.data.temperature}
              </Typography>
            </Grid>
            <Grid item>
              <Avatar
                className="backgroundColor: theme.palette.error.main, height: 80, width: 80"
                src={celsius}
                alt="degree Celsius"
              >
                {this.props.data.unit}
              </Avatar>
            </Grid>
          </Grid>
        </CardContent>
      </Card>
    );
  }
}

export default Temperature;
