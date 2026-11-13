# geometry.py


import math


def square_area(side_length: float) -> float:
    """
    Calculate the area of a square.

    Args:
    - side_length (float): the length of one side of the square.

    Returns:
    - float: the area of the square.
    """
    # returnem l' àrea del quadrat amb la longitud de costat donada
    return side_length ** 2


def rectangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
    - base_length (float): the length of the base of the rectangle.
    - height (float): the height of the rectangle.

    Returns:
    - float: the area of the rectangle.
    """
    # returnem l' àrea del rectangle amb la longitud de la base i l'altura donades
    return base_length * height


def triangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Args:
    - base_length (float): the length of the base of the triangle.
    - height (float): the height of the triangle.

    Returns:
    - float: the area of the triangle.
    """
    # returnem l' àrea del triangle amb la longitud de la base i l'altura donades
    return 0.5 * base_length * height


def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
    - radius (float): the radius of the circle.

    Returns:
    - float: the area of the circle
    """
    # returnem l' àrea del cercle amb el radi donat
    return math.pi * radius ** 2
