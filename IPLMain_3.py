# Alias
from IPL2021 import venue
from IPL2021.KKR import venue as KKRModule
from IPL2021.RCB import venue as RCBModule


venue.printVenue()

KKRModule.printVenue()
RCBModule.printVenue()

# Approach 2

from IPL2021.venue import printStadium as defStadium
from IPL2021.KKR.venue import printStadium as KKRStadium
from IPL2021.RCB.venue import printStadium as RCBStadium

# printStadium

defStadium()
KKRStadium()
RCBStadium()