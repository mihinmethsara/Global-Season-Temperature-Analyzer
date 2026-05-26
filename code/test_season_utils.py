import io
import os
import sys
import unittest
from season_utils import (
    get_meteorological_season,
    get_traditional_season,
    check_seasons_same
)


class TestSeasonUtils(unittest.TestCase):

    def setUp(self):
        self.input_file = "test_input.txt"
        self.output_file = "test_output.txt"

    def tearDown(self):
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        if os.path.exists(self.input_file):
            os.remove(self.input_file)

        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    # ---------- Black Box Tests ----------

    def test_meteorological_seasons(self):
        self.assertEqual(
            "Summer",
            get_meteorological_season("Australia", "January")
        )
        self.assertEqual(
            "Winter",
            get_meteorological_season("Australia", "July")
        )

    def test_invalid_inputs(self):
        self.assertEqual(
            "Invalid country",
            get_meteorological_season("Germany", "January")
        )
        self.assertEqual(
            "Invalid month",
            get_meteorological_season("Australia", "XYZ")
        )

    def test_month_numbers(self):
        self.assertEqual(
            "Summer",
            get_meteorological_season("Australia", 1)
        )
        self.assertEqual(
            "Summer",
            get_meteorological_season("Australia", "1")
        )

    def test_traditional_seasons(self):
        self.assertEqual(
            "Birak",
            get_traditional_season("Australia", "December")
        )
        self.assertEqual(
            "Makuru",
            get_traditional_season("Australia", "June")
        )

    def test_check_same_seasons(self):
        self.assertTrue(
            check_seasons_same("Australia", "Mauritius", "January")
        )
        self.assertFalse(
            check_seasons_same("Australia", "Japan", "January")
        )

    # ---------- Boundary Tests ----------

    def test_season_boundaries(self):
        self.assertEqual(
            "Spring",
            get_meteorological_season("Australia", "November")
        )
        self.assertEqual(
            "Summer",
            get_meteorological_season("Australia", "December")
        )

    # ---------- White Box Tests ----------

    def test_if_else_paths(self):
        self.assertEqual(
            "Summer",
            get_meteorological_season("Australia", "January")
        )

        self.assertEqual(
            "Invalid country",
            get_meteorological_season("XYZ", "January")
        )

    def test_loop_paths(self):
        self.assertEqual(
            "Summer",
            get_meteorological_season("Australia", "January")
        )

        self.assertEqual(
            "Invalid month",
            get_meteorological_season("Australia", "XYZ")
        )

    # ---------- Keyboard Input ----------

    def test_keyboard_input(self):
        sys.stdin = io.StringIO("Australia\nJanuary\n")

        country = input().strip()
        month = input().strip()

        result = get_meteorological_season(country, month)

        self.assertEqual("Summer", result)

    # ---------- Console Output ----------

    def test_console_output(self):
        captured = io.StringIO()
        sys.stdout = captured

        check_seasons_same("Australia", "Japan", "January")

        sys.stdout = sys.__stdout__

        output = captured.getvalue()

        self.assertIn("Australia", output)
        self.assertIn("Japan", output)

    # ---------- File Input ----------

    def test_file_input(self):
        with open(self.input_file, "w") as f:
            f.write("Australia,January")

        with open(self.input_file, "r") as f:
            country, month = f.read().split(",")

        result = get_meteorological_season(country, month)

        self.assertEqual("Summer", result)

    # ---------- File Output ----------

    def test_file_output(self):
        result = get_meteorological_season("Australia", "January")

        with open(self.output_file, "w") as f:
            f.write(result)

        with open(self.output_file, "r") as f:
            content = f.read()

        self.assertIn("Summer", content)

    # ---------- Exception Handling ----------

    def test_exception_handling(self):
        self.assertEqual(
            "Invalid country",
            get_meteorological_season("", "January")
        )

        self.assertEqual(
            "Invalid country",
            get_meteorological_season(None, "January")
        )

    # ---------- Data Types ----------

    def test_data_types(self):
        self.assertEqual(
            "Summer",
            get_meteorological_season("Australia", 1)
        )

        result = check_seasons_same(
            "Australia",
            "Japan",
            "January"
        )

        self.assertIsInstance(result, bool)


if __name__ == "__main__":
    unittest.main(verbosity=2)