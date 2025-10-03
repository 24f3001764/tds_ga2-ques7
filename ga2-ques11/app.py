from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import csv

app = FastAPI()

# Enable CORS for all origins and GET method
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load CSV data at startup
students_data = []
with open("students.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Convert studentId to int, keep class as string
        students_data.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
async def get_students(class_: List[str] = Query(None, alias="class")) -> Dict[str, Any]:
    if class_:
        # Return only students whose 'class' is in class_ (preserving CSV order)
        filtered = [s for s in students_data if s["class"] in class_]
        return {"students": filtered}
    return {"students": students_data}
