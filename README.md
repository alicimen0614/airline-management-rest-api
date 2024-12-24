# Airline Management System

This project provides a backend API for managing an airline's operations for airplanes, flights, and passenger reservations. Built using Django REST Framework (DRF), the API enables CRUD operations on key models while incorporating features such as reservation code generation, capacity checks, filtering and sending email after creating a reservation.

## Requirements

- **Django**: Web framework for building web applications.
- **Django REST Framework**: Toolkit for building Web APIs.
- **ShortUUID**: Library for generating short, human-readable UUIDs.
- **python-dotenv**: Reads key-value pairs from `.env` file and adds them to environment variables.
- **django-filter**: Django library for filtering querysets dynamically.

## Setup Instructions

1. Clone the repository.
2. Create a virtual environment and activate it.
```
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate  # for Windows
```
3. Install dependencies using `pip install -r requirements.txt`.
4. Run migrations: `python manage.py migrate`.
5. Start the development server: `python manage.py runserver`.
6. (Optional) To send an email after creating a reservation, create a project-level .env file and configure it with the provided data or customize it as needed.
```
APP_PASSWORD="******"
APP_EMAIL="johndoe@example.com"
APP_EMAIL_HOST="smtp.example.com"
```

## API Documentation

`For more detailed documentation you can view the postman collection documentation.`


### Base URL

```
http://127.0.0.1:8000/api
```

### Modules

#### 1. Airplanes

Manage airplane records.

- **List all airplanes**

  Retrieves the list of all airplanes.
  - Method: `GET`
  - Endpoint: `/airplanes/`
   

- **Get a specific airplane**

  Retrieves the details of a specific airplane.
  - Method: `GET`
  - Endpoint: `/airplanes/{airplaneId}/`
  - Parameters:
    - `airplaneId` : The ID of the airplane.

- **Get airplane flights**

  Retrieves all flights assigned to a specific airplane.
  - Method: `GET`
  - Endpoint: `/airplanes/{airplaneId}/flights`

- **Add a new airplane**

  Allows you to add a new airplane.
  - Method: `POST`
  - Endpoint: `/airplanes/`
  - Body (JSON):   

    The request body needs to be in JSON format and include the following properties:

    - tail_number - String - Required
    - model - String - Required
    - capacity - Integer- Required
    - production_year - Integer - Optional

    - status - Boolean - Optional (Default to True)

   ```json
    {
      "tail_number": "TC-NRT",
      "model": "Airbus A320",
      "capacity": 180,
      "production_year": 2005,
      "status": true
    }
    ```

- **Update an airplane**  

  Updates the details of a specific airplane.
  - Method: `PATCH`
  - Endpoint: `/airplanes/{airplaneId}/`

 
    ```json
    {
    "capacity": "190"
    }
    ```

- **Delete an airplane**  

  Deletes an airplane from the database.
  - Method: `DELETE`
  - Endpoint: `/airplanes/{airplaneId}/`

#### 2. Flights

Manage flight records.

- **List all flights**

   Retrieves the list of all flights.
  - Method: `GET`
  - Endpoint: `/flights/`

- **Get specific flight**

  Retrieves the details of a specific flight.
  - Method: `GET`
  - Endpoint: `/flights/{flightId}/`
  - Parameters:
    - `flightId` : The ID of the flight.

- **Get flight reservations**

  Retrieves all reservations for a specific flight
  - Method: `GET`
  - Endpoint: `/flights/{flightId}/reservations/`

- **Add a new flight**

  Allows you to add a new flight.
  - Method: `POST`
  - Endpoint: `/flights/`
  - Body (JSON):

    The request body needs to be in JSON format and include the following properties:
    - flight_number - String - Required

    - departure - String - Required
    - destination - String- Required
    - departure_time - DateTime- Required
    - arrival_time - DateTime - Required
    - airplane - Integer (valid airplaneId) - Required

  ```json
    {
      "flight_number": "TK1234",
      "departure": "Esenboga Airport",
      "destination": "Istanbul Airport",
      "departure_time": "2025-02-21T23:21:00Z",
      "arrival_time": "2025-02-22T10:00:00Z",
      "airplane": {airplaneId}
    }
    ```

- **Update a flight**

  Updates the details of a specific flight.
  - Method: `PATCH`

  - Endpoint: `/flights/{flightId}/`

  `Note: Ensure that both departure_time and arrival_time must be provided together if either is included.`

 ```json
    {
    "departure_time": "2025-02-22T5:21:00Z",
    "arrival_time": "2025-02-22T23:21:00"
    }
  ```


- **Delete a flight**

  Deletes a flight from the database.
  - Method: `DELETE`
  - Endpoint: `/flights/{flightId}`
- **Filter flights**

  Filters flights based on the specified parameters.
  - Method: `GET`
  - Endpoint: `/flights/`
  - Query Parameters:
    - `arrival_time`
    - `departure_time`
    - `departure`
    - `destination`
    - `search`
    - `ordering`

#### 3. Reservations

Manage passenger reservations.

- **List all reservations**  

  Retrieves the list of all reservations.
  - Method: `GET`
  - Endpoint: `/reservations/`

- **Get specific reservation**

   Retrieves the details of a specific reservation.
  - Method: `GET`
  - Endpoint: `/reservations/{reservationId}`
  - Parameters:
    - `reservationId` : The ID of the reservation.

- **Add a new reservation**

  Allows you to add a new reservation.
  - Method: `POST`
  - Endpoint: `/reservations/`
  - Body (JSON):

    `Note: The email sending feature requires additional configurations, including SMTP 
    server settings, an app password, and the app email address. Without these 
    configurations, the request may result with errors.`

    The request body needs to be in JSON format and include the following properties:

     - passenger_name - String - Required
     - passenger_email - String - Required (Enter a valid email to test email sending feature)
     - status - Boolean - Optional (Default to True)

     - flight - Integer (valid flightId) - Required


  ```json
    {
      "passenger_name": "John Doe",
      "passenger_email": "johndoe@example.com",
      "status": true,
      "flight": {flightId}
    }
    ```

- **Update a reservation**

  Updates the details of a specific reservation.
  - Method: `PATCH`

  - Endpoint: `/reservations/{reservationId}`

  ```json
  {
    "passenger_name":"James Doe"
   }
  ```
- **Delete a reservation**

  Deletes a reservation from the database.
  - Method: `DELETE`
  - Endpoint: `/reservations/{reservationId}`