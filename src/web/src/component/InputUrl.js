import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import axios from "axios";
import TextField from "@material-ui/core/TextField";
import { Grid } from "@material-ui/core";

const InputUrl = (props) => {
  const [url, setUrl] = useState();

  const temp = localStorage.getItem("loginStorage");

  const checkUrl = () => {
    try {
      axios
        .get("http://13.209.112.92:8000/api/analysis_url", {
          headers: { "Content-Type": "multipart/form-data" },
          params: {
            url: url,
          },
        })
        .then((response) => {
          const data = response.data;
          // console.log(data);
          if(data.result === false) {
            alert("wrong url. please, check url.");
          } else {
            props.setPlatform(data.result[0]);
            props.setVideoid(data.result[1]);
            props.setUrl(url);
            props.toggleInput(true);
          }
        })
        .catch(function (error) {
          if (error.response.status === 400) {
            alert("wrong url. please, check url.");
          }
          // console.log(error);
          
        });
    } catch (e) {
      console.log(e);
    }
  };

  const onClick = () => {
    try {
      axios
        .get("http://13.209.112.92:8000/api/login", {
          headers: { "Content-Type": "multipart/form-data" },
          params: {
            email: JSON.parse(temp).email,
            uuid: JSON.parse(temp).uuid,
          },
        })
        .then((response) => {
          const data = response.data;
          // console.log(data);
          localStorage.setItem("loginStorage", JSON.stringify(data));
          // props.toggleInput(true);
          // props.setUrl(url);
          if (props.input === true) {
            props.setPlatform();
            props.setVideoid();
            props.setUrl();
            props.toggleInput(false);
            alert("reset");
          } else {
            checkUrl();
          }
        })
        .catch(function (error) {
          if (error.response.status === 401) {
            localStorage.removeItem("loginStorage");
            props.toggleLogin(false);
            props.toggleInput(false);
            alert("please, you need sign in again.");
          }
        });
    } catch (e) {
      console.log(e);
    }
  };

  return (
    <Grid>
      <Grid
        container
        alignItems="center"
        direction="row"
        justify="center"
        style={{ paddingTop: 40, paddingBottom: 10 }}
      >
        <Grid xs={2} style={{marginRight: 20}}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            name="url"
            label="url"
            type="url"
            id="url"
            fullWidth
            onChange={(e) => {
              setUrl(e.target.value);
            }}
          />
        </Grid>
        
        <Grid>
          <Button variant="contained" color="secondary" onClick={onClick}>
            Input URL
          </Button>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default InputUrl;
