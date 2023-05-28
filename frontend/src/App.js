import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomeTemplate from './home/HomePage.js';
import LoginPage from './login/LoginPage.js'

function App() {
  return (
  <Router>
    <Routes>
        <Route path="/" element={<HomeTemplate />} />
        <Route path="/login" element={<LoginPage />} />
    </Routes>
  </Router>
  );
}

export default App;