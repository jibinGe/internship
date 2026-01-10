from fastapi import FastAPI, HTTPException
# from app.crud import add_student
# from app.models import Student

app = FastAPI()

# API endpoints 

@app.get("/")
def home():
    return {"message": "Students API 123"}

@app.get("/user")
def home():
    return {"message": "user read"}

# @app.post("/students")
# def create_students(student:Student):
#     add_student(student.id,student.name,student.email)
#     return {"message":"Student added sucessfully"}