// NPM
import React from 'react';

// Local
import fbLogo from '../assets/fbLogo.png';
import igLogo from '../assets/igLogo.png';

// CSS
import './MainScreen.css';

export default class MainScreen extends React.Component {
  render() {
    return (
      <div className="App">
        <div className="linkContainer facebook">
          <a 
            href="https://www.facebook.com/help/delete_account" 
            target="_blank" 
            className="flex">
            <img 
              className="siteLogo"
              src={fbLogo}
              alt="fucc the zucc" 
            />
            Flush Facebook
          </a>
        </div>
        <div className="linkContainer instagram">
          <a 
            href="https://www.instagram.com/accounts/remove/request/permanent/" 
            className="flex"
            target="_blank">
            <img 
              className="siteLogo"
              src={igLogo}
              alt="fucc the zucc" 
            />
            Flush Instagram
          </a>
        </div>
      </div>
    )
  }
}
