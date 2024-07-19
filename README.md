# Outsera - Golden Raspberry Awards API

# Requirements

- Python 3.8+
- Flask
- Flask-SQLAlchemy

# Install

1. Clone the repository
```
    git clone https://github.com/fabricioterranova/outsera.git
    cd Outsera
```

2. Create a virtual environment and activate it
```
    python3 -m venv venv
    source venv/bin/activate  # or Windows use `venv\Scripts\activate`
```

3. Dependencies
```
    pip install -r requirements.txt
```

# To start the Application

python app.py


# To run the tests

pytest

# Endpoints

- `GET /movies`: Returns the list of films.
- `GET /producers`: Returns the producers with the largest interval and the smallest interval between consecutive awards.