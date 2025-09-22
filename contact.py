from pyscript import *

location = "16 Ibuna Street, San Juan City"
contact_main = "0726-52-93"
contact_mob = "0928-54-36"
email1 = "info@KainTayo.com"
email2 = "support@KainTayo.com"
email3 = "careers@KainTayo.com"
time_period = {"open":"8:00 AM", "close":"9:00 PM"}

# Display values in contact.html
display(location, target="location")

display(f"Main: {contact_main}", target="phone_main")
display(f"Mobile: {contact_mob}", target="phone_mobile")

display(email1, target="email1")
display(email2, target="email2")
display(email3, target="email3")

display(f"Open Daily: {time_period['open']} – {time_period['close']}", target="business_hours")
