# k2-test

## Prerequisites

Ensure that **port 80** is not being used by any other process on your machine. If it is, you may need to free up the port or change the port configuration in the Docker setup.

## Getting Started

### 1. **Set Up the Environment**

-   Copy the `example.env` file to `.env` in the project root directory:

    ```bash
    cp example.env .env
    ```

### 2. **Run the Project with Docker**

To start the project using Docker, run the following command in the root of the project:

```bash
docker-compose up
```

After the containers are up and running, you can access the project by opening [http://localhost](http://localhost) in your browser.

## Running Tests

### 1. **Set Up the Testing Environment**

Go to the `k2-test/api` directory:

```bash
cd k2-test/api
```

Create a virtual environment (if you don't have one already):

```bash
python -m venv venv
```

Activate the virtual environment:

-   On **Windows**:

    ```bash
    venv\Scripts\activate
    ```

-   On **macOS/Linux**:

    ```bash
    source venv/bin/activate
    ```

### 2. **Install Dependencies**

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### 3. **Configure the Environment**

Set the `DEBUG` environment variable to `True`:

```bash
export DEBUG=True
```

> On **Windows**, use `set DEBUG=True` instead.

### 4. **Run the Tests**

To run the tests, execute the following command:

```bash
python manage.py test
```

This will run all the test cases in the project.
