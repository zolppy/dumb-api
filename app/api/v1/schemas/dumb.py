from pydantic import BaseModel


class DumbBase(BaseModel):
    string: str


class DumbCreate(DumbBase):
    id: int

    class Config:
        from_attributes = True


class DumbIn(DumbBase):
    pass
