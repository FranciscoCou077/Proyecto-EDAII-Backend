from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from app.core.database import Base


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    sender = Column(String(50), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)


class AlgorithmExecution(Base):
    __tablename__ = "algorithm_executions"

    id = Column(Integer, primary_key=True, index=True)
    algorithm_name = Column(String(100), nullable=False)
    execution_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), nullable=False)
    parameters = Column(Text)
    result = Column(Text)
