import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import { Grid } from "@material-ui/core";

const InputUrl = (props) => {
  const [url, setUrl] = useState();

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
            onChange = {(e)=> {setUrl(e.target.value)}}
          />
        </Grid>
        <Grid>
          <Button
            variant="contained"
            color="secondary"
            onClick={() => {
              props.toggleInput(true); props.setUrl(url);
            }}
          >
            Input URL
          </Button>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default InputUrl;
