import React, { Component } from "react";
import { Card, CardContent, Grid, Typography, Avatar } from "@material-ui/core";
import MoneyIcon from "@material-ui/icons/Money";
import { makeStyles } from "@material-ui/styles";
import humidity from "./images/humidity.jpg";

class Humidity extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Card>
        <CardContent>
          <Grid>
            <Grid item>
              <Typography
                className="fontWeight: 700"
                color="textSecondary"
                gutterBottom
                variant="body2"
                style={{ fontWeight: "bold" }}
              >
                Humidity
              </Typography>
              <Typography
                variant="h3"
                style={{
                  fontSize: "40px",
                  fontWeight: "bold",
                  padding: "10px",
                }}
              >
                {this.props.data.humidity}
              </Typography>
            </Grid>
            <Grid item>
              <Avatar
                className="backgroundColor: theme.palette.error.main, height: 100, width: 100"
                src={humidity}
                alt="%"
              ></Avatar>
            </Grid>
          </Grid>
        </CardContent>
      </Card>
    );
  }
}

export default Humidity;
