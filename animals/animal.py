"""Base Animal class for zoo management system."""

from datetime import datetime
from typing import Optional


class Animal:
    """Represents an individual animal in the zoo."""

    def __init__(
        self,
        name: str,
        species: str,
        date_of_birth: str,
        habitat: str,
        weight: float,
        health_status: str = "healthy",
    ):
        """Initialize an Animal.

        Args:
            name: Animal's name
            species: Species of the animal
            date_of_birth: Birth date (YYYY-MM-DD)
            habitat: Current habitat assignment
            weight: Weight in kilograms
            health_status: Current health status
        """
        self.name = name
        self.species = species
        self.date_of_birth = date_of_birth
        self.habitat = habitat
        self.weight = weight
        self.health_status = health_status
        self.feeding_log = []
        self.medical_log = []

    def feed(self, food_type: str, amount: float, notes: Optional[str] = None) -> None:
        """Record a feeding event.

        Args:
            food_type: Type of food given
            amount: Amount in kilograms
            notes: Optional feeding notes
        """
        entry = {
            "timestamp": datetime.now(),
            "food_type": food_type,
            "amount": amount,
            "notes": notes,
        }
        self.feeding_log.append(entry)

    def update_health_status(self, status: str, notes: Optional[str] = None) -> None:
        """Update animal's health status.

        Args:
            status: New health status
            notes: Optional medical notes
        """
        self.health_status = status
        entry = {
            "timestamp": datetime.now(),
            "status": status,
            "notes": notes,
        }
        self.medical_log.append(entry)

    def move_habitat(self, new_habitat: str) -> None:
        """Move animal to a different habitat.

        Args:
            new_habitat: New habitat assignment
        """
        self.habitat = new_habitat

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, species={self.species}, habitat={self.habitat})"
