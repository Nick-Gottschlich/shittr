import React from 'react';
import fbLogo from '../assets/fbLogo.png';
import './MainScreen.css';

export default class MainScreen extends React.Component {
  render() {
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
    )
  }
}
