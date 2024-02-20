import unittest
from console import HBNBCommand

class TestCreateCommand(unittest.TestCase):
    
    def setUp(self):
        self.cmd = HBNBCommand()

    def test_create_state(self):
        # Test creating a State object
        self.cmd.do_create("State name=\"California\"")
        output = self.cmd.stdout.getvalue().strip()
        self.assertIn("'name': 'California'", output)

        # Test creating another State object
        self.cmd.do_create("State name=\"Arizona\"")
        output = self.cmd.stdout.getvalue().strip()
        self.assertIn("'name': 'Arizona'", output)

    def test_create_place(self):
        # Test creating a Place object
        self.cmd.do_create("Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297")
        output = self.cmd.stdout.getvalue().strip()
        self.assertIn("'name': 'My little house'", output)
        self.assertIn("'number_rooms': 4", output)
        self.assertIn("'number_bathrooms': 2", output)
        self.assertIn("'max_guest': 10", output)
        self.assertIn("'price_by_night': 300", output)
        self.assertIn("'latitude': 37.773972", output)
        self.assertIn("'longitude': -122.431297", output)

if __name__ == '__main__':
    unittest.main()
