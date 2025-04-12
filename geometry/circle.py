import math

def area(radius):
    """Calcula el área de un círculo.
    
    :param radius: Radio del círculo (debe ser positivo)
    :type radius: float
    :return: Área del círculo
    :rtype: float
    :raises ValueError: Si el radio es negativo
    
    Ejemplo:
    >>> area(3.0)
    28.274333882308138
    """
    if radius < 0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * radius ** 2

def circumference(radius):
    """Calcula la circunferencia de un círculo."""
    return 2 * math.pi * radius
