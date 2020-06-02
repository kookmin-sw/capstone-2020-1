import {
    Grid,
    Typography,
} from '@material-ui/core';
import React from 'react';
import {makeStyles} from '@material-ui/core/styles';

const backgroundImg = require('../Usage.png');

const useStyles = makeStyles((theme) => ({
    root: {
        backgroundImage: `url(${backgroundImg})`,
        alignItems: 'center',
        color: 'white',
        backgroundSize: 'cover',
        // color: "textPrimary",
        justifyContent: 'center',
        textAlign: 'center',
        height: 700,
        width: '100%',
    },
}));

const Usage = (props) => {
    const classes = useStyles();

    if(props.login === false)
        return null;

    return (
        <Grid container className={classes.root} spacing={3}>
            <Grid xs={12}>
                <Typography variant='h3' gutterBottom>
                    Usage
                </Typography>
                <Typography variant='h5' gutterBottom>
                    <br/>1. 하단 URL을 입력하는 곳에 풀영상의 URL을 입력합니다.
                </Typography>
                <Typography variant='h7' gutterBottom>
                    - 지원하는 Platform : ①AfreecaTV ②Twitch ③Youtube <br/>
                    - 해당 URL에는 반드시 채팅로그가 포함되어 있어야 합니다.
                </Typography>
                <Typography variant='h5' gutterBottom>
                    <br/>2. input URL 버튼을 누르고 검사 결과를 기다립니다.
                </Typography>
            </Grid>
        </Grid>
    );

}
  
export default Usage;