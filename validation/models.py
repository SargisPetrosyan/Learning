
import uuid
from datetime import date, datetime, timedelta
from pydantic import BaseModel,field_validator
from enums import DepartmentEnum


class Module(BaseModel):
    id: int | uuid.UUID
    name: str
    professor: str
    credits: int
    registration_code: str

class Student(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: float
    course: str | None
    department: DepartmentEnum
    fees_paid: bool
    modules: list[Module] = []

    @field_validator('date_of_birth')
    def ensure_16_or_over(cls, value):
        sixteen_years_ago = datetime.now() - timedelta(days=365*16)

        # convert datetime object -> date
        sixteen_years_ago = sixteen_years_ago.date()
        
        # raise error if DOB is more recent than 16 years past.
        if value > sixteen_years_ago:
            raise ValueError("Too young to enrol, sorry!")
        return value