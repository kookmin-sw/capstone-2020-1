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
        style={{ paddingTop: 3, paddingBottom: 3}}
      >
        <Grid xs={1}>
          <Typography
            variant="h6"
            className="Navyoba"
          >
            YOBA
          </Typography>
        </Grid>
        <Grid xs={2}></Grid>

        <Grid xs={6}>
          <img alt="logo" src={YobaLogo} height="70px" />
        </Grid>

        <Grid xs = {2}>
          <Typography
            variant="h6"
            className="Navsign_url"
            onClick={onClick}
          >
            {props.login ? "Welcome! " + props.name : ""}
          </Typography>
        </Grid>
        <Grid xs = {1}>
          <Typography
            variant="h6"
            className="Navsign_main"
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
