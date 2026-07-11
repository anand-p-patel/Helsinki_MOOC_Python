# Enter you module contents here
"""Module for right-angled triangle calculations."""

__version__ = "1.0"
__author__ = "Anand"

import numpy

def hypotenuse(s1,s2):
    """Returns the length of the hypotenuse given two sides."""
    return numpy.hypot(s1,s2)


def area(s1,s2):
    """Returns the area of a right-angled triangle given two perpendicular sides."""
    return (1/2)*(s1)*(s2)