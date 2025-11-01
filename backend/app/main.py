# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
import uvicorn
from . import models, database

# --- Pydantic 模型用于 API 请求和响应 ---
class ConnectionResponse(BaseModel):
    id: int
    remote_ip: str
    remote_port: int
    local_ip: str
    local_port: int
    created_at: str # 将 datetime 转为字符串
    disconnected_at: Optional[str]
    last_active_at: str

# --- FastAPI 应用实例 ---
app = FastAPI(
    title="TCP Monitoring API",
    description="一个用于监控 TCP 连接状态的 API。",
    version="0.2.0"
)

# --- 数据库依赖 ---
@app.on_event("startup")
def on_startup():
    # 在启动时创建数据库表
    models.database.Base.metadata.create_all(bind=database.engine)
    database.SessionLocal()


# --- API 端点 ---

@app.get("/")
def read_root():
    """根路径，返回 API 状态"""
    return {"message": "Welcome to TCP Monitoring API"}

@app.get("/connections/", response_model=List[ConnectionResponse])
def read_connections(db: Session = database.dependency()):
    """获取所有连接列表"""
    connections = db.query(models.TCPConnectionDemo).all()
    return connections

@app.get("/connections/active", response_model=List[ConnectionResponse])
def read_active_connections(db: Session = database.dependency()):
    """获取所有未断开的连接"""
    active_connections = db.query(models.TCPConnectionDemo).filter(models.TCPConnectionDemo.disconnected_at.is_(None)).all()
    return active_connections

@app.get("/connections/{connection_id}", response_model=ConnectionResponse)
def read_connection(connection_id: int, db: Session = database.dependency()):
    """根据 ID 获取单个连接"""
    connection = db.query(models.TCPConnectionDemo).filter(models.TCPConnectionDemo.id == connection_id).first()
    if connection is None:
        raise HTTPException(status_code=404, detail="Connection not found")
    return connection

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)