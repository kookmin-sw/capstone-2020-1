import { AppBar, Grid, Typography } from "@material-ui/core";
import React, { useState } from "react";
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
  return (
    <AppBar position="sticky" color="default">
      <Grid
        container
        alignItems="center"
        direction="row"
        justify="space-between"
        style={{ paddingTop: 10, paddingBottom: 10 }}
      >
        <Grid>
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
        <Grid>
          <img alt="logo" src={YobaLogo} height="80px" />
        </Grid>
        <Grid>
          <Grid container direction="row">
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
              {props.login ? props.email + "님 환영합니다." : "Sign In"}
            </Typography>
          </Grid>
        </Grid>
      </Grid>
    </AppBar>
  );
};

export default NaviBar;
