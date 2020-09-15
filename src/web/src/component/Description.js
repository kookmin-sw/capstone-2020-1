import {
    Grid,
    Typography,
} from '@material-ui/core';
import React from 'react';
import {makeStyles} from '@material-ui/core/styles';

const backgroundImg = require('../backgroundImage.png');

const useStyles = makeStyles((theme) => ({
    root: {
        backgroundImage: `url(${backgroundImg})`,
        alignItems: 'center',
        color: 'white',
        backgroundSize: 'cover',
        // color: "textPrimary",
        justifyContent: 'center',
        textAlign: 'center',
        height: 400,
        width: '100%',
    },
}));

const Description =()=> {
    const classes = useStyles();
    return (
        <Grid container className={classes.root} spacing={3}>
            <Grid xs={12}>
                <Typography variant='h2' gutterBottom>
                    YOBA
                </Typography>
                <Typography variant='h3' gutterBottom>
                    Highlight editing assist tool for Creator
                </Typography>
            </Grid>
        </Grid>
);
}
  
export default Description;