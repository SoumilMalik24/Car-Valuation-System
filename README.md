# Car Valuation System 🚗💰

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?style=for-the-badge&logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render)

An end-to-end Machine Learning system aimed at providing real-time valuations for used cars. This project utilizes a Random Forest Regressor for high-accuracy predictions and exposes the model via a scalable REST API built with FastAPI. The entire application is containerized using Docker and is ready for deployment on platforms like Render. Open to use on: `https://car-valuation-system.onrender.com/`

---

## 🚀 Features

- **Real-time Valuation**: Instant price predictions based on car specifications  
- **Advanced ML Pipeline**: Feature engineering and model training using Scikit-Learn  
- **Robust Model**: Random Forest Regressor for handling non-linear relationships  
- **RESTful API**: High-performance prediction endpoints built with FastAPI  
- **Containerized**: Dockerized application for consistent deployment  
- **Interactive Docs**: Automatic Swagger UI documentation  

---

## 🛠️ Tech Stack

- **Language**: Python  
- **Machine Learning**: Scikit-Learn, Pandas, NumPy  
- **API Framework**: FastAPI, Uvicorn  
- **Containerization**: Docker  
- **Deployment**: Render  
- **Tools**: Jupyter Notebooks  

---

## 📂 Project Structure

```bash
Car-Valuation-System/
├── config/              # Configuration files
├── model/               # Serialized ML models
├── notebook/            # Jupyter notebooks (EDA & training)
├── schema/              # Pydantic request/response schemas
├── app.py               # FastAPI application entry point
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```
---

## 💻 Installation & Setup

### Prerequisites

* Python 3.8+
* Git
* Docker (optional)

### Local Setup

1. **Clone the repository**

```bash
git clone https://github.com/SoumilMalik24/Car-Valuation-System.git
cd Car-Valuation-System
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://localhost:8000
```

---

## 🐳 Running with Docker

1. **Build the Docker image**

```bash
docker build -t car-valuator .
```

2. **Run the container**

```bash
docker run -p 8000:8000 car-valuator
```

---

## 🔌 API Usage

Once running, access the API documentation:

* **Swagger UI**: `http://localhost:8000/docs`
* **ReDoc**: `http://localhost:8000/redoc`

### Example Prediction Request

**Endpoint**: `https://car-valuation-system.onrender.com/`

**Request Body**

```json
{
  "Levy": 1000,
  "Manufacturer": "Toyota",
  "Model": "Camry",
  "Category": "Sedan",
  "Leather_interior": "Yes",
  "Fuel_type": "Hybrid",
  "Mileage": 50000,
  "Cylinders": 4,
  "Gear_box_type": "Automatic",
  "Drive_wheels": "Front",
  "Doors": 4,
  "Wheel": "Left wheel",
  "Color": "Black",
  "Airbags": 12,
  "Engine_Vol": 2.5,
  "Prod_year": 2020
}
```

> Refer to the `schema/` directory for exact input fields.

---

## 🧠 Model Training

Model training notebooks are available in the `notebook/` directory.

Steps:

1. Open notebooks using Jupyter
2. Perform EDA and feature engineering
3. Train the model
4. Save the trained model to the `model/` directory

The API automatically loads the trained model during startup.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -m "Add feature"`)
4. Push to branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

<p align="center">
Built with ❤️ by <a href="https://github.com/SoumilMalik24">Soumil Malik</a>
</p>

