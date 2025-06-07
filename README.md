# Barbershop API

This is a FastAPI application for managing a barbershop. It provides endpoints for listing haircuts, gallery items, workers, and creating reservations.


## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd barbershop_api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

## Usage

- **List Haircuts**: GET `/api/haircuts/`
- **List Gallery Items**: GET `/api/gallery/`
- **List Workers**: GET `/api/workers/`
- **Create Reservation**: POST `/api/reservations/` with JSON body:
  ```json
  {
    "worker_id": 1,
    "name": "John Doe",
    "phone_number": "1234567890",
    "date": "2023-10-01",
    "time": "15:00"
  }
  ```

## License

This project is licensed under the MIT License.