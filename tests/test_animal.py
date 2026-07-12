"""Tests for Animal class."""

import pytest
from animals.animal import Animal


def test_animal_creation():
    """Test creating an animal."""
    animal = Animal(
        "Simba", "African Lion", "2018-03-15", "Savanna Ridge", 185.5
    )
    assert animal.name == "Simba"
    assert animal.species == "African Lion"
    assert animal.health_status == "healthy"


def test_feed_animal():
    """Test feeding an animal."""
    animal = Animal(
        "Rajah", "Bengal Tiger", "2019-01-10", "Tiger Territory", 215.0
    )
    animal.feed("meat", 5.0, "morning feeding")
    assert len(animal.feeding_log) == 1
    assert animal.feeding_log[0]["food_type"] == "meat"


def test_update_health_status():
    """Test updating health status."""
    animal = Animal("Panda", "Giant Panda", "2016-09-05", "Bamboo Forest", 98.5)
    animal.update_health_status("under observation", "routine checkup")
    assert animal.health_status == "under observation"
    assert len(animal.medical_log) == 1


def test_move_habitat():
    """Test moving animal to new habitat."""
    animal = Animal(
        "Kanga", "Red Kangaroo", "2020-11-12", "Outback", 78.0
    )
    original_habitat = animal.habitat
    animal.move_habitat("Outback North")
    assert animal.habitat != original_habitat
    assert animal.habitat == "Outback North"
