from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class SchoolBase(BaseModel):
    school_id: Optional[str] = None
    name: str
    long_name: str
    last_name: str
    dise_code: int = Field(..., ge=10**10, le=10**11 - 1, description="Phone number must be a 10-digit integer")    
    city: str
    state: str
    pincode: int
    owner_id: int
    organization_id: int
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    last_updated_at: Optional[datetime] = None
    last_updated_by: Optional[str] = None

class SchoolUpdate(BaseModel):
    school_id: Optional[str] = None
    name: Optional[str] = None
    long_name: Optional[str] = None
    last_name: Optional[str] = None
    dise_code: Optional[int] = Field(None, ge=10**10, le=10**11 - 1, description="Phone number must be a 10-digit integer")
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[int] = None
    owner_id: Optional[int] = None
    organization_id: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    last_updated_at: Optional[datetime] = None
    last_updated_by: Optional[str] = None

class ILPUserCreate(SchoolBase):
 pass

class ILPUser(SchoolBase):
    user_id: str
    class Config:
        orm_mode = True
