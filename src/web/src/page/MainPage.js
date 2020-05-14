import { Grid, Link, Typography, Box } from "@material-ui/core";
import React, { useState } from "react";
import axios from "axios";
import Navibar from "../component/Navibar";
import Description from "../component/Description";
import InputUrl from "../component/InputUrl";
import Login from "../component/Login";
import Result from "../component/Result";

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
  const [login, toggleLogin] = useState(false);
  const [input, toggleInput] = useState(false);
  const [platform, setPlatform] = useState();
  const [videoid, setVideoid] = useState();
  const [url, setUrl] = useState();

  const temp = localStorage.getItem("loginStorage");

  const test = () => {
    try {
      axios
        .get("http://localhost:8000/api/login", {
          headers: { "Content-Type": "multipart/form-data" },
          params: {
            email: JSON.parse(temp).email,
            uuid: JSON.parse(temp).uuid,
          },
        })
        .then((response) => {
          const data = response.data;
          console.log(data);
          localStorage.setItem("loginStorage", JSON.stringify(data));
          setEmail(JSON.parse(temp).email);
          toggleLogin(true);
        })
        .catch();
    } catch (e) {
      console.log(e);
    }
  };

  return (
    <div onLoad={test}>
      <Grid>
        <Navibar email={email} login={login} />
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
      {login ? (
        <InputUrl
          toggleInput={toggleInput}
          setUrl={setUrl}
          toggleLogin={toggleLogin}
          setPlatform={setPlatform}
          setVideoid={setVideoid}
        ></InputUrl>
      ) : (
        <Login setEmail={setEmail} toggleLogin={toggleLogin} />
      )}

      {input & login ? (
        <Result url={url} platform={platform} videoid={videoid}></Result>
      ) : (
        <></>
      )}
      <Box mt={8}>
        <Copyright />
      </Box>
    </div>
  );
};

export default MainPage;
