# imports
from instapy import InstaPy
from instapy import smart_run
import os

tags = ["natgeo"]

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
# Script expects firefox to be a portable version located in 'firefox' folder
session = InstaPy(headless_browser=False,
                  browser_executable_path=os.getcwd() + "/firefox/firefox",
                  want_check_browser=False)

with smart_run(session):
  """ Activity flow """		
  
  # activity		
  session.like_by_tags(tags, amount=10)

