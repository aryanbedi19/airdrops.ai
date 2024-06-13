import React from 'react';
import { Table } from 'reactstrap';

function AirdropChart({ airdrops, blurred }) {
    return (
        <Table striped>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Name</th>
                    <th>Network</th>
                    <th>Value</th>
                    <th>Percentage</th>
                    <th>Sentiment Score</th>
                    <th>Risk Score</th>
                </tr>
            </thead>
            <tbody>
                {airdrops.map((airdrop, index) => (
                    <tr key={index} style={{ filter: blurred && index > 0 ? 'blur(5px)' : 'none' }}>
                        <th scope="row">{index + 1}</th>
                        <td>{airdrop.name}</td>
                        <td>{airdrop.network}</td>
                        <td>{airdrop.value}</td>
                        <td>{airdrop.percentage}</td>
                        <td>{airdrop.sentiment_score}</td>
                        <td>{airdrop.risk_score}</td>
                    </tr>
                ))}
            </tbody>
        </Table>
    );
}

export default AirdropChart;
