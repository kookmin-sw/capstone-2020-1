import React, { useState } from "react";
import { Grid, Button } from "@material-ui/core";
import ViewerReact from "./ViewerReact";
import Highlight from "./Highlight";
import ViewerRank from "./ViewerRank";

const Result = (props) => {
  return (
    <div>
      <h3>Analysis results of {props.url}</h3>
      <Grid container>
        <Grid xs={6}>
          <ViewerReact></ViewerReact>
        </Grid>
        <Grid xs={6}>
          <ViewerRank></ViewerRank>
        </Grid>
      </Grid>
      <Grid container>
        <Highlight></Highlight>
      </Grid>
      <Grid>
        <h3>Audio standardization</h3>
        <Button
          variant="contained"
          color="secondary"
        >
          Download
        </Button>
      </Grid>
    </div>
  );
};

export default Result;
