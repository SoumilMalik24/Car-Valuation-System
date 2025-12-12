from pydantic import BaseModel, Field

class CarInput(BaseModel):
    Levy: int = Field(..., example=1000)
    Manufacturer: str = Field(..., example="Toyota")
    Model: str = Field(..., example="Camry")
    Category: str = Field(..., example="Sedan")
    Leather_interior: str = Field(..., example="Yes")
    Fuel_type: str = Field(..., example="Hybrid")
    Mileage: int = Field(..., example=50000)
    Cylinders: float = Field(..., example=4.0)
    Gear_box_type: str = Field(..., example="Automatic")
    Drive_wheels: str = Field(..., example="Front")
    Doors: int = Field(..., example=4)
    Wheel: str = Field(..., example="Left wheel")
    Color: str = Field(..., example="Black")
    Airbags: int = Field(..., example=12)
    Engine_Vol: float = Field(..., example=2.5)
    Prod_year: int = Field(..., example=2020)