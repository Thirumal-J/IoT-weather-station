import React, { Component } from "react";
import { Card, CardContent, Grid, Typography, Avatar } from "@material-ui/core";

class Clock extends Component {
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
                Last Updated
              </Typography>
              <Typography
                variant="h4"
                style={{
                  fontSize: "30px",
                  fontWeight: "bold",
                  padding: "10px",
                }}
              >
                {" "}
                {this.props.data.modifiedTime}{" "}
              </Typography>
            </Grid>
            <Grid item style={{ backgroundColor: "grey" }}></Grid>
          </Grid>
        </CardContent>
      </Card>
    );
  }
}

export default Clock;
