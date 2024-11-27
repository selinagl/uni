class GeocodingService:
    """Abstract class describing the common interface of a geocoder based on 
    some public service

    Attributes:
        attribution (string)    A String describing the service used
    """

    def __init__(self, attribution):
        """Sets the attribution property to the given string parameter
        """
        self.attribution = attribution

    def configure(self):
        """To be overwritten by derived classes: Ask user for input 
        values needed to use the given service (e.g. user name).
        """
        pass  # do nothing; we leave it to the subclasses to define their specialized behavior

    def geocodeLocation(self, location):
        """To be overwritten by derived classes: Geocode a location string and return
        the result as a (lat,lon) tuple.

        Parameters: 
            location (string)    A location name (e.g. "Salzburg, Austria")

        Returns:
            lat-lon-tuple (float,float)  Geocoding result in case the service was able to geocode the location, else None
        """
        pass  # do nothing; we leave it to the subclasses to define their specialized behavior