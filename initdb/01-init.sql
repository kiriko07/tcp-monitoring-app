-- initdb/01-init.sql

-- 创建数据库
-- 这个通常由 Kubernetes 的 StatefulSet 或外部数据库服务创建，这里仅为示例
-- CREATE DATABASE tcpdb;

-- 使用数据库
-- \c tcpdb;

-- 创建连接表
CREATE TABLE IF NOT EXISTS connections (
                                           id SERIAL PRIMARY KEY,
                                           name VARCHAR(100) NOT NULL,
                                           host VARCHAR(255) NOT NULL,
                                           port INTEGER NOT NULL,
                                           created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 插入一些示例数据（可选）
INSERT INTO connections (name, host, port) VALUES
                                               ('Google Public DNS', '8.8.8.8', 53),
                                               ('Cloudflare DNS', '1.1.1.1', 53),
                                               ('GitHub SSH', 'github.com', 22)
ON CONFLICT (id) DO NOTHING;