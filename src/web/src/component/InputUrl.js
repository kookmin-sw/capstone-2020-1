import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import axios from "axios";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import { Grid } from "@material-ui/core";

const InputUrl = (props) => {
  const [url, setUrl] = useState();

  const temp = localStorage.getItem("loginStorage");

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
          console.log(data);
          props.toggleInput(true);
          props.setUrl(url);
        })
        .catch(function (error) {
          if (error.response.status === 401) {
            props.toggleLogin(false);
            alert("please, you need sign in again.");
          }
        });
    } catch (e) {
      console.log(e);
    }
  };

  // const onClick = () => {
  //   try {
  //     axios
  //       .get("http://localhost:8000/api/login", {
  //         headers: { "Content-Type": "multipart/form-data" },
  //         params: {
  //           email: JSON.parse(temp).email,
  //           uuid: JSON.parse(temp).uuid,
  //         },
  //       })
  //       .then((response) => {
  //         const data = response.data;
  //         console.log(data);
  //         props.toggleInput(true);
  //         props.setUrl(url);
  //       })
  //       .catch(function (error) {
  //         if (error.response.status === 401) {
  //           props.toggleLogin(false);
  //           alert("please, you need sign in again.");
  //         }
  //       });
  //   } catch (e) {
  //     console.log(e);
  //   }
  // };

  return (
    <Grid>
      <Grid
        container
        alignItems="center"
        direction="row"
        justify="center"
        style={{ paddingTop: 10, paddingBottom: 10 }}
      >
        <Grid xs={2}>
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
