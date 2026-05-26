import io
import os
import sys
import unittest
from temperature_utils import (
    check_city_temperature,
    compare_with_perth
)


class TestTemperatureUtils(unittest.TestCase):

    def setUp(self):
        self.input_file = "temp_input.txt"
        self.output_file = "temp_output.txt"

    def tearDown(self):
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        if os.path.exists(self.input_file):
            os.remove(self.input_file)

        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    # ---------- Black Box Tests ----------

    def test_temperature_above_average(self):
        result = check_city_temperature("Perth", 25.0, "morning")
        self.assertIn("ABOVE", result)

    def test_temperature_below_average(self):
        result = check_city_temperature("Perth", 15.0, "morning")
        self.assertIn("BELOW", result)

    def test_temperature_equal_average(self):
        result = check_city_temperature("Perth", 18.2, "morning")
        self.assertIn("equals", result.lower())

    def test_invalid_city(self):
        result = check_city_temperature("Sydney", 20.0, "morning")
        self.assertEqual("Invalid city", result)

    def test_invalid_time(self):
        result = check_city_temperature("Perth", 20.0, "evening")
        self.assertIn("Invalid time", result)

    # ---------- Perth Comparison ----------

    def test_compare_warmer_than_perth(self):
        result = compare_with_perth("Adelaide", 25.0, "morning")
        self.assertIn("warmer", result.lower())

    def test_compare_cooler_than_perth(self):
        result = compare_with_perth("Adelaide", 10.0, "morning")
        self.assertIn("cooler", result.lower())

    def test_compare_same_as_perth(self):
        result = compare_with_perth("Adelaide", 18.2, "morning")
        self.assertIn("same", result.lower())

    # ---------- Boundary Tests ----------

    def test_minimum_boundary(self):
        result = check_city_temperature("Perth", 0.6, "morning")
        self.assertIn("below minimum", result.lower())

        result = check_city_temperature("Perth", 0.7, "morning")
        self.assertIn("BELOW", result)

    def test_maximum_boundary(self):
        result = check_city_temperature("Perth", 46.1, "morning")
        self.assertIn("above maximum", result.lower())

    # ---------- White Box Tests ----------

    def test_if_else_paths(self):
        result = check_city_temperature("Perth", 25.0, "morning")
        self.assertNotIn("Invalid city", result)

        result = check_city_temperature("XYZ", 25.0, "morning")
        self.assertEqual("Invalid city", result)

    def test_temperature_paths(self):
        result = check_city_temperature("Perth", 25.0, "morning")
        self.assertIn("ABOVE", result)

        result = check_city_temperature("Perth", 15.0, "morning")
        self.assertIn("BELOW", result)

    # ---------- Keyboard Input ----------

    def test_keyboard_input(self):
        sys.stdin = io.StringIO("Perth\n25.5\nafternoon\n")

        city = input().strip()
        temp = float(input().strip())
        time = input().strip()

        result = check_city_temperature(city, temp, time)

        self.assertIn("ABOVE", result)

    # ---------- Console Output ----------

    def test_console_output(self):
        captured = io.StringIO()
        sys.stdout = captured

        result = check_city_temperature("Perth", 25.0, "morning")
        print(result)

        sys.stdout = sys.__stdout__

        output = captured.getvalue()

        self.assertIn("ABOVE", output)

    # ---------- File Input ----------

    def test_file_input(self):
        with open(self.input_file, "w") as f:
            f.write("25.5,Perth,afternoon")

        with open(self.input_file, "r") as f:
            temp_str, city, time = f.read().split(",")
            temp = float(temp_str)

        result = check_city_temperature(city, temp, time)

        self.assertIn("ABOVE", result)

    # ---------- File Output ----------

    def test_file_output(self):
        result = check_city_temperature("Perth", 25.0, "morning")

        with open(self.output_file, "w") as f:
            f.write(result)

        with open(self.output_file, "r") as f:
            content = f.read()

        self.assertIn("ABOVE", content)

    # ---------- Exception Handling ----------

    def test_exception_handling(self):
        result = check_city_temperature("", 25.0, "morning")
        self.assertEqual("Invalid city", result)

        result = check_city_temperature(None, 25.0, "morning")
        self.assertEqual("Invalid city", result)

    # ---------- Data Types ----------

    def test_data_types(self):
        result = check_city_temperature("Perth", 25, "morning")
        self.assertIn("ABOVE", result)

        self.assertIsInstance(result, str)

    # ---------- Student Data ----------

    def test_student_data(self):
        result = check_city_temperature("Perth", 1.0, "morning")
        self.assertIn("BELOW", result)

        result = check_city_temperature("Perth", 0.0, "morning")
        self.assertIn("below minimum", result.lower())

        result = check_city_temperature(
            "Prathapasinghe",
            25.0,
            "morning"
        )
        self.assertEqual("Invalid city", result)


if __name__ == "__main__":
    unittest.main(verbosity=2)