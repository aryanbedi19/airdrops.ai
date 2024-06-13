import React, { useState } from 'react';
import WalletInput from '../components/WalletInput';
import AirdropChart from '../components/AirdropChart';

function HomePage() {
    const [airdrops, setAirdrops] = useState([]);
    const [user, setUser] = useState(null);

    const handleRegister = async (email, walletAddress, password) => {
        try {
            const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/register`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, wallet_address: walletAddress, password }),
            });

            if (response.ok) {
                const data = await response.json();
                setUser(data.user_id);
                fetchAirdrops(data.user_id);
            } else {
                console.error('Registration failed');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const fetchAirdrops = async (userId) => {
        try {
            const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/airdrops?user_id=${userId}`);
            const data = await response.json();
            setAirdrops(data);
        } catch (error) {
            console.error('Error:', error);
        }
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
