import React, { useState, useEffect } from "react";
import axios from "axios";
import { Pie } from "react-chartjs-2";
import { MDBContainer } from "mdbreact";
import { Button } from "@material-ui/core";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";



function humanReadable(seconds) {
  var pad = function (x) {
    return x < 10 ? "0" + x : x;
  };
  return (
    pad(parseInt(seconds / (60 * 60))) +
    ":" +
    pad(parseInt((seconds / 60) % 60)) +
    ":" +
    pad(seconds % 60)
  );
}

const ViewerRank = (props) => {
  const [load, setLoad] = useState(false);
  const [test, setTest] = useState({
    labels: [],
    datasets: [
      {
        data: [],
        backgroundColor: [
          "#F7464A",
          "#46BFBD",
          "#FDB45C",
          "#949FB1",
          "#4D5360",
          "#AC64AD",
          "#F7464A",
          "#46BFBD",
          "#FDB45C",
          "#949FB1",
        ],
        hoverBackgroundColor: [
          "#FF5A5E",
          "#5AD3D1",
          "#FFC870",
          "#A8B3C5",
          "#616774",
          "#DA92DB",
          "#FF5A5E",
          "#5AD3D1",
          "#FFC870",
          "#A8B3C5",
        ],
      },
    ],
  });

  let state = {
    dataPie: {
      labels: [],
      datasets: [
        {
          data: [],
          backgroundColor: [
            "#F7464A",
            "#46BFBD",
            "#FDB45C",
            "#949FB1",
            "#4D5360",
            "#AC64AD",
            "#F7464A",
            "#46BFBD",
            "#FDB45C",
            "#949FB1",
          ],
          hoverBackgroundColor: [
            "#FF5A5E",
            "#5AD3D1",
            "#FFC870",
            "#A8B3C5",
            "#616774",
            "#DA92DB",
            "#FF5A5E",
            "#5AD3D1",
            "#FFC870",
            "#A8B3C5",
          ],
        },
      ],
    },
  };
  const [keywordList, setKeywordList] = useState([]);
  const [timeList, setTimeList] = useState([[[]]]);
  const [alertOpen, setAlertOpen] = useState(false);
  const [alertMessage, setAlertMessage] = useState();

  const closeAlert = () => {
    setAlertOpen(false);
  };

  useEffect(() => {
    // console.log(props);
    try {
      axios
        .get("http://13.209.112.92:8000/api/chatlog", {
          headers: { "Content-Type": "multipart/form-data" },
          params: {
            platform: props.platform,
            videoid: props.videoid,
          },
        })
        .then((response) => {
          const data = response.data;
          var list = [];
          var tList = [];
          for (var i = 0; i < 10; i++) {
            state.dataPie.labels = state.dataPie.labels.concat(
              data.keyword[i][0]
            );
            state.dataPie.datasets[0].data = state.dataPie.datasets[0].data.concat(
              data.keyword[i][1]
            );
            list = list.concat(data.keyword[i][0]);
            tList = tList.concat([data.keyword[i][2]]);
          }

          setTimeList(tList);
          setTest(state.dataPie);
          setKeywordList(list);
          setLoad(true);
        })
        .catch();
    } catch (e) {
      console.log(e);
    }
  }, [props]);

  const showAlert = (e) => {
    // console.log(e);
    setAlertOpen(true);
    var temp = "";
    for (var i = 0; i < timeList[e].length; i++) {
      temp += humanReadable(timeList[e][i][0]) + " ~ " + humanReadable(timeList[e][i][1]) + ',   \n';
    }
    // console.log(temp);
    setAlertMessage(temp);
  };

  const ButtonList = keywordList.map((test, index) => (
    <>
      <Button
        margin-right="10px"
        variant="contained"
        color="secondary"
        key={index}
        onClick={() => showAlert(index)}
      >
        {" "}
        {test}{" "}
      </Button>{" "}
    </>
  ));

  return (
    <div>
      <MDBContainer>
        <h3 className="mt-5">Keyword Rank</h3>
        {load ? (
          <Pie data={test} options={{ responsive: true }}></Pie>
        ) : (
          <div></div>
        )}
        <h3 className="mt-5">Check Time</h3>
        {ButtonList}
        <div></div>
      </MDBContainer>
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
            {"Appearing section"}
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

export default ViewerRank;
