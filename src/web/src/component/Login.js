import React, { useState } from "react";
import axios from "axios";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import SignUp from "./SignUp";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogTitle from "@material-ui/core/DialogTitle";

const useStyles = makeStyles((theme) => ({
  paper: {
    // marginTop: theme.spacing(8),
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

  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };
  const onClick = () => {
    let frd = new FormData();
    frd.append("email", email);
    frd.append("pw", password);
    try {
      axios
        .post("http://13.209.112.92:8000/api/login", frd, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
        })
        .then((response) => {
          const data = response.data;
          // console.log(data);
          localStorage.setItem("loginStorage", JSON.stringify(data));
          props.setEmail(email);
          props.setName(data.name);
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
    <div>
      <Typography
        variant="h6"
        style={{
          textTransform: "none",
          color: "black",
          marginLeft: 20,
          marginRight: 30,
        }}
        onClick={handleClickOpen}
      >
        Sign in
      </Typography>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="form-dialog-title"
      >
        <DialogTitle id="form-dialog-title">Sign in</DialogTitle>
        <Container component="main" maxWidth="xs">
          <CssBaseline />
          <div className={classes.paper}>
            <form className={classes.form} noValidate>
              <Typography component="h7" variant="h7">
                If you want to use YOBA service Please, Sign in
              </Typography>
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
              <Typography component="h7" variant="h7">
                First visiting? please, sign up.
              </Typography>
              <SignUp></SignUp>
            </form>
          </div>
        </Container>
        <DialogActions>
            <Button onClick={handleClose} color="secondary" autoFocus>
              Cancel
            </Button>
          </DialogActions>
      </Dialog>
    </div>
  );
};

export default Login;
