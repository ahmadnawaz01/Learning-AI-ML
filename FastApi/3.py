from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json


class Patient(BaseModel):
    id: Annotated[
        str,
        Field(
            ...,
            description="The ID of the patient in DB",
            example="P001"
        )
    ]

    name: Annotated[
        str,
        Field(
            ...,
            description="The name of the patient",
            example="John Doe"
        )
    ]

    city: Annotated[
        str,
        Field(
            ...,
            description="The city of the patient",
            example="New York"
        )
    ]

    age: Annotated[
        int,
        Field(
            ...,
            gt=0,
            lt=120,
            description="The age of the patient",
            example=30
        )
    ]

    gender: Annotated[
        Literal["male", "female"],
        Field(
            ...,
            description="The gender of the patient",
            example="male"
        )
    ]

    height: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="The height of the patient in cm",
            example=175.5
        )
    ]

    weight: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="The weight of the patient in kg",
            example=70.5
        )
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / ((self.height / 100) ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal["male", "female"]], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


app = FastAPI()


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)


@app.get("/")
def hello():
    return {
        "message": "Patient management system is running successfully!"
    }


@app.get("/about")
def about():
    return {
        "message": "A fully functional patient management system to manage your patient record."
    }


@app.get("/view")
def view():
    data = load_data()
    return data


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ...,
        description="The ID of the patient in DB",
        example="P001"
    )
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(
        status_code=404,
        detail=f"Patient with ID {patient_id} not found in the database."
    )


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="Sort on the basis of height, weight or bmi",
        example="height"
    ),
    order: str = Query(
        "asc",
        description="Sort order",
        example="asc"
    )
):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Use 'asc' or 'desc'."
        )

    data = load_data()

    reverse = True if order == "desc" else False

    if sort_by == "bmi":
        sorted_data = sorted(
            data.values(),
            key=lambda x: round(
                x["weight"] / ((x["height"] / 100) ** 2),
                2
            ),
            reverse=reverse
        )
    else:
        sorted_data = sorted(
            data.values(),
            key=lambda x: x[sort_by],
            reverse=reverse
        )

    return sorted_data


@app.post("/create")
def create_patient(patient: Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail=f"Patient with ID {patient.id} already exists in the database."
        )

    data[patient.id] = patient.model_dump(exclude=["id"])

    save_data(data)

    return JSONResponse(
        status_code=201,
        content={
            "message": f"Patient with ID {patient.id} created successfully."
        }
    )


@app.put("/edit/{patient_id}")
def update_patient(
    patient_id: str,
    patient_update: PatientUpdate
):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Patient with ID {patient_id} not found in the database."
        )

    existing_info = data[patient_id]

    patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in patient_info.items():
        existing_info[key] = value

    existing_info["id"] = patient_id

    pydantic_obj = Patient(**existing_info)

    existing_info = pydantic_obj.model_dump(exclude=["id"])

    data[patient_id] = existing_info

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Patient with ID {patient_id} updated successfully."
        }
    )

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id:str):
    data=load_data()


    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Patient with ID {patient_id} not found in the database."
        )

    del data[patient_id]
    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Patient with ID {patient_id} deleted successfully."
        }
    )