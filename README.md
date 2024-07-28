# Customer Order Management System

## Overview

The Customer Order Management System is designed to manage customer orders efficiently using a Hexagonal Architecture pattern. This architecture ensures a clear separation between business logic and external systems, making the application robust, flexible, and easier to test.

## Features

- Efficient order management
- RESTful API
- AWS SQS integration
- SQLite for data storage

## Technology Stack

- Python
- Flask
- SQLAlchemy
- AWS SQS
- SQLite

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/customer-order-system.git
    cd customer-order-system
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```bash
    python3 -m app.initialize_db
    ```

5. Set the AWS region:
    ```bash
    export AWS_REGION=us-west-2
    ```

6. Run the application:
    ```bash
    flask run
    ```

## Usage

- Access the API at `http://127.0.0.1:5000/api/`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.