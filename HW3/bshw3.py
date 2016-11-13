# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
import requests

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.parse, urllib.error

import urllib.request
html = urllib.request.urlopen('https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions').read()
soup = BeautifulSoup(html, 'html.parser')

soup2 = soup.prettify()


soup2= soup2.replace('https://www.youtube.com/embed/mimp_3gquc4?feature=oembed','fili.jpg')
soup2 = soup2.replace('student', "AMAZING student")
soup2 = soup2.replace('/sites/default/themes/umsi/imgs/logo_intranet.png','media/logo.png')

file = open("BSHW3_NEW.html",'w')
file.write(soup2)









# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
