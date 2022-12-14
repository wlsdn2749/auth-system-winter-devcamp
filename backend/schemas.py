from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class RefreshIncludedToken(Token):
    refresh_token: str

class TokenData(BaseModel):
    email: str | None = None


class TokenDataModel(BaseModel):
    access_token: str
    token_type: str
    email: str    
    
    # class Config:
    #     orm_mode = True

class User(UserBase):
    # id: int
    # is_activate = bool

    class Config:
        orm_mode = True
