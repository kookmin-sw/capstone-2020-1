import React from "react";
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

export default function FormDialog() {
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Button
        // type="submit"
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
          <DialogContentText>
            To use to this website, please enter your information for sign up.
          </DialogContentText>
          Please enter ID that you want to use it and check it.
          <TextField
            autoFocus
            margin="dense"
            id="id"
            label="ID"
            type="id"
            fullWidth
          />
          <Button
            // variant="contained"
            color="secondary"
            className={classes.submit}
            onClick={handleClickOpen}
          >
            check
          </Button>
          <DialogContentText></DialogContentText>
          Please enter Email.
          <TextField
            autoFocus
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
            margin="dense"
            id="password"
            label="Password"
            type="password"
            fullWidth
          />
          <TextField
            autoFocus
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
          <Button onClick={handleClose} color="secondary">
            Sign Up
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
