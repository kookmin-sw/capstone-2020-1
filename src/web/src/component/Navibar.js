import { AppBar, Grid, Typography } from "@material-ui/core";
import React from "react";
import YobaLogo from "../yoba_logo.png";

const NaviBar = (props) => {
  // console.log(props.email)
  const logout = () => {
    if (props.login === true) {
      localStorage.removeItem("loginStorage");
      props.toggleLogin(false);
      props.toggleInput(false);
      alert("sign out");
    } else {
      alert("Please, sign in from the bottom page.")
    }
  };
  const onClick = () => {
    if (props.login === true) {
      alert("welcome");
    }
  }

  return (
    <AppBar position="sticky" color="default">
      <Grid
        container
        alignItems="center"
        direction="row"
        justify="center"
        style={{ paddingTop: 10, paddingBottom: 10 }}
      >
        <Grid xs={1}>
          <Typography
            variant="h6"
            style={{
              textTransform: "none",
              color: "black",
              marginLeft: 20,
              marginRight: 20,
            }}
          >
            YOBA
          </Typography>
        </Grid>
        <Grid xs={2}></Grid>

        <Grid xs={6}>
          <img alt="logo" src={YobaLogo} height="80px" />
        </Grid>

        <Grid xs = {2}>
          <Typography
            variant="h6"
            style={{
              textTransform: "none",
              color: "black",
              marginLeft: 20,
              marginRight: 30,
            }}
            onClick={onClick}
          >
            {props.login ? "Welcome! " + props.email : ""}
          </Typography>
        </Grid>
        <Grid xs = {1}>
          <Typography
            variant="h6"
            style={{
              textTransform: "none",
              color: "black",
              marginLeft: 20,
              marginRight: 30,
            }}
            onClick={logout}
          >
            {props.login ? "Sign out" : "Sign in"}
          </Typography>
        </Grid>
      </Grid>
    </AppBar>
  );
};

export default NaviBar;
