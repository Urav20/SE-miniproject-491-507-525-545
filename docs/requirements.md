# Railway Reservation System — Requirements

## 1. Functional Requirements

### FR-01 — Train Search

**Requirement:**
The system shall allow a passenger to search for available trains by providing the source station, destination station, and travel date.

**Priority:** High

**Acceptance Criteria:**

* The passenger can enter a source station.
* The passenger can enter a destination station.
* The passenger can enter a travel date.
* The system displays trains matching the provided search criteria.
* If no matching train is available, the system displays an appropriate message.

---

### FR-02 — Check Seat Availability

**Requirement:**
The system shall allow a passenger to view the number of available seats for each class on a selected train and travel date.

**Priority:** High

**Acceptance Criteria:**

* The passenger can select a train from the search results.
* The system displays available seats per class (e.g., Sleeper, 3AC, 2AC, 1AC).
* If no seats are available in a class, the system displays "Waiting list" or "Not available".
* Seat counts reflect the most recent bookings and cancellations.

---

### FR-03 — Search Input Validation

**Requirement:**
The system shall validate all train search inputs and reject invalid entries with a clear error message.

**Priority:** Medium

**Acceptance Criteria:**

* The system rejects a search where the source and destination stations are the same.
* The system rejects a station name that does not exist in the system.
* The system rejects a travel date in the past.
* The system rejects a search with any empty field and states which field is missing.

---

## 2. Non-Functional Requirements

### NFR-01 — Performance

**Requirement:**
The system shall return train search results within **5 seconds** in normal usage.

**Priority:** High

**Acceptance Criteria:**

* A valid train search request should return results within 5 seconds under normal operating conditions.
* The system should display an appropriate response if the search cannot be completed.

---

### NFR-02 — Usability

**Requirement:**
A first-time passenger shall be able to complete a train search without external help.

**Priority:** Medium

**Acceptance Criteria:**

* The search form has no more than three required fields.
* Error messages state what is wrong and how to fix it.
