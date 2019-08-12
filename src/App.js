import React from 'react';
import fbLogo from './assets/fbLogo.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <button className="facebookButton">
        <img 
          className="facebookLogo"
          src={fbLogo}
          alt="fucc the zucc" 
        />
        
        Flush Facebook
      </button>
    </div>
  );
}

export default App;
