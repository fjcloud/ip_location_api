## ip_location.py

from ip2geotools.databases.noncommercial import DbIpCity
from typing import Optional

class IPGeolocationError(Exception):
    """Custom exception for errors in IPGeolocation"""

class IPGeolocation:
    def __init__(self, ip: str):
        self.ip = ip
        self.city = None

    def get_location(self) -> Optional[str]:
        try:
            response = DbIpCity.get(self.ip, api_key='free')
            self.city = response.city
            return self.city
        except Exception as e:
            raise IPGeolocationError(f"An error occurred: {e}")
