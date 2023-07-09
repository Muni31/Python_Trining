# Create a class Shape with __init__, __repr__, __eq__, __gt__, __lt__ functions. 
# These functions should raise NotImplementedError when called with an object of Shape class. 
# Add valid docstrings containing description, and usage, parameter and return details as applicable. 

class Shape:
    """A class representing a generic shape."""

    def __init__(self):
        """Initializes a new instance of the Shape class. """
        raise NotImplementedError

    def __repr__(self):
        """Returns a string representation of the Shape object. """
        raise NotImplementedError

    def __eq__(self, other):
        """ Comparing two Shape objects for equality."""
        return NotImplementedError

    def __gt__(self, other):
        """Cheching if a Shape object is greater than another Shape object."""
        return NotImplementedError

    def __lt__(self, other):
        """Cheching if a Shape object is less than another Shape object."""
        return NotImplementedError
