import React, { useState } from "react";
import { Grid, Button } from "@material-ui/core";
import ViewerReact from "./ViewerReact";
import Highlight from "./Highlight";
import ViewerRank from "./ViewerRank";
import clsx from "clsx";
import { makeStyles } from "@material-ui/core/styles";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";

const useStyles = makeStyles({
  root: {
    "&:hover": {
      backgroundColor: "transparent",
    },
  },
  icon: {
    borderRadius: "50%",
    width: 16,
    height: 16,
    boxShadow:
      "inset 0 0 0 1px rgba(16,22,26,.2), inset 0 -1px 0 rgba(16,22,26,.1)",
    backgroundColor: "#f5f8fa",
    backgroundImage:
      "linear-gradient(180deg,hsla(0,0%,100%,.8),hsla(0,0%,100%,0))",
    "$root.Mui-focusVisible &": {
      outline: "2px auto rgba(19,124,189,.6)",
      outlineOffset: 2,
    },
    "input:hover ~ &": {
      backgroundColor: "#ebf1f5",
    },
    "input:disabled ~ &": {
      boxShadow: "none",
      background: "rgba(206,217,224,.5)",
    },
  },
  checkedIcon: {
    backgroundColor: "#137cbd",
    backgroundImage:
      "linear-gradient(180deg,hsla(0,0%,100%,.1),hsla(0,0%,100%,0))",
    "&:before": {
      display: "block",
      width: 16,
      height: 16,
      backgroundImage: "radial-gradient(#fff,#fff 28%,transparent 32%)",
      content: '""',
    },
    "input:hover ~ &": {
      backgroundColor: "#106ba3",
    },
  },
});

// Inspired by blueprintjs
function StyledRadio(props) {
  const classes = useStyles();

  return (
    <Radio
      className={classes.root}
      disableRipple
      color="default"
      checkedIcon={<span className={clsx(classes.icon, classes.checkedIcon)} />}
      icon={<span className={classes.icon} />}
      {...props}
    />
  );
}

const Result = (props) => {
  const [posAndNeg, setPosAndNeg] = useState(false);
  const [keword, setKeyword] = useState(false);

  const dashboad = (e) => {
    // console.log(e.target.value);
    console.log(props);
    if (e.target.value === "posAndNeg") {
      setPosAndNeg(true);
      setKeyword(false);
    } else if (e.target.value === "keword") {
      setPosAndNeg(false);
      setKeyword(true);
    } else {
      setPosAndNeg(false);
      setKeyword(false);
    }
  };

  return (
    <div>
      <h3>Analysis results of {props.url}</h3>
      <FormControl component="fieldset">
        <FormLabel component="legend">Options</FormLabel>
        <RadioGroup
          aria-label="options"
          name="customized-radios"
          onChange={dashboad}
        >
          <FormControlLabel
            value="posAndNeg"
            control={<StyledRadio />}
            label="positive & negative"
          />
          <FormControlLabel
            value="keword"
            control={<StyledRadio />}
            label="keword10"
          />
          <FormControlLabel
            value="other"
            control={<StyledRadio />}
            label="Other"
          />
        </RadioGroup>
      </FormControl>

      <Grid container>
        {posAndNeg ? (
          <Grid xs={12}>
            <ViewerReact></ViewerReact>
          </Grid>
        ) : (
          <></>
        )}
        {keword ? (
          <Grid xs={12}>
            <ViewerRank
              platform={props.platform}
              videoid={props.videoid}
            ></ViewerRank>
          </Grid>
        ) : (
          <></>
        )}
      </Grid>

      <Grid container>
        <Highlight
          platform={props.platform}
          videoid={props.videoid}
          url={props.url}
        ></Highlight>
      </Grid>
      <Grid>
        <h3>Audio standardization</h3>
        <Button variant="contained" color="secondary">
          Download
        </Button>
      </Grid>
    </div>
  );
};

export default Result;
