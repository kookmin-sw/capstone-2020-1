import { Grid, Link, Typography, Box } from "@material-ui/core";
import React, { useState } from "react";
import Navibar from "../component/Navibar";
import Description from "../component/Description";
import InputUrl from "../component/InputUrl";
import Login from "../component/Login";

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {"Copyright © "}
      <Link color="inherit" href="https://material-ui.com/">
        Yoba
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

const MainPage = () => {
  


  return (
    <div>
      <Grid>
        <Navibar />
      </Grid>
      <Grid>
        <Description />
      </Grid>
      <Grid>
        <Login />
      </Grid>
      <Grid>
        <InputUrl></InputUrl>
      </Grid>
      <Box mt={8}>
        <Copyright />
      </Box>
    </div>
  );
};

export default MainPage;
