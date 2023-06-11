import axios from 'axios';
import React, { useState } from 'react';
import './Prediction.css';

function Prediction() {
  const [stock, setStock] = useState('');
  const [days, setDays] = useState('');

  const handleStock = (e) => {
    setStock(e.target.value);
  };

  const handleDays = (e) => {
    setDays(e.target.value);
  };

  const predictAction = () => {
      axios.post('http://localhost:8000/predict', {
          stock: stock,
          days: days,
      }) 
      .then((response) => {
          // success
          console.log('예측 요청');
      })
      .catch((error) => {
          // error
          console.log('요청 실패');
      })
  }

  return (
    <div className="page2">
      <div className="contentWrap2">
        <div className="inputWrap2">
          <input
            className="input2"
            type="text"
            placeholder="종목"
            value={stock}
            onChange={handleStock}
          />
        </div>
        <div className="inputWrap2">
          <input
            className="input2"
            type="text"
            placeholder="예측 일 수"
            value={days}
            onChange={handleDays}
          />
        </div>
      </div>

      <div>
        <button className="bottomButton2" onClick={()=>{
            predictAction();
        }}>
          예측하기
        </button>
      </div>
    </div>
  );
}
export default Prediction;