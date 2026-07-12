"""Habitat management for zoo animals."""

from typing import List


class Habitat:
    """Represents a habitat section in the zoo."""

    def __init__(
        self,
        name: str,
        habitat_type: str,
        capacity: int,
        temperature: float,
        humidity: float,
    ):
        """Initialize a Habitat.

        Args:
            name: Habitat name (e.g., "Savanna Ridge")
            habitat_type: Type of habitat (savanna, rainforest, etc.)
            capacity: Maximum number of animals
            temperature: Temperature in Celsius
            humidity: Humidity percentage
        """
        self.name = name
        self.habitat_type = habitat_type
        self.capacity = capacity
        self.temperature = temperature
        self.humidity = humidity
        self.animals: List[str] = []  # List of animal names

    def add_animal(self, animal_name: str) -> bool:
        """Add an animal to the habitat.

        Args:
            animal_name: Name of the animal

        Returns:
            True if successful, False if habitat is full
        """
        if len(self.animals) < self.capacity:
            self.animals.append(animal_name)
            return True
        return False

    def remove_animal(self, animal_name: str) -> bool:
        """Remove an animal from the habitat.

        Args:
            animal_name: Name of the animal

        Returns:
            True if successful, False if animal not found
        """
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            return True
        return False

    def get_occupancy(self) -> float:
        """Get habitat occupancy percentage.

        Returns:
            Occupancy as a percentage
        """
        return (len(self.animals) / self.capacity) * 100

    def __repr__(self) -> str:
        return f"Habitat(name={self.name}, type={self.habitat_type}, occupancy={self.get_occupancy():.1f}%)"
