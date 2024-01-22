
# Twitter APP built with FastAPI 

## Overview

This project is a Twitter clone built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features

- **User Management:** CRUD operations for managing users.
- **Tweet Management:** CRUD operations for creating, reading, updating, and deleting tweets.
- **FastAPI:** Utilizes the power and simplicity of FastAPI for efficient API development.
- **RESTful API:** Follows RESTful principles for a well-organized API structure.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:pratik-udeshi1/twitter-app.git
   cd twitter-app
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   uvicorn main:app --reload
   ```

   The API will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

- **User Endpoints:**
  - `GET /users/{user_id}`: Get user details by ID.
  - `POST /users/`: Create a new user.
  - `PUT /users/{user_id}`: Update user details.
  - `DELETE /users/{user_id}`: Delete a user.

- **Tweet Endpoints:**
  - `GET /tweets/{tweet_id}`: Get tweet details by ID.
  - `POST /tweets/`: Create a new tweet.
  - `PUT /tweets/{tweet_id}`: Update tweet content.
  - `DELETE /tweets/{tweet_id}`: Delete a tweet.

## Documentation

- The API documentation is available at `http://127.0.0.1:8000/docs`.
- Explore and test the API using the Swagger UI.

## Contributing

Contributions are welcome! Follow the best practices and guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit/) file for details.

---