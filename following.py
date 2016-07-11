# - *- coding: utf- 8 - *-
import json

with open("data.json") as json_file:    
    data = json.load(json_file)

user_list = []

for user in  data["users"]:
     user_list.append((str(user["screen_name"])))

def url_builder(accts,since_date,until_date):
     #establishing url modifiers
     from_acct = 'from%3A'
     or_acct = '%20OR%20from%3A'
     since_mod = '%20since%3A'
     until_mod = '%20until%3A'  
     acct_url = ''
     base_url = 'https://twitter.com/search?q='
     end_mod = '&src=typd&lang=en'
     
     #loop thru acct list
     for acct in accts:
          acct_url = acct_url+acct+or_acct
     
     acct_url = from_acct+acct_url
     acct_url = acct_url[:-15]
     
     #add date modifiers
     acct_url = acct_url+since_mod+since_date+until_mod+until_date
     acct_url = base_url+acct_url+end_mod     

     return acct_url

start = '2016-03-30'
end = '2016-04-29'
url_adv = url_builder(user_list,start,end)

print url_adv
