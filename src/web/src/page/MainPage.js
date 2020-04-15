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
  const [email, setEmail] = useState();
  const [login, togleLogin] = useState(false);
  console.log(email)
  return (
    <div>
      <Grid>
        <Navibar email={email} login={login}/>
      </Grid>
      <Grid>
        <Description />
      </Grid>
      {/* <Grid>
        <Login setEmail={setEmail} togleLogin={togleLogin}/>
      </Grid>
      <Grid>
        <InputUrl></InputUrl>
      </Grid> */}
      {login?  <InputUrl></InputUrl>:<Login setEmail={setEmail} togleLogin={togleLogin}/>}
      <Box mt={8}>
        <Copyright />
      </Box>
    </div>
  );
};

export default MainPage;
