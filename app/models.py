from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from .database import base

class DictionaryRequest(base):
    __tablename__="dictionary_requests"
    id = Column(Integer, primary_key=True, index=True)
    request_date = Column(DateTime, default=datetime.utcnow)
    word = Column(String(255), nullable=False)
    response_json = Column(JSON, nullable=False)
    