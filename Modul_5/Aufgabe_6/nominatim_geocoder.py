import geopy
from geocoding_service import GeocodingService

class NominatimGeocoder(GeocodingService):
    """Implements a geocoding service based on the Nominatim API (accessed via GeoPy)."""

    def __init__(self):
        """Initializes the user_name property to the empty string.
        """
        # call superclass constructor to set the attribution property
        super().__init__("Nominatim geocoding service accessed via GeoPy")

        self.user_name = ""

    def geocodeLocation(self, location):
        """Overwrites the method from GeocodingService, calling Nominatim via GeoPy to
        geocode a given location string.

        Parameters:
            location (string)    A location name (e.g. "Salzburg, Austria")

        Returns:
            lat-lon-tuple (float,float)  Geocoding result in case the service was able to geocode the location, else None
        """
        # perform the geocoding attempt
        g = geopy.geocoders.Nominatim(user_agent="test_script")
        result = g.geocode(location)

        # if the result is not None, we transform it from a geopy.point into a (lat,lon)-Tuple
        if result is not None:
            return result.point.latitude, result.point.longitude
        return None  # geocoding failed, so we return None