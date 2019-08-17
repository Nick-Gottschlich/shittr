// NPM
import React from 'react';

// Local
import fbLogo from '../assets/fbLogo.png';

// CSS
import './MainScreen.css';

export default class MainScreen extends React.Component {
  render() {
    return (
      <div className="App">
        <div className="linkContainer">
          <a 
            href="https://www.facebook.com/help/delete_account" 
            target="_blank" 
            className="button">
            <img 
              className="facebookLogo"
              src={fbLogo}
              alt="fucc the zucc" 
            />
            Flush Facebook
          </a>
        </div>
        <div className="linkContainer">
          <a href="https://google.com" className="button">
            <img 
              className="facebookLogo"
              src={fbLogo}
              alt="fucc the zucc" 
            />
            Flush Instagram
          </a>
        </div>
      </div>
    )
  }
}
