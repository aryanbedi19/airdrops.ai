import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import SignUpPage from './pages/SignUpPage';

function App() {
    const [userId, setUserId] = useState(null);

    const handleLogin = async (email, password) => {
        const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password }),
        });
        const data = await response.json();
        if (response.status === 200) {
            setUserId(data.user_id);
        }
    };

    const handleSignUp = async (email, walletAddress, password) => {
        const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, wallet_address: walletAddress, password }),
        });
        const data = await response.json();
        if (response.status === 201) {
            setUserId(data.user_id);
        }
    };

    return (
        <Router>
            <Switch>
                <Route path="/" exact>
                    <HomePage />
                </Route>
                <Route path="/login" exact>
                    <LoginPage onLogin={handleLogin} />
                </Route>
                <Route path="/signup" exact>
                    <SignUpPage onSignUp={handleSignUp} />
                </Route>
            </Switch>
        </Router>
    );
}

export default App;
