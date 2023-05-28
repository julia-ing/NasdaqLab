import axios from 'axios';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';


export default function Login() {
    const [nickname, setNickname] = useState('');
    const [pw, setPw] = useState('');

    const handleNickname = (e) => {
        setNickname(e.target.value);
    };

    const handlePw = (e) => {
      setPw(e.target.value);
    };

    const replace = useNavigate();

    const loginAction = () => {
       axios.post('http://localhost:8000/login', {
           nickname: nickname,
           password: pw,
       }) 
       .then((response) => {
           // success
           console.log('로그인 성공');
           console.log('user', response.data.nickname);
           console.log('token', response.data.access_token);
           localStorage.setItem('token', response.data.access_token);
           replace("/");
       })
       .catch((error) => {
           // error
           console.log('로그인 실패');
       })
    }

    return (
      <div className="page">
        <div className="titleWrap">
          로그인
        </div>

        <div className="contentWrap">
          <div className="inputTitle">닉네임</div>
          <div className="inputWrap">
            <input
              className="input"
              type="text"
              placeholder="닉네임을 입력해주세요."
              value={nickname}
              onChange={handleNickname}
            />
          </div>

          <div style={{ marginTop: "26px" }} className="inputTitle">
            비밀번호
          </div>
          <div className="inputWrap">
            <input
              className="input"
              type="password"
              placeholder="영문, 숫자, 특수문자 포함 8자 이상"
              value={pw}
              onChange={handlePw}
            />
          </div>
        </div>

        <div>
          <button className="bottomButton" onClick={()=>{
              loginAction();
          }}>
            확인
          </button>
        </div>
      </div>
    );
}
