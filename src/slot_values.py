"""Class containing types of slots and their values."""

from datetime import datetime

import pandas as pd


class Subject:
    """Class representing types and instances of subjects."""

    class Country:
        """Class representing instances of type Country."""

        def __init__(self):
            """Initialize the Country class."""
            self._values = None

        @property
        def values(self):
            """Return all countries."""
            if self._values is None:
                try:
                    df = pd.read_csv('resources/iso-3166.csv')
                    self._values = sorted(df['name'].to_numpy())
                except FileNotFoundError:
                    raise FileNotFoundError('File "resources/iso-3166.csv" not found.') from FileNotFoundError
            return self._values

    class Region:
        """Class representing instances of type Region."""

        def __init__(self):
            """Initialize the Region class."""
            self._values = None

        @property
        def values(self):
            """Return all unique regions."""
            if self._values is None:
                try:
                    df = pd.read_csv('resources/iso-3166.csv')
                    self._values = sorted(df['sub-region'].dropna().unique())
                except FileNotFoundError:
                    raise FileNotFoundError('File "resources/iso-3166.csv" not found.') from FileNotFoundError
            return self._values


class Property:
    """Class representing types of property."""

    @classmethod
    def values(cls):
        """Return valid properties."""
        return [
            'population',
            'GDP',
            'urban population',
            'rural population',
            'male population',
            'female population',
            'energy consumption',
            'renewable energy consumption',
            'hydro energy consumption',
            'solar energy consumption',
            'electricity output',
        ]


class Operation:
    """Class representing types of operation."""

    class Value:
        """Class representing 'value'/null operation."""

        @classmethod
        def values(cls):
            """Return no operation."""
            return ['']

    class NaryComparison:
        """Class representing comparison operations."""

        @classmethod
        def values(cls):
            """Return comparison operations."""
            return ['highest', 'lowest']

    class BinaryComparison:
        """Class representing binary comparison operations."""

        @classmethod
        def values(cls):
            """Return binary comparison operations."""
            return ['higher', 'lower']

    class Aggregation:
        """Class representing aggregation operations."""

        @classmethod
        def values(cls):
            """Return aggregation operations."""
            return ['sum', 'average']


class Time:
    """Class representing types of time."""

    @classmethod
    def current_year(cls):
        """Return current year."""
        return datetime.now().year

    class Past:
        """Class representing types of past time."""

        @classmethod
        def values(cls):
            """Return past years."""
            current_year = Time.current_year()
            return [f'{year}' for year in range(current_year - 10, current_year)]

    class Future:
        """Class representing types of future time."""

        @classmethod
        def values(cls):
            """Return future years."""
            current_year = Time.current_year()
            return [f'{year}' for year in range(current_year + 1, current_year + 11)]


if __name__ == '__main__':
    print(Subject.Country().values)
    print(Subject.Region().values)
    print(Property.values())
    print(Operation.Value.values())
    print(Operation.NaryComparison.values())
    print(Operation.BinaryComparison.values())
    print(Operation.Aggregation.values())
    print(Time.Past.values())
    print(Time.Future.values())
    print(Time.current_year())
