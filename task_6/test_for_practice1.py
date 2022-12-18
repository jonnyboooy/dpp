from pub_cmd import App
import unittest

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()

    # Тестирование функции вычисления пройденного расстояния
    def test_distance_calculation(self):
        self.assertEqual(self.app.distance_calculation([[0, 0],[3, 4]]), 5)

    # Тестирование функции вычисления времени движения
    def test_counting_drive_time(self):
        self.assertEqual(self.app.counting_drive_time([14],3.5), 4)

    # Тестирование функции вычисления угла поворота
    def test_angle_calculations(self):
        self.assertEqual(self.app.angle_calculations([[0.0, 5.0], [5.0, 5.0]]), 45)

    # Тестирование функции вычисления времени поворота
    def test_counting_angular_rotation_time(self):
        self.assertEqual(self.app.counting_angular_rotation_time([45], 30), 1.5)

if __name__ == '__main__':
    unittest.main()
