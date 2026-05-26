import io
import os
import sys
import unittest
import temperature_analyzer
import perth_comparator


class TestTemperatureAnalyzer(unittest.TestCase):
    """Test suite for temperature modules"""
    
    def setUp(self):
        self.input_file = "test_temp_input.txt"
        self.output_file = "test_temp_output.txt"
    
    def tearDown(self):
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        for f in [self.input_file, self.output_file]:
            if os.path.exists(f):
                os.remove(f)

    
     #equivalence partitioning part black box
    
    def test_ep_temp_above_average(self):
       
        result = temperature_analyzer.check_city_temperature("Perth", 25.0, "morning")
        self.assertIn("above", result, "25°C should be above Perth morning average (18.2°C)")
    

    def test_ep_temp_below_average(self):
       
        result = temperature_analyzer.check_city_temperature("Perth", 15.0, "morning")
        self.assertIn("below", result, "15°C should be below Perth morning average (18.2°C)")
    
    def test_ep_temp_equal_average(self):
        result = temperature_analyzer.check_city_temperature("Perth", 18.2, "morning")
        self.assertIn("same as", result, "18.2°C should equal Perth morning average")
    
    def test_ep_temp_significant_difference(self):
        
        result = temperature_analyzer.check_city_temperature("Perth", 30.0, "morning")
        self.assertIn("Significant difference", result, "30°C is >6° above average, should show warning")
    


    def test_ep_temp_no_significant_difference(self):
      
        result = temperature_analyzer.check_city_temperature("Perth", 20.0, "morning")
        self.assertNotIn("Significant difference", result, "20°C is only 1.8° above average, no warning")
    
    def test_ep_invalid_city(self):

        result = temperature_analyzer.check_city_temperature("Sydney", 25.0, "morning")
        self.assertEqual("Invalid city", result, "Sydney should return Invalid city")
    


    def test_ep_invalid_time(self):

        result = temperature_analyzer.check_city_temperature("Perth", 25.0, "evening")
        self.assertIn("Invalid time", result, "Evening should return invalid time message")
    
    def test_ep_temp_below_minimum(self):
       
        result = temperature_analyzer.check_city_temperature("Perth", -10.0, "morning")
        self.assertIn("below minimum", result, "-10°C is below Perth minimum (0.7°C)")
    

    def test_ep_temp_above_maximum(self):
       
        result = temperature_analyzer.check_city_temperature("Perth", 60.0, "morning")
        self.assertIn("above maximum", result, "60°C is above Perth maximum (46.0°C)")
    


      #boundary value analysistest black box
    
    def test_bva_temperature_6_degree_no_warning(self):
    
        result = temperature_analyzer.check_city_temperature("Perth", 24.2, "morning")
        self.assertNotIn("Significant difference", result, "24.2°C is exactly 6° above, no warning")


    def test_bva_temperature_6_degree_warning(self):
    
        result = temperature_analyzer.check_city_temperature("Perth", 24.3, "morning")
        self.assertIn("Significant difference", result, "24.3°C is 6.1° above, should warn")



    def test_bva_temperature_above_minimum(self):
    
        result = temperature_analyzer.check_city_temperature("Perth", 1.0, "morning")
        self.assertNotIn("below minimum", result, "1.0°C is above minimum")


    def test_bva_temperature_below_minimum(self):
 
       result = temperature_analyzer.check_city_temperature("Perth", 0.6, "morning")
       self.assertIn("below minimum", result, "0.6°C is below minimum")


    def test_bva_temperature_below_maximum(self):
    
       result = temperature_analyzer.check_city_temperature("Perth", 45.9, "morning")
       self.assertNotIn("above maximum", result, "45.9°C is below maximum")



    def test_bva_temperature_above_maximum(self):
    
        result = temperature_analyzer.check_city_temperature("Perth", 46.1, "morning")
        self.assertIn("above maximum", result, "46.1°C is above maximum")
    

     
     
     #perth comparison test
    
    def test_compare_warmer_than_perth(self):
        
        result = perth_comparator.compare_with_perth("Adelaide", 25.0, "afternoon") #test if else staement
        self.assertEqual("Adelaide is warmer than Perth", result, "25°C > Perth afternoon avg 23.0°C")
    

    def test_compare_cooler_than_perth(self):
        
        result = perth_comparator.compare_with_perth("Adelaide", 20.0, "afternoon")
        self.assertEqual("Adelaide is cooler than Perth", result, "20°C < Perth afternoon avg 23.0°C")
    
    def test_compare_same_as_perth(self):
        
        result = perth_comparator.compare_with_perth("Adelaide", 23.0, "afternoon")
        self.assertEqual("Adelaide is the same as Perth", result, "23°C equals Perth afternoon avg")
    
    def test_compare_invalid_city(self):
        
        result = perth_comparator.compare_with_perth("Sydney", 25.0, "afternoon")
        self.assertEqual("Invalid city", result, "Sydney should return Invalid city")
    

    def test_compare_invalid_time(self):
        
        result = perth_comparator.compare_with_perth("Adelaide", 25.0, "evening")
        self.assertEqual("Invalid time of day. Use morning or afternoon", result)

    

      #white box testing 
    
    def test_wb_if_elif_else_paths(self):


        result_above = temperature_analyzer.check_city_temperature("Perth", 25.0, "morning")  #test if else staement
        self.assertIn("above", result_above, "IF path: temperature above average")
        
        
        result_below = temperature_analyzer.check_city_temperature("Perth", 15.0, "morning")
        self.assertIn("below", result_below, "ELIF path: temperature below average")
        
       
        result_equal = temperature_analyzer.check_city_temperature("Perth", 18.2, "morning")
        self.assertIn("same as", result_equal, "ELSE path: temperature equals average")


    
    def test_wb_nested_if_significant_difference(self):
       

        result_large = temperature_analyzer.check_city_temperature("Perth", 30.0, "morning")   #testnested if else
        self.assertIn("Significant difference", result_large, "Nested IF entered: difference > 6")
        
        
        result_small = temperature_analyzer.check_city_temperature("Perth", 20.0, "morning")
        self.assertNotIn("Significant difference", result_small, "Nested IF skipped: difference <= 6")
    

    def test_wb_perth_comparison_paths(self):
        
        result_warmer = perth_comparator.compare_with_perth("Adelaide", 25.0, "afternoon")
        self.assertEqual("Adelaide is warmer than Perth", result_warmer)
        

        result_cooler = perth_comparator.compare_with_perth("Adelaide", 20.0, "afternoon")
        self.assertEqual("Adelaide is cooler than Perth", result_cooler)
        
       
        result_same = perth_comparator.compare_with_perth("Adelaide", 23.0, "afternoon")
        self.assertEqual("Adelaide is the same as Perth", result_same)
    
      
      
      #keyboard input test
    
    def test_keyboard_input_temperature(self):
        
        sys.stdin = io.StringIO("Perth\n25.0\nmorning\n")
        city = input().strip()
        temp = float(input().strip())
        time = input().strip()
        result = temperature_analyzer.check_city_temperature(city, temp, time)
        self.assertIn("above", result, "Keyboard input should return above average")
    
      
      
       #console output test
    
    def test_console_output_temperature(self):

        captured = io.StringIO()
        sys.stdout = captured

        temperature_analyzer.print_city_temperature("Perth", 25.0, "morning")
        
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("above", output, "Console output should show above average")
    

      #file input test
    
    def test_file_input_temperature(self):
 
        with open(self.input_file, "w") as f:
            f.write("Perth,25.0,morning")
        with open(self.input_file, "r") as f:
            data = f.read().strip().split(',')
            city, temp, time = data[0], float(data[1]), data[2]

        result = temperature_analyzer.check_city_temperature(city, temp, time)
        self.assertIn("above", result, "file input should return above average")
    
       
       
       #data type tests 
    
    def test_numeric_temperature_as_int(self):
      
        result = temperature_analyzer.check_city_temperature("Perth", 25, "morning")
        self.assertIn("25°C", result, "integer temperature should work")
    
    def test_numeric_temperature_as_float(self):
        
        result = temperature_analyzer.check_city_temperature("Perth", 25.5, "morning")
        self.assertIn("25.5°C", result, "float temperature should work")


        #string value return
    
    def test_string_return_value(self):
       
        result = temperature_analyzer.check_city_temperature("Perth", 25.0, "morning")
        self.assertIsInstance(result, str, "Temperature functions should return strings")

         
         #exception test part
    
    def test_exception_none_city(self):
      
        result = temperature_analyzer.check_city_temperature(None, 25.0, "morning")
        self.assertEqual("Invalid city", result, "None city should return error")

    
    def test_exception_empty_city(self):
        result = temperature_analyzer.check_city_temperature("", 25.0, "morning")
        self.assertEqual("Invalid city", result, "Empty city should return error")
    
    
    
     #student id tets

    #id 23590102 (digits: 1, 0, 2)
    #last name: Prathapasinghe
    
    def test_student_id_digit_1_temperature(self):
        """Student ID digit 1 as temperature (1.0°C)"""
        result = temperature_analyzer.check_city_temperature("Perth", 1.0, "morning")
        self.assertIn("below", result, "ID digit 1: 1.0°C should be below average")
    
    def test_student_id_digit_0_temperature(self):
        """Student ID digit 0 as temperature (0.0°C)"""
        result = temperature_analyzer.check_city_temperature("Perth", 0.0, "morning")
        self.assertIn("below minimum", result, "ID digit 0: 0.0°C is below Perth minimum")
    
    def test_student_id_digit_2_temperature(self):
        """Student ID digit 2 as temperature (2.0°C)"""
        result = temperature_analyzer.check_city_temperature("Perth", 2.0, "morning")
        self.assertIn("below", result, "ID digit 2: 2.0°C should be below average")
    
    def test_student_last_name_as_city(self):
        """Last name as city should be invalid"""
        result = temperature_analyzer.check_city_temperature("Prathapasinghe", 25.0, "morning")
        self.assertEqual("Invalid city", result, "Last name as city should return Invalid city")


if __name__ == "__main__":
    unittest.main()