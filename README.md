# Planet Explorer Test

Test the search functionality of a given city
Save the search location and update the Save search

Project was written using selenium and pytest.

## Installation

Python 3.8+

Install libraries with pip

```bash
  pip install -r "requirements.txt"
```

## Running Tests

To run tests, run the following command

To run on a single login per class, use:

```bash
  pytest
```

To run in parallel, use:

```bash
  pytest -n 4
  *NOTE:  Tests aren't ramped/delayed, hence 4 is the max the application allows for stable tests.
```

### Testcases

Out of Scope:  Login Page

Pre-requisite: Login to Planet explorer (www.planet.com/explorer)

#### 1. Search for and Save a city

- Click Search button
- Search for city: San francisco, CA
- Click Save search
    - a. Save a New Search
    - b. Update Save search

#### 2. Verify Search Suggestions

- Click Search button
- Search for a city
- Verify suggestions match the grammer of the city
- Verify Saved Searches are also tagged as the top search results

#### 3. Negative Case

- Click Search button
- Enter non-existing location
- Verify no results show up or suggestions

#### 4. Delete Save Searches

- Click Save Search
- Delete the save searches

## Discovered Issues

#### 1. Saved Search name has a character limit

#### 2. Searches of less than 5 characters, i.e Miami would return results in Philippines.

#### 3. The implicit waits is a little flaky at around when the Save Search is clicked and when suggestions are displayed.

## Author

- [@aazad01](https://www.github.com/aazad01)

