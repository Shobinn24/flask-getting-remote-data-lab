# Getting Remote Data Lab

## Overview
A Python class for retrieving and parsing remote JSON data via HTTP GET requests. The `GetRequester` class provides a simple interface for fetching data from web APIs and converting responses to Python data structures.

## Features
- HTTP GET request handling using the `requests` library
- JSON parsing and conversion to Python objects
- Clean, reusable class-based design

## Installation
```bash
# Clone the repository
git clone <your-repo-url>

# Navigate to project directory
cd flask-getting-remote-data-lab

# Install dependencies
pipenv install

# Activate virtual environment
pipenv shell
```

## Usage
```python
from lib.get_requester import GetRequester

# Initialize with API endpoint URL
url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
requester = GetRequester(url)

# Get raw response body (bytes)
raw_data = requester.get_response_body()

# Get parsed JSON data (Python objects)
json_data = requester.load_json()
print(json_data)
# Output: [{'name': 'Daniel', 'occupation': 'LG Fridge Salesman'}, ...]
```

## Implementation Details

### GetRequester Class

The `GetRequester` class provides two main methods:

- **`get_response_body()`**: Makes an HTTP GET request to the initialized URL and returns the raw response body as bytes
- **`load_json()`**: Fetches the data and parses it from JSON format into Python data structures (lists, dictionaries, etc.)

## Testing
```bash
# Run all tests
pytest lib/testing/get_requester_test.py

# Run with verbose output
pytest lib/testing/get_requester_test.py -v
```

## Project Structure
```
flask-getting-remote-data-lab/
├── lib/
│   ├── get_requester.py       # Main GetRequester class
│   └── testing/
│       ├── conftest.py        # Pytest configuration
│       └── get_requester_test.py  # Test suite
├── Pipfile                    # Dependencies
├── pytest.ini                 # Pytest settings
└── README.md                  # Documentation
```

## API Endpoint

This project uses a test endpoint provided by Flatiron School:
- **URL**: https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json
- **Returns**: JSON array of person objects with name and occupation fields

## Technologies Used
- Python 3.11+
- `requests` library for HTTP requests
- `json` library for JSON parsing
- `pytest` for testing

## Resources
- [HTTP GET Method - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [Python JSON Module](https://docs.python.org/3/library/json.html)

## License
This project is part of the Flatiron School curriculum.

## Author
Shobinn Clark - [GitHub Profile](https://github.com/shobinn24)
EOF