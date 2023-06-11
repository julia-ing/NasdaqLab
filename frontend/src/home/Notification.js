import axios from 'axios';
import React, { useState, useEffect } from 'react';
import './Notification.css';

const WS_URL = "ws://localhost:8000/ws";

const NotiItem = (props) => {
  return (
    <div className='notification'>
      {props.noti.days}일치 {props.noti.stock} 주식에 대한 예측 주가의 평균: {props.noti.predicted_val}
    </div>
  );
};

const NotiList = (props) => {
  return (
      <div>
          {props.notis.map(noti => (
              <NotiItem key={noti.timestamp}  noti={noti} />
          ))}
      </div>
  );
};

function Notification() {

  const [websocket, _] = useState(new WebSocket(WS_URL));
  const [result, setResult] = useState([]);

  useEffect(() => {
    websocket.onmessage = (event) => {
      const payload = JSON.parse(event.data);
      console.log(payload)
      setResult(payload);
    };
  }, [websocket]);

  return (
    <NotiList notis={result} />
  );
}
export default Notification;