// NPM
import React from 'react';

// Local
import fbLogo from '../assets/fbLogo.png';
import igLogo from '../assets/igLogo.png';
import twitterLogo from '../assets/twitterLogo.png';
import redditLogo from '../assets/redditLogo.svg';

// CSS
import './MainScreen.css';

export default class MainScreen extends React.Component {
  render() {
    return (
      <div className="App">
        <div className="linkContainer facebook">
          <a 
            href="https://www.facebook.com/help/delete_account" 
            target="_blank">
            Flush Facebook
            <img 
              className="siteLogo"
              src={fbLogo}
              alt="fucc the zucc" 
            />
          </a>
        </div>
        <div className="linkContainer instagram">
          <a 
            href="https://www.instagram.com/accounts/remove/request/permanent/" 
            target="_blank">
            Flush Instagram
            <img 
              className="siteLogo"
              src={igLogo}
              alt="fucc the zucc" 
            />
          </a>
        </div>
        <div className="linkContainer twitter">
          <a 
            href="https://twitter.com/settings/deactivate" 
            target="_blank">
            Flush Twitter
            <img 
              className="siteLogo"
              src={twitterLogo}
              alt="facc the jacc" 
            />
          </a>
        </div>
        <div className="linkContainer reddit">
          <a 
            href="https://www.reddit.com/settings" 
            target="_blank">
            Flush Reddit
            <img 
              className="siteLogo"
              src={redditLogo}
              alt="Ok Aaron Swartz is aight" 
            />
          </a>
        </div>
      </div>
    )
  }
}
