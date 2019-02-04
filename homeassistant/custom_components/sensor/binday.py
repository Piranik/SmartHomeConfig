"""
sensor:
  - platform: binday
      
"""
VERSION = '0.0.1'

import logging
import datetime

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.components.sensor.rest import RestData
from homeassistant.const import (STATE_UNKNOWN, STATE_OK, ATTR_ATTRIBUTION)
from homeassistant.exceptions import PlatformNotReady
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DEFAULT_ATTRIBUTION = 'Bin Day'