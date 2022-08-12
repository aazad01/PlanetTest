
# Planet Explorer Test

Test the search functionality of a given city
Save the search location and update the Save search


## Installation
Python 3.8+

Install libraries with pip

```bash
  pip install -r "requirements.txt"
```

    
## Running Tests

To run tests, run the following command

```bash
  python -m pytest
```

### Testcases

Out of Scope:  Login Page

Pre-requisite: Login to Planet explorer (www.planet.com/explorer)

#### 1.  Search for and Save a city
- Click Search button
- Search for city: San francisco, CA
- Click Save search
- Update Save search

#### 2.  Verify Search Suggestions
- Click Search button
- Search for a city
- Verify suggestions match the grammer of the city
- Verify Saved Searches are also tagged as the top search results

#### 3. Negative Case
- Click Search button
- Enter non-existing location
- Verify no results show up or suggestions

## Authors

- [@aazad01](https://www.github.com/aazad01)

