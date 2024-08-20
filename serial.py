"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """
        Initialize the serial generator with a starting number.

        Args:
            start (int): The starting number for the serial generator.
        """
        self._start = start  # Original start value
        self._current = start  # Current value that will be incremented

    def generate(self):
        """
        Generate the next serial number.

        Returns:
            int: The next serial number.
        """
        number = self._current
        self._current += 1
        return number

    def reset(self):
        """
        Reset the serial generator to the original starting number.
        """
        self._current = self._start

