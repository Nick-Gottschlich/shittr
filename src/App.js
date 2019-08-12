import React from 'react';
import MainScreen from './Containers/MainScreen';
import FacebookScreen from './Containers/FacebookScreen';
import { 
  BrowserRouter as Router, 
  Route
} from 'react-router-dom';

function App() {
  return (
    <Router>
      <Route path="/" exact component={MainScreen} />
      <Route path="/facebook" component={FacebookScreen} />
    </Router>
  );
}

export default App;