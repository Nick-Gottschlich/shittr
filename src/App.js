import React from 'react';
import MainScreen from './Containers/MainScreen';
import { 
  BrowserRouter as Router, 
  Route
} from 'react-router-dom';

function App() {
  return (
    <Router>
      <Route path="/" exact component={MainScreen} />
    </Router>
  );
}

export default App;