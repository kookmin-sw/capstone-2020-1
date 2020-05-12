import React, { useState } from "react";
import axios from "axios";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import SignUp from "./SignUp";

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

const Login = (props) => {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();
  const classes = useStyles();
  
  const onClick = () => {
    let frd = new FormData();
    frd.append("email", email);
    frd.append("pw", password);

    try {
      axios
        .post("http://localhost:8000/api/login", frd, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
        })
        .then((response) => {
          const data = response.data;
          // console.log(data);

          localStorage.setItem("loginStorage", JSON.stringify(data));
          props.toggleLogin(true);
          return true;
        })
        .catch(function (error) {
          if (error.response.status === 400) {
            props.toggleLogin(false);
            alert("wrong information");
          }
          if (error.response.status === 404) {
            props.toggleLogin(false);
            alert("wrong id or pw");
          }
        });
    } catch (e) {
      console.log(e);
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Typography component="h1" variant="h5">
          If you want to use YOBA service <br />
          Please, Sign in
        </Typography>
        <form className={classes.form} noValidate>
          <TextField
            onChange={(e) => {
              setEmail(e.target.value);
            }}
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="email"
            autoFocus
          />
          <TextField
            onChange={(e) => {
              setPassword(e.target.value);
            }}
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
          />
          <Button
            // type="submit"
            fullWidth
            variant="contained"
            color="secondary"
            className={classes.submit}
            onClick={onClick}
          >
            Sign In
          </Button>
          First visiting? please, sign up.
          <SignUp></SignUp>
        </form>
      </div>
    </Container>
  );
};

export default Login;
