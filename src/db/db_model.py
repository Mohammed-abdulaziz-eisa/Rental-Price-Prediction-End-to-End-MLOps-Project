"""
This module is used for creating the database model for the rent apartment data.

Classes:
    - Base : Base class for the database model.
    - RentApartments : Database model for rent apartment data.

"""

# third-part library
from sqlalchemy import REAL, INTEGER, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# local application imports
from config.config import settings


class Base(DeclarativeBase):
    """Base class for ORM model."""

    pass


class RentApartments(Base):
    """
    ORM model representating the RentApartments table in the database.

    Attributes:
        address (str): The address of the apartment (Primary Key).
        area (float): The area the apartment in square meters.
        constraction_year (int): The year of the construction of the apartment.
        rooms (int): The number of rooms in the apartment.
        bedrooms (int): The number of the bedrooms in the apartment.
        bathrooms (int): The number of the bathrooms in the apartment.
        balcony (str): The balcony status of the apartment.
        storage (str): The storage status of the apartment.
        parking (str): The parking status of the apartment.
        furnished (str): The furnished status of the apartment.
        garage (str): The garage status of the apartment.
        garden (str): The garden status of the apartment.
        energy (str): The energy label of the apartment.
        facilities (str): Additional facilities in or near the apartment.
        zip (str): The postal code of the apartment.
        neighborhood (str): The neighborhood where the apartment is located.
        rent (int): The rent price of the apartment.
    """

    __tablename__ = settings.rent_apart_table_name

    address: Mapped[str] = mapped_column(VARCHAR(), primary_key=True)
    area: Mapped[float] = mapped_column(REAL())
    constraction_year: Mapped[int] = mapped_column(INTEGER())
    rooms: Mapped[int] = mapped_column(INTEGER())
    bedrooms: Mapped[int] = mapped_column(INTEGER())
    bathrooms: Mapped[int] = mapped_column(INTEGER())
    balcony: Mapped[str] = mapped_column(VARCHAR())
    storage: Mapped[str] = mapped_column(VARCHAR())
    parking: Mapped[str] = mapped_column(VARCHAR())
    furnished: Mapped[str] = mapped_column(VARCHAR())
    garage: Mapped[str] = mapped_column(VARCHAR())
    garden: Mapped[str] = mapped_column(VARCHAR())
    energy: Mapped[str] = mapped_column(VARCHAR())
    facilities: Mapped[str] = mapped_column(VARCHAR())
    zip: Mapped[str] = mapped_column(VARCHAR())
    neighborhood: Mapped[str] = mapped_column(VARCHAR())
    rent: Mapped[int] = mapped_column(INTEGER())
