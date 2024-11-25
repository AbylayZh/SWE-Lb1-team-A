import React, { useState } from 'react';

// Simulating a JSON file with valid credentials
const validCredentials = {
  email: "r@example.com",
  password: "1",
};

// Login Page Component
const LoginForm = ({ onLoginSuccess }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validate credentials
    if (email === validCredentials.email && password === validCredentials.password) {
      setError('');
      onLoginSuccess(); // Notify parent component of successful login
    } else {
      setError('Invalid email or password.');
    }
  };

  return (
    <div style={{ padding: '20px', backgroundColor: '#f8f9fa', height: '100vh' }}>
      <h1 style={{ color: '#155724', textAlign: 'center' }}>Admin's Dashboard</h1>
      <div
        style={{
          maxWidth: '400px',
          margin: '0 auto',
          padding: '1.5rem',
          border: '1px solid #c3e6cb',
          borderRadius: '8px',
          marginTop: '100px',
          backgroundColor: '#d4edda',
        }}
      >
        <h2 style={{ color: '#155724', textAlign: 'center' }}>Login</h2>
        {error && (
          <div
            style={{
              color: 'red',
              marginBottom: '1rem',
              backgroundColor: '#f8d7da',
              padding: '0.5rem',
              borderRadius: '4px',
              textAlign: 'center',
            }}
          >
            {error}
          </div>
        )}
        <form onSubmit={handleSubmit}>
          <div style={{ marginBottom: '1.5rem' }}>
            <label
              htmlFor="email"
              style={{
                display: 'block',
                marginBottom: '0.5rem',
                fontWeight: 'bold',
                color: '#155724',
              }}
            >
              Email:
            </label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              style={{
                width: '95%',
                padding: '0.75rem',
                borderRadius: '4px',
                border: '1px solid #c3e6cb',
                backgroundColor: '#f8f9fa',
              }}
            />
          </div>
          <div style={{ marginBottom: '1.5rem' }}>
            <label
              htmlFor="password"
              style={{
                display: 'block',
                marginBottom: '0.5rem',
                fontWeight: 'bold',
                color: '#155724',
              }}
            >
              Password:
            </label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              style={{
                width: '95%',
                padding: '0.75rem',
                borderRadius: '4px',
                border: '1px solid #c3e6cb',
                backgroundColor: '#f8f9fa',
              }}
            />
          </div>
          <button
            type="submit"
            style={{
              padding: '0.75rem 1.5rem',
              borderRadius: '4px',
              border: 'none',
              backgroundColor: '#28a745',
              color: 'white',
              fontWeight: 'bold',
              cursor: 'pointer',
              width: '100%',
            }}
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;

