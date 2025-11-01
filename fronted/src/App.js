// src/App.js
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
    const [connections, setConnections] = useState([]);
    const [newConnection, setNewConnection] = useState({ name: '', host: '', port: '' });

    useEffect(() => {
        // 在开发环境中，前端运行在 3000 端口，后端在 8000 端口
        // 需要代理配置，或者在代码中指定完整 URL
        // Create React App 开发服务器默认会代理请求到 /api 到 http://localhost:8000
        fetch('/api/connections/')
            .then(response => response.json())
            .then(data => setConnections(data))
            .catch(error => console.error('Error fetching connections:', error));
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setNewConnection(prev => ({ ...prev, [name]: value }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('/api/connections/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newConnection),
        })
            .then(response => response.json())
            .then(data => {
                setConnections([...connections, data]);
                setNewConnection({ name: '', host: '', port: '' }); // 重置表单
            })
            .catch(error => console.error('Error creating connection:', error));
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>TCP Connection Monitor</h1>
                <form onSubmit={handleSubmit} className="connection-form">
                    <input
                        type="text"
                        name="name"
                        value={newConnection.name}
                        onChange={handleChange}
                        placeholder="Connection Name"
                        required
                    />
                    <input
                        type="text"
                        name="host"
                        value={newConnection.host}
                        onChange={handleChange}
                        placeholder="Host (e.g., google.com)"
                        required
                    />
                    <input
                        type="number"
                        name="port"
                        value={newConnection.port}
                        onChange={handleChange}
                        placeholder="Port (e.g., 80)"
                        required
                    />
                    <button type="submit">Add Connection</button>
                </form>
            </header>
            <main>
                <h2>Active Connections</h2>
                <ul className="connection-list">
                    {connections.map(conn => (
                        <li key={conn.id} className="connection-item">
                            <strong>{conn.name}</strong> - {conn.host}:{conn.port}
                        </li>
                    ))}
                </ul>
            </main>
        </div>
    );
}

export default App;