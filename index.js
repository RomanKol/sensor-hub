import {exec} from "node:child_process";
import express from 'express'
import morgan from 'morgan'

function getSensorData() {
  return new Promise((resolve, reject) => {
    exec('python3 ./sensor/hub.py', (error, stdout) => {
      if(error) reject(error);

      resolve(JSON.parse(stdout));
    })
  })
}

const app = express();
app.use(morgan('combined'));

app.listen(80, () => {
  console.log('Listen on port 80!');
});

app.get('/data', async (req, res) => {
  const data = await getSensorData();
  res.json(data);
});

app.get('/data/:prop', async (req, res) => {
  const data = await getSensorData();

  const {prop} = req.params;

  if(!data.hasOwnProperty(prop)) {
    return res.status(404).json({
      status: 404,
      message: `Not Found! The requested resoruce \`${prop}\` does not exist`,
    });
  }

  res.json(data[prop]);
});