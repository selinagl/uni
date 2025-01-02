import unittest
from Modul_5.Aufgabe_6.geonames_geocoder import GeoNamesGeocoder


class TestGeonamesGeocoder(unittest.TestCase):

    def setUp(self):
        self.geocoder = GeoNamesGeocoder()
        self.geocoder.user_name = "segl_108500"

    def test_slzbg(self):
        test_input = "Salzburg, Austria"
        expected_output = (47.79941, 13.04399)

        location_slzbg = self.geocoder.geocodeLocation(test_input)
        self.assertEqual(location_slzbg, expected_output)

    def test_none(self):
        test_input = "xyzblabla"
        expected_output = None

        location_none = self.geocoder.geocodeLocation(test_input)
        self.assertEqual(location_none, expected_output)


if __name__ == "__main__":
    unittest.main()
