from datetime import date

import pytest

from railway.search import SearchError, Train, search_trains, validate_search

STATIONS = {"Bengaluru", "Chennai", "Mysuru"}
TODAY = date(2026, 10, 5)  # a Monday
TRAINS = [
    Train("12607", "Lalbagh Express", "Bengaluru", "Chennai", "06:00", (0, 1, 2, 3, 4, 5, 6)),
    Train("12008", "Shatabdi", "Bengaluru", "Mysuru", "07:00", (0, 2)),
]


def test_valid_search_returns_matching_train():
    result = search_trains("Bengaluru", "Chennai", date(2026, 10, 6), TRAINS, STATIONS, TODAY)
    assert [t.number for t in result] == ["12607"]


def test_search_is_case_insensitive_and_trims_spaces():
    result = search_trains("  bengaluru ", "CHENNAI", date(2026, 10, 6), TRAINS, STATIONS, TODAY)
    assert len(result) == 1


def test_no_matching_train_returns_empty_list():
    assert search_trains("Chennai", "Mysuru", date(2026, 10, 6), TRAINS, STATIONS, TODAY) == []


def test_train_not_running_on_that_weekday_is_excluded():
    # Shatabdi runs Mon and Wed only; 6 Oct 2026 is a Tuesday
    assert search_trains("Bengaluru", "Mysuru", date(2026, 10, 6), TRAINS, STATIONS, TODAY) == []


def test_train_running_on_that_weekday_is_included():
    result = search_trains("Bengaluru", "Mysuru", date(2026, 10, 7), TRAINS, STATIONS, TODAY)
    assert [t.number for t in result] == ["12008"]


def test_today_is_allowed():
    assert validate_search("Bengaluru", "Chennai", TODAY, STATIONS, TODAY) == ("bengaluru", "chennai")


@pytest.mark.parametrize(
    "source,destination,travel_date,message",
    [
        ("", "Chennai", date(2026, 10, 6), "Source station is required"),
        ("Bengaluru", "", date(2026, 10, 6), "Destination station is required"),
        ("Bengaluru", "Chennai", None, "Travel date is required"),
        ("Atlantis", "Chennai", date(2026, 10, 6), "Unknown station"),
        ("Bengaluru", "Atlantis", date(2026, 10, 6), "Unknown station"),
        ("Chennai", "Chennai", date(2026, 10, 6), "cannot be the same"),
        ("Bengaluru", "Chennai", date(2026, 10, 1), "in the past"),
    ],
)
def test_invalid_input_is_rejected(source, destination, travel_date, message):
    with pytest.raises(SearchError, match=message):
        search_trains(source, destination, travel_date, TRAINS, STATIONS, TODAY)