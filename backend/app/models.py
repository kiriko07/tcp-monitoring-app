# backend/app/models.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .database import Base

class TCPConnectionDemo(Base):
    __tablename__ = "tcp_connections_demo"

    id = Column(Integer, primary_key=True, index=True)
    remote_ip = Column(String(45), nullable=False, index=True)
    remote_port = Column(Integer, nullable=False)
    local_ip = Column(String(45), nullable=False)
    local_port = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    disconnected_at = Column(DateTime) # 可以为 NULL
    last_active_at = Column(DateTime, nullable=False)