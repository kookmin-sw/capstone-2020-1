import {
    Grid,
    Typography,
} from '@material-ui/core';
import React from 'react';
import {makeStyles} from '@material-ui/core/styles';

const login = require('../flaticon/login.png');
const url = require('../flaticon/url.png');
const analysis = require('../flaticon/analysis.png');
const edit = require('../flaticon/edit.png');
const a= require('../flaticon/a.png');
const b= require('../flaticon/b.png');
const c= require('../flaticon/c.png');
const d= require('../flaticon/d.png');

const next = require('../flaticon/next.png');

const img_style = {width:128,height:128}
const arrow_style = {width:64,height:64,marginLeft:20,marginRight:20}
const img_info_style = {width:192,height:192,marginLeft:20,marginRight:20}

const useStyles = makeStyles((theme) => ({
    root: {
        alignItems: 'center',
        justifyContent: 'center',
        textAlign: 'center',
        height: 200,
        width: '100%',
    },
}));

const Usage =()=> {
    const classes = useStyles();

    return (
        <div>
        <Grid container className={classes.root} spacing={3}>
            <img src={login} style={img_style}/>
            <img src={next} style={arrow_style}/>

            <img src={url} style={img_style}/>
            <img src={next} style={arrow_style}/>

            <img src={analysis} style={img_style}/>
            <img src={next} style={arrow_style}/>

            <img src={edit} style={img_style}/>
        </Grid>
        <Grid container className={classes.root} spacing={3}>
            <img src={a} style={img_info_style}/>

            <img src={b} style={img_info_style}/>

            <img src={c} style={img_info_style}/>

            <img src={d} style={img_info_style}/>
        </Grid>
        </div>
    );

}
  
export default Usage;