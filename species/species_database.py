"""Species information database."""

from typing import Dict, List, Optional


class Species:
    """Represents a species with taxonomic and care information."""

    def __init__(
        self,
        name: str,
        scientific_name: str,
        family: str,
        diet: str,
        avg_weight: float,
        avg_lifespan: int,
        habitat_type: str,
    ):
        """Initialize a Species.

        Args:
            name: Common name
            scientific_name: Scientific binomial name
            family: Taxonomic family
            diet: Type of diet (herbivore, carnivore, omnivore)
            avg_weight: Average weight in kg
            avg_lifespan: Average lifespan in years
            habitat_type: Natural habitat type
        """
        self.name = name
        self.scientific_name = scientific_name
        self.family = family
        self.diet = diet
        self.avg_weight = avg_weight
        self.avg_lifespan = avg_lifespan
        self.habitat_type = habitat_type

    def __repr__(self) -> str:
        return f"Species(name={self.name}, family={self.family})"


class SpeciesDatabase:
    """Manages a database of species."""

    def __init__(self):
        """Initialize the species database."""
        self.species: Dict[str, Species] = {}
        self._populate_default_species()

    def _populate_default_species(self) -> None:
        """Populate database with common zoo animals."""
        default_species = [
            Species(
                "African Lion",
                "Panthera leo",
                "Felidae",
                "carnivore",
                190.0,
                15,
                "savanna",
            ),
            Species(
                "African Elephant",
                "Loxodonta africana",
                "Elephantidae",
                "herbivore",
                6000.0,
                65,
                "savanna",
            ),
            Species(
                "Bengal Tiger",
                "Panthera tigris tigris",
                "Felidae",
                "carnivore",
                220.0,
                15,
                "rainforest",
            ),
            Species(
                "Giant Panda",
                "Ailuropoda melanoleuca",
                "Ursidae",
                "herbivore",
                100.0,
                20,
                "forest",
            ),
            Species(
                "Red Kangaroo",
                "Macropus rufus",
                "Macropodidae",
                "herbivore",
                85.0,
                18,
                "grassland",
            ),
        ]

        for species in default_species:
            self.add_species(species)

    def add_species(self, species: Species) -> None:
        """Add a species to the database.

        Args:
            species: Species object to add
        """
        self.species[species.name] = species

    def get_species(self, name: str) -> Optional[Species]:
        """Retrieve a species by name.

        Args:
            name: Species name

        Returns:
            Species object or None if not found
        """
        return self.species.get(name)

    def list_all_species(self) -> List[Species]:
        """Get all species in the database.

        Returns:
            List of all Species objects
        """
        return list(self.species.values())

    def filter_by_diet(self, diet: str) -> List[Species]:
        """Filter species by diet type.

        Args:
            diet: Diet type (herbivore, carnivore, omnivore)

        Returns:
            List of matching Species objects
        """
        return [s for s in self.species.values() if s.diet == diet]

    def filter_by_habitat(self, habitat_type: str) -> List[Species]:
        """Filter species by habitat type.

        Args:
            habitat_type: Habitat type

        Returns:
            List of matching Species objects
        """
        return [s for s in self.species.values() if s.habitat_type == habitat_type]
