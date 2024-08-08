from enum import Enum


class Grades(Enum):
    pass


class GradesEU(Grades):
    MILLIMETER = 0, 'millimeter'
    CENTIMETER = 1, 'centimeter'
    METER = 2, 'meter'
    KILOMETER = 3, 'kilometer'


class Unit:
    def __init__(self, value, grade: Grades, metric_system):
        self.value = value
        self.grade = grade
        self.metric_system = metric_system

    def convert(self, to_grade: Grades):
        pass


class DifferenceEU(Enum):
    MILLIMETER_BETWEEN_CENTIMETER = 0, 10
    CENTIMETER_BETWEEN_METER = 1, 100
    METER_BETWEEN_KILOMETER = 2, 1000


class MetricsEU:
    MILLIMETER = 1
    CENTIMETER = MILLIMETER * 10
    METER = CENTIMETER * 100
    KILOMETER = METER * 1000

    UNITS = [
        MILLIMETER,
        CENTIMETER,
        METER,
        KILOMETER,
    ]

    BASE_UNIT = UNITS[0]

    def __init__(self, base_unit):
        self.base_unit = base_unit
