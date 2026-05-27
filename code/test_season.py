import io
import os
import sys
import unittest
import season_finder
import season_comparator


class TestSeasonFinder(unittest.TestCase):
    
    
    def setUp(self):
        self.input_file = "test_input.txt"
        self.output_file = "test_output.txt"
    
    def tearDown(self):
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        for f in [self.input_file, self.output_file]:
            if os.path.exists(f):
                os.remove(f)


    
      #equivalence partitioning black box
    
    def test_ep_meteorological_summer(self):
        result = season_finder.get_meteorological_season("Australia", "January")
        self.assertEqual("Summer", result, "Australia in January should be Summer")

    
    def test_ep_meteorological_autumn(self):
        result = season_finder.get_meteorological_season("Australia", "April")
        self.assertEqual("Autumn", result, "Australia in April should be Autumn")
    
    def test_ep_meteorological_winter(self):
        result = season_finder.get_meteorological_season("Australia", "July")
        self.assertEqual("Winter", result, "Australia in July should be Winter")

    
    def test_ep_meteorological_spring(self):
        result = season_finder.get_meteorological_season("Australia", "October")
        self.assertEqual("Spring", result, "Australia in October should be Spring")

    
    def test_ep_invalid_country(self):
        result = season_finder.get_meteorological_season("Germany", "January")
        self.assertEqual("Invalid country", result, "Germany should return Invalid country")

    
    def test_ep_invalid_month(self):
        result = season_finder.get_meteorological_season("Australia", "XYZ")
        self.assertEqual("Invalid month", result, "XYZ should return Invalid month")

    
      #boundary value analysis  black box

    
    def test_bva_november_spring(self):
        result = season_finder.get_meteorological_season("Australia", "November")
        self.assertEqual("Spring", result, "November should be Spring")

    
    def test_bva_december_summer(self):
        result = season_finder.get_meteorological_season("Australia", "December")
        self.assertEqual("Summer", result, "December should be Summer")

    
      #traditional seasonal test 
    
    def test_traditional_birak(self):
        result = season_finder.get_traditional_season("Australia", "December")
        self.assertEqual("Birak", result, "December in Australia should be Birak")

    
    def test_traditional_non_australia(self):
        result = season_finder.get_traditional_season("Japan", "June")
        self.assertEqual("No traditional season for this country", result, 
                        "Japan should have no traditional season")
        
        
    
      #white box testing 
    
    def test_wb_if_path_valid_country(self):  #test if else staement
        result = season_finder.get_meteorological_season("Australia", "January")
        self.assertEqual("Summer", result, "IF path: valid country should return season")

    
    def test_wb_else_path_invalid_country(self):
        result = season_finder.get_meteorological_season("XYZ", "January")
        self.assertEqual("Invalid country", result, "ELSE path: invalid country should return error")

    
    def test_wb_loop_finds_match(self):
        result = season_finder.get_meteorological_season("Australia", "January")  #test loops
        self.assertEqual("Summer", result, "Loop should find Summer season")
    
    def test_wb_loop_no_match(self):
        result = season_finder.get_meteorological_season("Australia", "XYZ")
        self.assertEqual("Invalid month", result, "Loop should exit without match")

    
    
        #keyboard input test
    
    def test_keyboard_input(self):
        sys.stdin = io.StringIO("Australia\nJanuary\n")
        country = input().strip()
        month = input().strip()
        result = season_finder.get_meteorological_season(country, month)
        self.assertEqual("Summer", result, "Keyboard input should return Summer")

    
    #console output test
    
    def test_console_output(self):
        captured = io.StringIO()
        sys.stdout = captured
        season_comparator.check_seasons_same("Australia", "Japan", "January")
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Australia in January: Summer", output, 
                     "Console output should show Australia season")
                     
    
       #file input and output test
    
    def test_file_input(self):
    
       with open(self.input_file, "w") as f:
           f.write("Australia,January")
       with open(self.input_file, "r") as f:
           country, month = f.read().split(',')

          #test with production code

       result = season_finder.get_meteorological_season(country, month)
       self.assertEqual("Summer", result, "File input should return Summer")


       with open(self.output_file, "w") as f:  
         f.write(f"{country} in {month}: {result}\n")

    
       with open(self.output_file, "r") as f:
         content = f.read()
    
    
       self.assertIn("Australia", content)
       self.assertIn("Summer", content)
       self.assertIn("January", content) #file deleted afte test with teardown
    
   
       
    
       #exception tests
    
    def test_exception_none_country(self):
        result = season_finder.get_meteorological_season(None, "January")
        self.assertEqual("Invalid country", result, "None country should return error")
    
    def test_exception_empty_country(self):
        result = season_finder.get_meteorological_season("", "January")
        self.assertEqual("Invalid country", result, "Empty country should return error")
    
    def test_exception_none_month(self):
        result = season_finder.get_meteorological_season("Australia", None)
        self.assertEqual("Invalid month", result, "None month should return error")

    
    #numaric data tests
    
    def test_numeric_month_as_int(self):
        result = season_finder.get_meteorological_season("Australia", 1)
        self.assertEqual("Summer", result, "Month 1 (int) should be Summer")
    

    #boolean return value test
    
    def test_boolean_return_value(self):
        result = season_comparator.check_seasons_same("Australia", "Japan", "January")
        self.assertIsInstance(result, bool, "Return value should be boolean")
    

    
     #student id tets

    #id 23590102 (digits: 1, 0, 2)
    #last name: Prathapasinghe

    
    def test_student_id_digit_1(self):
        result = season_finder.get_meteorological_season("Australia", 1)
        self.assertEqual("Summer", result, "ID digit 1: January = Summer")
    
    def test_student_id_digit_0(self):
        result = season_finder.get_meteorological_season("Australia", 0)
        self.assertEqual("Invalid month", result, "ID digit 0: Month 0 = Invalid")
    
    def test_student_id_digit_2(self):
        result = season_finder.get_meteorological_season("Australia", 2)
        self.assertEqual("Summer", result, "ID digit 2: February = Summer")
    
    def test_student_last_name_as_country(self):
        result = season_finder.get_meteorological_season("Prathapasinghe", "January")
        self.assertEqual("Invalid country", result, "Last name as country = Invalid")


if __name__ == "__main__":
    unittest.main()