/*eslint-disable*/
import React from "react";
import PropTypes from "prop-types";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import ListItem from "@material-ui/core/ListItem";
import List from "@material-ui/core/List";
// core components
import styles from "../../assets/jss/material-dashboard-react/components/footerStyle.js";

import iot_logo from "../../components/images/iot_logo.jpg";

const useStyles = makeStyles(styles);

export default function Footer(props) {
  const classes = useStyles();
  return (
    <footer className={classes.footer}>
      <div className={classes.container}>
        <p className={classes.right}>
          <span className="footer-img">
          </span>
          <span className="footer-text">IOT Project , Hochschule Rhein-Waal University &copy; {1900 + new Date().getYear()}{" "}</span>
        </p>
      </div>
    </footer>
  );
}
