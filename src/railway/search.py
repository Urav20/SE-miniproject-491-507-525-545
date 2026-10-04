from dataclasses import dataclass
from datetime import date


class SearchError(ValueError):
    """Raised when a train search input is invalid."""


@dataclass(frozen=True)
class Train:
    number: str
    name: str
    source: str
    destination: str
    departure: str
    runs_on: tuple  # weekdays the train runs, 0 = Monday ... 6 = Sunday


def _clean(value):
    return (value or "").strip().lower()


def validate_search(source, destination, travel_date, stations, today=None):
    """Validate search input (FR-03). Returns cleaned (source, destination)."""
    today = today or date.today()
    src, dst = _clean(source), _clean(destination)

    if not src:
        raise SearchError("Source station is required.")
    if not dst:
        raise SearchError("Destination station is required.")
    if travel_date is None:
        raise SearchError("Travel date is required.")

    known = {s.lower() for s in stations}
    if src not in known:
        raise SearchError(f"Unknown station: {source}.")
    if dst not in known:
        raise SearchError(f"Unknown station: {destination}.")
    if src == dst:
        raise SearchError("Source and destination cannot be the same.")
    if travel_date < today:
        raise SearchError("Travel date cannot be in the past.")
    return src, dst


def search_trains(source, destination, travel_date, trains, stations, today=None):
    """Return trains matching the search (FR-01). Empty list if none match."""
    src, dst = validate_search(source, destination, travel_date, stations, today)
    return [
        t for t in trains
        if t.source.lower() == src
        and t.destination.lower() == dst
        and travel_date.weekday() in t.runs_on
    ]