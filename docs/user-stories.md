# User Stories

Each story maps to a requirement in `requirements.md`.

## User Story 1 – Search for Trains

As a passenger, I want to search for trains by source, destination, and travel date, so that I can find a suitable train for my journey.

* **Priority:** High
* **Requirements:** FR-01, FR-03, NFR-01, NFR-02
* **Acceptance Criteria:**
  * Matching trains are listed for valid input.
  * A "no trains found" message is shown when nothing matches.
  * Same source and destination, unknown station, past date and empty fields are rejected with a clear message.
  * Results appear within 5 seconds.

## User Story 2 – Check Seat Availability

As a passenger, I want to check the availability of seats on a selected train, so that I can know whether I can book a seat for my journey.

* **Priority:** High
* **Requirements:** FR-02
* **Acceptance Criteria:**
  * Available seats are shown per class for the selected train and date.
  * "Waiting list" or "Not available" is shown when a class is full.
  * Counts reflect recent bookings and cancellations.

## User Story 3 – Book a Train Ticket

As a passenger, I want to book a ticket for a selected train and available seat, so that I can reserve my journey from my source to my destination.

* **Priority:** High
* **Requirements:** FR-04, FR-05, BR-01, NFR-03
* **Acceptance Criteria:**
  * Booking succeeds only if seats are available in the chosen class.
  * Name, age and gender are validated for every passenger.
  * A unique PNR is generated and shown on confirmation.
  * Available seats decrease by the number of tickets booked.
  * The same seat is never assigned to two passengers.
  * More than 6 passengers in one booking is rejected.

## User Story 4 – Cancel a Booking

As a passenger, I want to cancel my ticket using my PNR, so that I can get a refund if I no longer need my journey.

* **Priority:** High
* **Requirements:** FR-06, FR-08, BR-02, NFR-04
* **Acceptance Criteria:**
  * A valid PNR cancels the booking and releases the seat.
  * An invalid or already-cancelled PNR shows an error.
  * The system increases the available seat count for the cancelled seats.
  * The booking can only be cancelled up to 4 hours before scheduled departure.
  * The cancellation confirmation displays the PNR and refund amount.

## User Story 5 – View Refund Amount

As a passenger, I want to see my refund amount before confirming a cancellation, so that I know how much I will get back.

* **Priority:** Medium
* **Requirements:** FR-07, BR-02
* **Acceptance Criteria:**
  * The refund amount is calculated based on the ticket fare and cancellation rule.
  * The refund amount is displayed before the passenger confirms cancellation.
  * The passenger can decline the cancellation and keep the booking.
  * No refund is given if cancellation is requested after the train has departed.

## Backlog (not yet written)

* User Story 6 – Register and log in as a passenger
* User Story 7 – Admin: add and manage trains and schedules