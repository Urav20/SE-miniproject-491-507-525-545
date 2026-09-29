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

## 2. Non-Functional Requirements

### NFR-01 — Performance

**Requirement:**
The system shall return train search results within **5 seconds** in normal usage.

**Priority:** High

**Acceptance Criteria:**

* A valid train search request should return results within 5 seconds under normal operating conditions.
* The system should display an appropriate response if the search cannot be completed.
