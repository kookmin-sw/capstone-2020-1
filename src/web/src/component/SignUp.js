import React, { useState } from "react";
import axios from "axios";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

const checkEmail = (str) => {
  var reg_email = /^([0-9a-zA-Z_\.-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}$/;
  if (!reg_email.test(str)) {
    return false;
  } else {
    return true;
  }
};

const SignUp = () => {
  const classes = useStyles();
  const [open, setOpen] = useState(false);
  const [alertOpen, setAlertOpen] = useState(false);
  const [alertMessage, setAlertMessage] = useState();
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();
  const [check, setCheck] = useState();
  const [name, setName] = useState();
  const [age, setAge] = useState();
  const [success, setSuccess] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const closeAlert = () => {
    if (success) {
      setOpen(false);
      setAlertOpen(false);
    } else {
      setAlertOpen(false);
    }
  };

  const singUp = () => {
    if (!checkEmail(email)) {
      setAlertMessage("wrong email");
      setAlertOpen(true);
    } else if (password !== check && password !== undefined) {
      setAlertMessage("wrong checkPassword");
      setAlertOpen(true);
    } else if (isNaN(age)) {
      setAlertMessage("wrong age");
      setAlertOpen(true);
    } else {
      try {
        let frd = new FormData();
        frd.append("email", email);
        frd.append("pw", password);
        frd.append("name", name);
        frd.append("age", age);
        axios
          .post("http://localhost:8000/api/signup", frd, {
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
          })
          .then((response) => {
            if (response.status === 200) {
              setAlertMessage("success");
              setSuccess(true);
              setAlertOpen(true);
            }
            return true;
          })
          .catch(function (error) {
            if (error.response.status === 409) {
              setAlertMessage("You can't use this Email");
              setAlertOpen(true);
            }
          });
      } catch (e) {
        console.log(e);
      }
    }
  };

  return (
    <div>
      <Button
        fullWidth
        variant="contained"
        color="secondary"
        className={classes.submit}
        onClick={handleClickOpen}
      >
        SIGN UP
      </Button>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="form-dialog-title"
      >
        <DialogTitle id="form-dialog-title">Sign Up</DialogTitle>
        <DialogContent>
          Please enter Email.
          <TextField
            autoFocus
            onChange={(e) => {
              setEmail(e.target.value);
            }}
            margin="dense"
            id="email"
            label="Email Address"
            type="email"
            fullWidth
          />
          <DialogContentText></DialogContentText>
          Please enter password
          <TextField
            autoFocus
            onChange={(e) => {
              setPassword(e.target.value);
            }}
            margin="dense"
            id="password"
            label="Password"
            type="password"
            fullWidth
          />
          <TextField
            autoFocus
            onChange={(e) => {
              setCheck(e.target.value);
            }}
            margin="dense"
            id="check"
            label="Password Check"
            type="password"
            fullWidth
          />
          <DialogContentText></DialogContentText>
          Please enter your name
          <TextField
            autoFocus
            onChange={(e) => {
              setName(e.target.value);
            }}
            margin="dense"
            id="name"
            label="Name"
            type="name"
            fullWidth
          />
          <DialogContentText></DialogContentText>
          Please enter your age
          <TextField
            autoFocus
            onChange={(e) => {
              setAge(Number(e.target.value));
            }}
            margin="dense"
            id="age"
            label="Age"
            type="integer"
            fullWidth
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="secondary">
            Cancel
          </Button>
          <Button onClick={singUp} color="secondary">
            Sign Up
          </Button>
        </DialogActions>
      </Dialog>
      {alertOpen ? (
        <Dialog
          open={alertOpen}
          onClose={() => {
            setAlertOpen(false);
          }}
          aria-labelledby="alert-dialog-title"
          aria-describedby="alert-dialog-description"
        >
          <DialogTitle id="alert-dialog-title">
            {"Check your sing up info"}
          </DialogTitle>
          <DialogContent>
            <DialogContentText id="alert-dialog-description">
              {alertMessage}
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button onClick={closeAlert} color="primary" autoFocus>
              Check
            </Button>
          </DialogActions>
        </Dialog>
      ) : (
        <></>
      )}
    </div>
  );
};
export default SignUp;
