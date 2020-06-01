#you need to install this two libraries

from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build

import time

#pafy required youtube_dl library , so make sure you install youtube_dl library too
#i used pafy so that i could lower the number of queries
import pafy

stts = [0]

flow = InstalledAppFlow.from_client_secrets_file(
    #name of your oauth credential files ,please make that this file is in same directory
    'client_secret.json',
    #specific scopes url are defined for youtube data api related actions each action have specific action
    #this scopes let you edit , delete your youtube video
    scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])

credentials = flow.run_console()

youtube = build('youtube' , 'v3' ,credentials = credentials)

#this function return the views count 
def views_count():
    vid = pafy.new("https://youtu.be/h9N29ZLDGY0")
    views = vid.viewcount
    return views 

def changing_title():
    new_title = views_count()
    if new_title[0] > stts[0]:
        change = youtube.videos().update(part="snippet",body={
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
    time.sleep(300)
    changing_title()
    print(stts[0])

