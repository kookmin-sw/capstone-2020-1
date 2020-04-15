import { AppBar, Grid, Typography } from "@material-ui/core";
import React from "react";
import YobaLogo from "../yoba_logo.png";

const NaviBar = () => {
  return (
    <AppBar position="sticky" color="default">
      <Grid
        container
        alignItems="center"
        direction="row"
        justify="space-between"
        style={{ paddingTop: 10, paddingBottom: 10 }}
      >
        <Grid xs={2}>
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
        <Grid xs={8}>
          <img alt="logo" src={YobaLogo} height="80px" />
        </Grid>
        <Grid xs={2}>
          <Grid container direction="row">
            <Typography
              variant="h8"
              style={{
                textTransform: "none",
                color: "black",
                marginLeft: 20,
                marginRight: 20,
              }}
            >
              About
            </Typography>
            <Typography
              variant="h8"
              style={{
                textTransform: "none",
                color: "black",
                marginLeft: 20,
                marginRight: 30,
              }}
            >
              Sign In
            </Typography>
          </Grid>
        </Grid>
      </Grid>
    </AppBar>
  );
};

export default NaviBar;
