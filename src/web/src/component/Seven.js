import React, { useEffect, useState } from "react";
import axios from "axios";
import { Line } from "react-chartjs-2";
import { MDBContainer } from "mdbreact";

const Seven = (props) => {
  let state = {
    dataLine: {
      labels: [],
      datasets: [
        {
          label: "joy",
          fill: true,
          lineTension: 0.3,
          backgroundColor: "rgba(225, 204,230, .3)",
          borderColor: "rgb(205, 130, 158)",
          borderCapStyle: "butt",
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: "miter",
          pointBorderColor: "rgb(205, 130, 158)",
          pointBackgroundColor: "rgb(255, 255, 255)",
          pointBorderWidth: 10,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgb(0, 0, 0)",
          pointHoverBorderColor: "rgba(220, 220, 220,1)",
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: [],
        },
        {
          label: "love",
          fill: true,
          lineTension: 0.3,
          backgroundColor: "rgba(184, 185, 210, .3)",
          borderColor: "rgb(35, 26, 136)",
          borderCapStyle: "butt",
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: "miter",
          pointBorderColor: "rgb(35, 26, 136)",
          pointBackgroundColor: "rgb(255, 255, 255)",
          pointBorderWidth: 10,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgb(0, 0, 0)",
          pointHoverBorderColor: "rgba(220, 220, 220, 1)",
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: [],
        },
        {
          label: "angry",
          fill: true,
          lineTension: 0.3,
          backgroundColor: "rgba(184, 185, 210, .3)",
          borderColor: "rgb(135, 26, 136)",
          borderCapStyle: "butt",
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: "miter",
          pointBorderColor: "rgb(135, 26, 136)",
          pointBackgroundColor: "rgb(255, 255, 255)",
          pointBorderWidth: 10,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgb(0, 0, 0)",
          pointHoverBorderColor: "rgba(220, 220, 220, 1)",
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: [],
        },
        {
          label: "neutral",
          fill: true,
          lineTension: 0.3,
          backgroundColor: "rgba(184, 185, 210, .3)",
          borderColor: "rgb(135, 126, 36)",
          borderCapStyle: "butt",
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: "miter",
          pointBorderColor: "rgb(135, 126, 36)",
          pointBackgroundColor: "rgb(255, 255, 255)",
          pointBorderWidth: 10,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgb(0, 0, 0)",
          pointHoverBorderColor: "rgba(220, 220, 220, 1)",
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: [],
        },
        {
          label: "sadness",
          fill: true,
          lineTension: 0.3,
          backgroundColor: "rgba(184, 185, 210, .3)",
          borderColor: "rgb(35, 76, 36)",
          borderCapStyle: "butt",
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: "miter",
          pointBorderColor: "rgb(35, 76, 36)",
          pointBackgroundColor: "rgb(255, 255, 255)",
          pointBorderWidth: 10,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgb(0, 0, 0)",
          pointHoverBorderColor: "rgba(220, 220, 220, 1)",
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: [],
        },
        {
          label: "fear",
          fill: true,
          lineTension: 0.3,
          backgroundColor: "rgba(184, 185, 210, .3)",
          borderColor: "rgb(35, 76, 116)",
          borderCapStyle: "butt",
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: "miter",
          pointBorderColor: "rgb(35, 76, 116)",
          pointBackgroundColor: "rgb(255, 255, 255)",
          pointBorderWidth: 10,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgb(0, 0, 0)",
          pointHoverBorderColor: "rgba(220, 220, 220, 1)",
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: [],
        },
        {
          label: "surprise",
          fill: true,
          lineTension: 0.3,
          backgroundColor: "rgba(184, 185, 210, .3)",
          borderColor: "rgb(135, 176, 116)",
          borderCapStyle: "butt",
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: "miter",
          pointBorderColor: "rgb(135, 176, 116)",
          pointBackgroundColor: "rgb(255, 255, 255)",
          pointBorderWidth: 10,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgb(0, 0, 0)",
          pointHoverBorderColor: "rgba(220, 220, 220, 1)",
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: [],
        },
      ],
    },
  };
  const [test, setTest] = useState({
    labels: [],
    datasets: [
      {
        label: "joy",
        fill: true,
        lineTension: 0.3,
        backgroundColor: "rgba(225, 204,230, .3)",
        borderColor: "rgb(205, 130, 158)",
        borderCapStyle: "butt",
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: "miter",
        pointBorderColor: "rgb(205, 130, 158)",
        pointBackgroundColor: "rgb(255, 255, 255)",
        pointBorderWidth: 10,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgb(0, 0, 0)",
        pointHoverBorderColor: "rgba(220, 220, 220,1)",
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: [],
      },
      {
        label: "love",
        fill: true,
        lineTension: 0.3,
        backgroundColor: "rgba(184, 185, 210, .3)",
        borderColor: "rgb(35, 26, 136)",
        borderCapStyle: "butt",
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: "miter",
        pointBorderColor: "rgb(35, 26, 136)",
        pointBackgroundColor: "rgb(255, 255, 255)",
        pointBorderWidth: 10,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgb(0, 0, 0)",
        pointHoverBorderColor: "rgba(220, 220, 220, 1)",
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: [],
      },
      {
        label: "angry",
        fill: true,
        lineTension: 0.3,
        backgroundColor: "rgba(184, 185, 210, .3)",
        borderColor: "rgb(135, 26, 136)",
        borderCapStyle: "butt",
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: "miter",
        pointBorderColor: "rgb(135, 26, 136)",
        pointBackgroundColor: "rgb(255, 255, 255)",
        pointBorderWidth: 10,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgb(0, 0, 0)",
        pointHoverBorderColor: "rgba(220, 220, 220, 1)",
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: [],
      },
      {
        label: "neutral",
        fill: true,
        lineTension: 0.3,
        backgroundColor: "rgba(184, 185, 210, .3)",
        borderColor: "rgb(135, 126, 36)",
        borderCapStyle: "butt",
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: "miter",
        pointBorderColor: "rgb(135, 126, 36)",
        pointBackgroundColor: "rgb(255, 255, 255)",
        pointBorderWidth: 10,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgb(0, 0, 0)",
        pointHoverBorderColor: "rgba(220, 220, 220, 1)",
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: [],
      },
      {
        label: "sadness",
        fill: true,
        lineTension: 0.3,
        backgroundColor: "rgba(184, 185, 210, .3)",
        borderColor: "rgb(35, 76, 36)",
        borderCapStyle: "butt",
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: "miter",
        pointBorderColor: "rgb(35, 76, 36)",
        pointBackgroundColor: "rgb(255, 255, 255)",
        pointBorderWidth: 10,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgb(0, 0, 0)",
        pointHoverBorderColor: "rgba(220, 220, 220, 1)",
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: [],
      },
      {
        label: "fear",
        fill: true,
        lineTension: 0.3,
        backgroundColor: "rgba(184, 185, 210, .3)",
        borderColor: "rgb(35, 76, 116)",
        borderCapStyle: "butt",
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: "miter",
        pointBorderColor: "rgb(35, 76, 116)",
        pointBackgroundColor: "rgb(255, 255, 255)",
        pointBorderWidth: 10,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgb(0, 0, 0)",
        pointHoverBorderColor: "rgba(220, 220, 220, 1)",
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: [],
      },
      {
        label: "surprise",
        fill: true,
        lineTension: 0.3,
        backgroundColor: "rgba(184, 185, 210, .3)",
        borderColor: "rgb(135, 176, 116)",
        borderCapStyle: "butt",
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: "miter",
        pointBorderColor: "rgb(135, 176, 116)",
        pointBackgroundColor: "rgb(255, 255, 255)",
        pointBorderWidth: 10,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgb(0, 0, 0)",
        pointHoverBorderColor: "rgba(220, 220, 220, 1)",
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: [],
      },
    ],
  });

  const [load, setLoad] = useState(false);

  useEffect(() => {
    try {
      axios
        .get("http://13.209.112.92:8000/api/predict7", {
          headers: { "Content-Type": "multipart/form-data" },
          params: {
            url: props.url,
          },
        })
        .then((response) => {
          const data = response.data;
          // console.log(data.predict.pos);
          for (var i = 0; i < 100; i++) {
            state.dataLine.labels = state.dataLine.labels.concat(i);
            state.dataLine.datasets[0].data = state.dataLine.datasets[0].data.concat(
              data.predict.joy[i]
            );
            state.dataLine.datasets[1].data = state.dataLine.datasets[1].data.concat(
              data.predict.love[i]
            );
            state.dataLine.datasets[2].data = state.dataLine.datasets[2].data.concat(
              data.predict.anger[i]
            );
            state.dataLine.datasets[3].data = state.dataLine.datasets[3].data.concat(
              data.predict.neutral[i]
            );
            state.dataLine.datasets[4].data = state.dataLine.datasets[4].data.concat(
              data.predict.sadness[i]
            );
            state.dataLine.datasets[5].data = state.dataLine.datasets[5].data.concat(
              data.predict.fear[i]
            );
            state.dataLine.datasets[6].data = state.dataLine.datasets[6].data.concat(
              data.predict.surprise[i]
            );
          }
          for (i = 99; i > 0; i--) {
            if (
              state.dataLine.datasets[0].data[i] === 0 &&
              state.dataLine.datasets[1].data[i] === 0 &&
              state.dataLine.datasets[2].data[i] === 0 &&
              state.dataLine.datasets[3].data[i] === 0 &&
              state.dataLine.datasets[4].data[i] === 0 &&
              state.dataLine.datasets[5].data[i] === 0 &&
              state.dataLine.datasets[6].data[i] === 0
            ) {
              state.dataLine.labels.splice(i, 1);
              state.dataLine.datasets[0].data.splice(i, 1);
              state.dataLine.datasets[1].data.splice(i, 1);
              state.dataLine.datasets[2].data.splice(i, 1);
              state.dataLine.datasets[3].data.splice(i, 1);
              state.dataLine.datasets[4].data.splice(i, 1);
              state.dataLine.datasets[5].data.splice(i, 1);
              state.dataLine.datasets[6].data.splice(i, 1);
            } else {
              break;
            }
          }
          // console.log(state.dataLine);
          setTest(state.dataLine);
          setLoad(true);
        })
        .catch();
    } catch (e) {
      console.log(e);
    }
  }, [props]);

  return (
    <MDBContainer>
      <h3 className="mt-5">Seven Sentiment</h3>
      {load ? <Line data={test} options={{ responsive: true }} /> : <></>}
    </MDBContainer>
  );
};

export default Seven;
