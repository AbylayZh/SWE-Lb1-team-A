import React, { useState } from 'react';
import LoginForm from './LoginForm';
import HomePage from './Homepage'

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <div>
      {isLoggedIn ? (
        <HomePage />
      ) : (
        <LoginForm onLoginSuccess={() => setIsLoggedIn(true)} />
      )}
    </div>
  );
};

export default App;




