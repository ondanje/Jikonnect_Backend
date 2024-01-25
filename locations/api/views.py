from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from locations.models import County, SubCounty, Locality
from geopy.geocoders import Nominatim

class LocationHierarchyAPIView(generics.GenericAPIView):
    queryset = Locality.objects.none()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        geolocator = Nominatim(user_agent="jikonnect")  # Initialize the geolocator
        location_hierarchy = self.create_location_hierarchy(geolocator)  # Pass the geolocator instance
        return Response(location_hierarchy)
   
def create_location_hierarchy(self, geolocator):
    all_counties = County.objects.all()
    location_hierarchy = []

    for county in all_counties:
        county_data = {"county": county.name, "subcounties": []}

        for subcounty in SubCounty.objects.filter(county=county):
            subcounty_data = {"subcounty": subcounty.name, "localities": []}

            for locality in Locality.objects.filter(subcounty=subcounty):
                locality_data = {"locality": locality.name}

                # Get the coordinates of the locality
                location = self.get_coordinates(locality.name)

                if location:
                    locality_data["latitude"] = location[0]
                    locality_data["longitude"] = location[1]

                subcounty_data["localities"].append(locality_data)

            county_data["subcounties"].append(subcounty_data)

        location_hierarchy.append(county_data)

    return location_hierarchy
