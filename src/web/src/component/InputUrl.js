import React from "react";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import { Grid } from "@material-ui/core";

const InputUrl = () => {
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
          />
        </Grid>
        <Grid>
          <Button type="submit" variant="contained" color="secondary">
            URL 입력 완료
          </Button>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default InputUrl;
