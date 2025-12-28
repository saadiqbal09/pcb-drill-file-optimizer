from src.optimizer import calculate_total_distance


class DummyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_calculate_total_distance_empty():
    assert calculate_total_distance([]) == 0.0


def test_calculate_total_distance_two_points():
    points = [
        DummyPoint(0.0, 0.0),
        DummyPoint(3.0, 4.0),
    ]
    assert calculate_total_distance(points) == 5.0
