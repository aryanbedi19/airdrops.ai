import React, { useState } from 'react';

function SignUpPage({ onSignUp }) {
    const [email, setEmail] = useState('');
    const [walletAddress, setWalletAddress] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSignUp(email, walletAddress, password);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Enter your email"
                required
            />
            <input
                type="text"
                value={walletAddress}
                onChange={(e) => setWalletAddress(e.target.value)}
                placeholder="Enter your wallet address"
                required
            />
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Enter your password"
                required
            />
            <button type="submit">Sign Up</button>
        </form>
    );
}

export default SignUpPage;
