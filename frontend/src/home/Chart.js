import React, { PureComponent } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const data = [ // example
  {
    "Open": 382.5833435058594,
    "High": 400.3566589355469,
    "Low": 378.67999267578125,
    "Close": 399.9266662597656,
    "Adj Close": 399.9266662597656,
    "Volume": 103931400
  },
  {
    "Open": 396.51666259765625,
    "High": 402.6666564941406,
    "Low": 374.3500061035156,
    "Close": 383.1966552734375,
    "Adj Close": 383.1966552734375,
    "Volume": 100248300
  },
  {
    "Open": 382.2166748046875,
    "High": 390.11334228515625,
    "Low": 360.336669921875,
    "Close": 362.7066650390625,
    "Adj Close": 362.7066650390625,
    "Volume": 80119800
  },
  {
    "Open": 359,
    "High": 362.6666564941406,
    "Low": 340.1666564941406,
    "Close": 354.8999938964844,
    "Adj Close": 354.8999938964844,
    "Volume": 90336600
  },
  {
    "Open": 360.1233215332031,
    "High": 360.30999755859375,
    "Low": 336.6666564941406,
    "Close": 342.32000732421875,
    "Adj Close": 342.32000732421875,
    "Volume": 84164700
  },
  {
    "Open": 333.3333435058594,
    "High": 353.0333251953125,
    "Low": 326.6666564941406,
    "Close": 352.7066650390625,
    "Adj Close": 352.7066650390625,
    "Volume": 91815000
  },
  {
    "Open": 351.22332763671875,
    "High": 358.6166687011719,
    "Low": 346.2733459472656,
    "Close": 354.79998779296875,
    "Adj Close": 354.79998779296875,
    "Volume": 66063300
  },
  {
    "Open": 359.6166687011719,
    "High": 371.61334228515625,
    "Low": 357.5299987792969,
    "Close": 368.739990234375,
    "Adj Close": 368.739990234375,
    "Volume": 83739000
  },
  {
    "Open": 369.69000244140625,
    "High": 371.8666687011719,
    "Low": 342.17999267578125,
    "Close": 343.85333251953125,
    "Adj Close": 343.85333251953125,
    "Volume": 97209900
  },
  {
    "Open": 339.9599914550781,
    "High": 350.6666564941406,
    "Low": 337.7933349609375,
    "Close": 349.8699951171875,
    "Adj Close": 349.8699951171875,
    "Volume": 72924300
  },
];

export default class Chart extends PureComponent {
  static demoUrl = 'https://codesandbox.io/s/simple-line-chart-kec3v';

  render() {
    return (
      <LineChart
      width={700}
      height={400}
      data={data}
      margin={{
        top: 5,
        right: 30,
        left: 20,
        bottom: 5
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line
        type="monotone"
        dataKey="Close"
        stroke="#8884d8"
        activeDot={{ r: 8 }}
      />
      {/* <Line type="monotone" dataKey="uv" stroke="#82ca9d" /> */}
    </LineChart>
    );
  }
}
