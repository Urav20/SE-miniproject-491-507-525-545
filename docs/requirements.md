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

### FR-04 — Book Ticket

**Requirement:**
The system shall allow a registered passenger to book a ticket on a selected train, travel date and class by providing passenger details.

**Priority:** High

**Acceptance Criteria:**

* The passenger can book only if seats are available in the selected class.
* The passenger provides name, age and gender for each traveller.
* The system generates a unique PNR (booking reference) after a successful booking.
* The system reduces the available seat count for that class by the number of tickets booked.
* The system displays a booking confirmation with PNR, train, date, class and fare.

---

### FR-05 — Passenger Detail Validation

**Requirement:**
The system shall validate passenger details before confirming a booking.

**Priority:** Medium

**Acceptance Criteria:**

* The system rejects an empty passenger name.
* The system rejects an age that is not between 1 and 120.
* The system rejects a booking of more than 6 passengers in a single transaction.
* The system displays which field is invalid.

---

### BR-01 — Maximum Passengers per Booking

A single booking may contain at most 6 passengers.

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

---
### NFR-03 — Reliability

**Requirement:**
The system shall never assign the same seat to two different passengers for the same train, date and class.

**Priority:** High

**Acceptance Criteria:**

* Two simultaneous bookings for the last available seat result in exactly one confirmed booking.
* The second passenger receives a "No seats available" message.