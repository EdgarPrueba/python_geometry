"""
Módulo geometry - Cálculos geométricos básicos.

Contiene operaciones para:
- Círculos (área, circunferencia)
- Rectángulos (área, perímetro)
- Triángulos (área, perímetro)
"""
from geometry.circle import area as circle_area, circumference as circle_circumference
from geometry.rectangle import area as rect_area, perimeter as rect_perimeter
from .triangle import *

__version__ = "1.0.0"
__author__ = "Tu Nombre"