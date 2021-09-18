
# coding: utf-8

# In[2]:


import urllib.request as urllib2
import json
from datetime import datetime
from datetime import timedelta
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.geocoders import Nominatim


# In[46]:


class DataGetter:
    
    def __init__(self):
#         self.base_url = "http://api.open-notify.org/"
        pass
    
    def loc(self, url):
        try:
            """
            What does this do?
            
            Retrive live data from the API with time and location
            Parameters:
            -----------
        
            url (string): a valid url to call the API
        
            Returns:
            --------
            
            print the current location of ISS with latitude and longitude and time
        
            """
            # getting details from the API
            api_request = urllib2.Request(url)
            position = urllib2.urlopen(api_request)
            api_data = json.loads(position.read())
        
            print("The ISS current location at time",datetime.fromtimestamp(api_data["timestamp"]),                  " is", api_data["iss_position"]["latitude"],",",api_data["iss_position"]["longitude"],"\n")
            
        except urllib2.HTTPError as err:
            if err.code == 404:
                print ("Page not found!")
            elif err.code == 403:
                print ("Access denied!")
            else:
                print ("Something happened! Plesse check your URL", err.code)
            
        
        
    def people(self,url):
        try:
            """
            What does this do?
            
            Retrive live data of the onboard astronauts details
            Parameters:
            -----------
        
            url (string): a valid url to call the API
        
            Returns:
            --------
            
            print the astranauts names with their current craft name
        
            """
            
            api_request = urllib2.Request(url)
            astronauts = urllib2.urlopen(api_request)
            api_data = json.loads(astronauts.read())
            df = pd.DataFrame(api_data)
            df2 = pd.DataFrame(df["people"].values.tolist(),index=df.index)
            
            # extracting and printing people data
            val = df2["craft"].value_counts()
            list_of_crafts = df2["craft"].unique().tolist()
            
            # printing the astraunauts names with their craft name
            for i in range(len(list_of_crafts)):
                print(f"There are", val.tolist()[i] , "people abroad the" , val.index.tolist()[i] + ".",                      "They are" , (', '.join(df2.loc[df2['craft'] == list_of_crafts[i]]['name'].tolist())),"\n")
                
        except urllib2.HTTPError as err:
            if err.code == 404:
                print ("Page not found!")
            elif err.code == 403:
                print ("Access denied!")
            else:
                print ("Something happened! Plesse check your URL", err.code)

    def passover(self, url, zip_address):
        try:
            
            """
            What does this do?
            
            user input the location either as zip code or address as  'zip_address'
            
            Parameters:
            -----------
        
            url (string): a valid url to call the API
            zip_address(int or string): a valid zip code or an address
        
            Returns:
            --------
            
            print when the ISS will pass the given location and the duration
        
            """
            geolocator = Nominatim(user_agent="My-goelocation-application")
            location = geolocator.geocode(zip_address)
            
            # retrieve latitude and longitude of the given location
            a, b = location.latitude , location.longitude
            print(f"Your location is:",location.address, "where, latitude is",a,"and longitude is",b)
            
            # combine the latidude and longitude of the given location the to URL and retrieve ISS path data
            url = url + "?lat=" + str(a) +"&lon=" +str(b)
            req = urllib2.Request(url)
            pos = urllib2.urlopen(req)
            isspass = json.loads(pos.read())

            # retrieve and print ISS-pass details 
            over_head = isspass["response"][1]["risetime"]
            rising_time = datetime.fromtimestamp(over_head)
            pass_duration = timedelta(seconds= isspass["response"][1]["duration"])
            print(f"The ISS will be overhead",a ,b, "at", rising_time, "for", pass_duration,"duration","\n")
        
        except urllib2.HTTPError as err:
            if err.code == 404:
                print ("Page not found!")
            elif err.code == 403:
                print ("Access denied!")
            else:
                print ("Something happened! Plesse check your URL", err.code)
            
        
#     def url_creator(self, url, path):
#         return self.url + '/' + path
    
#     def pass_over(self, url, path, zip_address):
#         url = self.url_creator(path)
#         geolocator = Nominatim(user_agent="My-goelocation-application")
#         location = geolocator.geocode(zip_address)


# In[47]:


data_gtr = DataGetter()

iss_now_url = 'http://api.open-notify.org/iss-now.json'
passover_url = 'http://api.open-notify.org/iss-pass.json'
people_url = 'http://api.open-notify.org/astros.json'

data_gtr.loc(iss_now_url)
data_gtr.passover(passover_url , zip_address='akron')
data_gtr.people(people_url)

