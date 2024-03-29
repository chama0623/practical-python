from src.valid_by_init_subclass import (Filled, Hexagon, Nonagon, Polygon,
                                        Rectangle, RedTriangle, Triangle)


def test_polygon():
    assert Triangle.interior_angles() == 180
    assert Rectangle.interior_angles() == 360
    assert Nonagon.interior_angles() == 1260
    assert Hexagon.interior_angles() == 720
    ruddy = RedTriangle()
    assert isinstance(ruddy, Filled)
    assert isinstance(ruddy, Polygon)
