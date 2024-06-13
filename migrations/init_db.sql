CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    wallet_address TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    subscription_end_date TIMESTAMP
);

CREATE TABLE airdrop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    claim_url TEXT,
    logo_url TEXT,
    network TEXT,
    value REAL,
    percentage REAL,
    sentiment_score REAL,
    risk_score REAL
);
