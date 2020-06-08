from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build

import time

stts = [0]

api_key = "Your youtube data api token key"
flow = InstalledAppFlow.from_client_secrets_file(
    #name of your oauth credential files ,please make that this file is in same directory
    'client_secret.json',
    #specific scopes url are defined for youtube data api related actions each action have specific action
    #this scopes let you edit , delete your youtube video
    scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])

credentials = flow.run_console()

youtube = build('youtube' , 'v3' ,credentials = credentials ,developerKey = api_key)

#this function return the views count 
def views_count():
    request = youtube.videos().list(id='Youtube video id',part="statistics")
    pop = dict(request.execute())
    views = pop['items'][0]["statistics"]['viewCount']
    return views

def changing_title():
    new_title = int(views_count())
    if new_title[0] > stts[0]:
        change = youtube.videos().update(part="snippet",body={
            #id of your youtube video of which title will change 
            "id": "h9N29ZLDGY0",
            "snippet": {
    	   	"categoryId": 24,
    		"defaultLanguage": "en",
    		"description": "Salman saved his culture.",
    		"title": "Salman Khan slapped " +str(new_title[0])+ " times."
    	    }
    	  })
        change.execute()
        stts[0] = new_title[0]
    else:
        print("No changed exists")
#use while true for running it continuously
for t in range(10):
    changing_title()
    print(stts[0])
    time.sleep(900)
    

