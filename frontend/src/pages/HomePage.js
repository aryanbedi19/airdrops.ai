import React, { useState } from 'react';
import WalletInput from '../components/WalletInput';
import AirdropChart from '../components/AirdropChart';

function HomePage() {
    const [airdrops, setAirdrops] = useState([]);
    const [user, setUser] = useState(null);

    const handleRegister = async (email, walletAddress, password) => {
        const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, wallet_address: walletAddress, password }),
        });
        const data = await response.json();
        if (response.status === 201) {
            setUser(data.user_id);
            fetchAirdrops(data.user_id);
        }
    };

    const fetchAirdrops = async (userId) => {
        const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/airdrops?user_id=${userId}`);
        const data = await response.json();
        setAirdrops(data);
    };

    return (
        <div>
            <h1>Airdrop Platform</h1>
            <WalletInput onRegister={handleRegister} />
            <AirdropChart airdrops={airdrops} blurred={!user} />
        </div>
    );
}

export default HomePage;
