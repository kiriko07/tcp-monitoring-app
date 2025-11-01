# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# --- 数据模型 ---
class Connection(BaseModel):
    id: Optional[int] = None
    name: str
    host: str
    port: int

# --- 创建 FastAPI 应用实例 ---
app = FastAPI(
    title="TCP Monitoring API",
    description="一个用于监控 TCP 连接状态的 API。",
    version="0.1.0"
)

# --- 模拟数据库 ---
# 在真实应用中，这里会连接到 PostgreSQL 数据库
connections_db = []

# --- API 端点 ---

@app.get("/")
def read_root():
    """根路径，返回 API 状态"""
    return {"message": "Welcome to TCP Monitoring API"}

@app.get("/connections/", response_model=List[Connection])
def read_connections():
    """获取所有连接列表"""
    return connections_db

@app.post("/connections/", response_model=Connection)
def create_connection(connection: Connection):
    """创建一个新的监控连接"""
    # 在真实应用中，这里会使用数据库添加新记录
    # 并获取生成的 ID
    new_id = len(connections_db) + 1
    connection.id = new_id
    connections_db.append(connection)
    return connection

@app.get("/connections/{connection_id}", response_model=Connection)
def read_connection(connection_id: int):
    """根据 ID 获取单个连接"""
    for connection in connections_db:
        if connection.id == connection_id:
            return connection
    raise HTTPException(status_code=404, detail="Connection not found")

# --- 运行应用 ---
if __name__ == "__main__":
    # 这行代码用于本地直接运行（不通过 Docker）
    uvicorn.run(app, host="0.0.0.0", port=8000)