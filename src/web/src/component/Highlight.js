import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles({
  table: {
    minWidth: 650,
  },
});

function createData(name, calories, fat, carbs) {
  return { name, calories, fat, carbs };
}

const rows = [
  createData('Highlight 1', '18:00', '19:00', 'chat'),
  createData('Highlight 2', '28:00', '29:00', 'sound'),
  createData('Highlight 3', '38:00', '39:00', 'chat'),
  createData('Highlight 4', '48:00', '49:00', 'chat'),
  createData('Highlight 5', '58:00', '59:00', 'sound'),
];

export default function Highlight() {
  const classes = useStyles();

  return (
    <TableContainer component={Paper}>
       <h3 className="mt-5">Highlight Point</h3>
      <Table className={classes.table} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Highlight</TableCell>
            <TableCell align="right">Point Start</TableCell>
            <TableCell align="right">Point End</TableCell>
            <TableCell align="right">Sound or Chat</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.name}>
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.calories}</TableCell>
              <TableCell align="right">{row.fat}</TableCell>
              <TableCell align="right">{row.carbs}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
