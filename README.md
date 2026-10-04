# Train Search Feature: Explained in Simple Words

## 1. What was built

A passenger types **where from**, **where to** and **which date**. The system:

1. **Checks the input is sensible** (no empty fields, real stations, not a past date).
2. **Finds the trains** that match.
3. **Sends the answer** back through a URL (API) so a UI can show it.

This covers requirements **FR-01** (train search), **FR-03** (input validation), **NFR-01** (fast results).

---

## 2. How the pieces fit together

```
UI (website form)
      |
      v
api.py       <- the URL the UI calls (the "waiter")
      |
      v
search.py    <- the actual logic: validate + find trains (the "chef")
      |
      v
data.py      <- the list of trains and stations (the "fridge")
```

Each file has **one job**. This is called *modular design*. If we change the data (say, to a database), we don't touch the logic.

---

## 3. Folder structure

```
SE-project-repo/
├── src/railway/
│   ├── __init__.py     (empty, marks the folder as a Python package)
│   ├── search.py       (logic)
│   ├── data.py         (sample trains and stations)
│   └── api.py          (the API endpoint)
├── tests/
│   ├── test_search.py  (tests for the logic)
│   └── test_api.py     (tests for the API)
├── .github/workflows/ci.yml   (automatic test runner on GitHub)
├── pytest.ini                 (tells pytest where code and tests are)
├── requirements.txt           (what the app needs: flask)
└── requirements-dev.txt       (what testing needs: pytest, pytest-cov)
```

---

## 4. `search.py`: the brain

### `Train`: a blueprint for one train

```python
@dataclass(frozen=True)
class Train:
    number, name, source, destination, departure, runs_on
```

Each train stores its number, name, from, to, departure time and `runs_on`, the weekdays it runs (0 = Monday ... 6 = Sunday).
`frozen=True` means once a train is created, nobody can accidentally change it.

### `SearchError`: our own error

When input is wrong, we raise this with a clear message like *"Travel date cannot be in the past."* The API catches it and shows the message to the user.

### `_clean(value)`: tidy up text

Removes extra spaces and makes it lowercase. So `"  BENGALURU "` and `"bengaluru"` are treated as the same station. The `_` at the start means it's a small helper used only inside this file.

### `validate_search(...)`: the bouncer (FR-03)

Checks in this order and stops at the first problem:

| # | Check | Error message |
|---|---|---|
| 1 | Source empty? | Source station is required. |
| 2 | Destination empty? | Destination station is required. |
| 3 | Date missing? | Travel date is required. |
| 4 | Source not a known station? | Unknown station: ... |
| 5 | Destination not a known station? | Unknown station: ... |
| 6 | Source same as destination? | Source and destination cannot be the same. |
| 7 | Date in the past? | Travel date cannot be in the past. |

The `today` parameter is there so tests can pretend today is a fixed date. That way the tests never break as real time passes.

### `search_trains(...)`: the finder (FR-01)

1. Calls `validate_search` first. If input is bad, it stops with an error.
2. Loops through all trains and keeps one only if **all three** are true:
   - the source matches
   - the destination matches
   - the train **runs on that weekday**
3. Returns the list. If nothing matches, the list is **empty**. That is how "no trains found" works.

---

## 5. `data.py`: sample data

```python
STATIONS = {"Bengaluru", "Chennai", "Mysuru", "Hyderabad"}
TRAINS = [ Train(...), Train(...), Train(...) ]
```

This is a **temporary** fake database so we can test. Later it can be replaced by a real database without changing `search.py`.

---

## 6. `api.py`: the endpoint for the UI

**What is an API endpoint?** A URL that the UI calls to get data instead of a human reading it.

```
GET /api/trains/search?source=Bengaluru&destination=Chennai&date=2026-10-07
```

**What the code does, step by step:**

1. Reads `source`, `destination`, `date` from the URL.
2. Converts the date text to a real date. Format must be `YYYY-MM-DD`, otherwise it returns an error.
3. Calls `search_trains(...)` from `search.py`.
4. Replies in **JSON** (a text format that every UI understands).

**The three possible replies:**

| Situation | HTTP code | Reply |
|---|---|---|
| Trains found | `200` | `{"trains": [ ... ]}` |
| No trains | `200` | `{"trains": [], "message": "No trains found for the given search."}` |
| Bad input | `400` | `{"error": "Travel date cannot be in the past."}` |

(`200` means OK. `400` means the user's request was wrong.)

`create_app()` builds the Flask web app. Putting it inside a function makes it easy to create a fresh copy for each test.

---

## 7. Tests: proof that it works

### `test_search.py`: 13 unit tests

A **unit test** checks one small piece alone.

- A valid search returns the right train
- Extra spaces and capital letters still work
- No match returns an empty list
- A train that doesn't run on that weekday is left out
- A train that does run on that weekday is included
- Today's date is allowed
- 7 bad-input cases: empty source, empty destination, missing date, unknown source, unknown destination, same source and destination, past date

### `test_api.py`: 6 integration tests

An **integration test** checks that the pieces work **together** (API + logic).

- Valid search returns 200 and a train
- No match returns 200 and an empty list with a message
- Missing source returns 400
- Missing date returns 400
- Wrong date format returns 400
- Past date returns 400

### Coverage: 100%

Coverage shows how much of the code the tests actually ran.
- **Line coverage:** every line was executed.
- **Branch coverage:** every `if` was tested both ways (true and false).

Our result for `search.py`: **100% lines, 100% branches**.

---

## 8. CI: the automatic robot (`ci.yml`)

**CI = Continuous Integration.** Every time someone pushes code or opens a pull request, GitHub automatically:

1. Sets up Python
2. Installs the dependencies
3. Runs all the tests
4. **Fails the check if coverage drops below 80%**

So broken code can't sneak into `main` without somebody noticing.

---

## 9. How to run it 

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt

# run tests with coverage
pytest --cov=src --cov-branch --cov-report=term-missing

# start the API
$env:PYTHONPATH="src"; python -m railway.api
```

Then open in a browser (use a future date):

```
http://127.0.0.1:5000/api/trains/search?source=Bengaluru&destination=Chennai&date=2026-10-07
```

---

## 10. Git work we did (for the evaluators)

| What | Why it matters |
|---|---|
| Issue created first (e.g. #5) | Shows planning and backlog use |
| Feature branch (`feature/train-search`) | Keeps `main` clean |
| Commit message with issue number | Links code to the task |
| Pull request with `Closes #5` | Shows code review flow, auto-closes the issue |
| CI check on the PR | Shows the automated pipeline |
----

