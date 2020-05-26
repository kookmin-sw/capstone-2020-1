import React, { useEffect, useState } from "react";
import axios from "axios";
import { makeStyles } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";
import CircularProgress from "@material-ui/core/CircularProgress";

const useStyles = makeStyles({
  table: {
    minWidth: 650,
  },
});

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

function makeTime(str) {
  var tmpTime = str.split(":");
  // console.log(tmpTime);
  var temp =
    parseInt(tmpTime[0]) * 3600 +
    parseInt(tmpTime[1]) * 60 +
    parseInt(tmpTime[2]);
  return temp;
}

function createData(number, point, kind) {
  return { number, point, kind };
}

const Highlight = (props) => {
  const classes = useStyles();
  const [rows, setRows] = useState([]);
  const [load, setLoad] = useState(false);

  useEffect(() => {
    try {
      let temp = [];
      axios
        .get("http://13.209.112.92:8000/api/SNDhighlight", {
          headers: { "Content-Type": "multipart/form-data" },
          params: {
            url: props.url,
          },
        })
        .then((response) => {
          const data = response.data.highlight;
          // console.log(data);
          for (var i in data) {
            temp = temp.concat([[humanReadable(data[i][0]), "sound"]]);
          }
          axios
            .get("http://13.209.112.92:8000/api/chatlog_highlight", {
              headers: { "Content-Type": "multipart/form-data" },
              params: {
                url: props.url,
              },
            })
            .then((response) => {
              const data = response.data.highlight;
              // console.log(data);
              for (var i in data) {
                temp = temp.concat([[humanReadable(data[i][0]), "chat"]]);
              }
              temp.sort();
              let temprows = [];
              for (i = 0; i < 6; i++) {
                temprows = temprows.concat(
                  createData("Highlight" + (i + 1), temp[i][0], temp[i][1])
                );
              }
              setRows(temprows);
              setLoad(true);
            })
            .catch(function (error) {
              setRows([]);
            });
        })
        .catch();
    } catch (e) {
      console.log(e);
    }
  }, [props]);

  const onClick = (e) => {
    // console.log(e.point);
    if (props.platform !== "AfreecaTV") {
      props.setTime(makeTime(e.point));
      props.setCheck(true);
    }
  };

  return (
    <TableContainer component={Paper}>
      <h3 className="mt-5">Highlight Point</h3>
      {load ? (
        <Table className={classes.table} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Highlight</TableCell>
              <TableCell align="right">Point</TableCell>
              <TableCell align="right">Sound or Chat</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow
                key={row.number}
                onClick={() => {
                  onClick(row);
                }}
                hover
              >
                <TableCell component="th" scope="row">
                  {row.number}
                </TableCell>
                <TableCell align="right">{row.point}</TableCell>
                <TableCell align="right">{row.kind}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      ) : (
        <CircularProgress color="secondary" />
      )}
    </TableContainer>
  );
};

export default Highlight;
