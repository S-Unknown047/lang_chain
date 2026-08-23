from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    studentName: str = 'subh'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt = 0, lt = 10, default= 5, description="a decimal value")

new_student = {'studentName': 'subbu', 'age': 45, 'email': 'abc@gamil.com', 'cgpa': 8}

student = Student(**new_student)

print(student.model_dump())