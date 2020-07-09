from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build

import time

old_view_count = 0
api_key = "your token"

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])

credentials = flow.run_console()

youtube = build('youtube' , 'v3' , developerKey = api_key ,credentials = credentials)

def views_count():
    request = youtube.videos().list(id="video id",part="statistics")
    view_out = dict(request.execute())
    total_count = view_out['items'][0]["statistics"]['viewCount']
    return total_count


def changing_title():
    global old_view_count
    new_view_count = int(views_count())
    if new_view_count > old_view_count :
        change = youtube.videos().update(part="snippet",body={
            "id": "video id",
            "snippet": {
    	   	"categoryId": 24,
    		"defaultLanguage": "en",
    		"description": "Salman saved his culture.",
    		"title": "Salman Khan slapped a women " +format(new_view_count , ',')+ " times "
    	    }
    	  })
        change.execute()
        old_view_count = new_view_count
        print("title updated")
    else:
        pass

    runtime = True
try:
   while True:
    changing_title()
    time.sleep(900)
except Exception as e:
    time.sleep()

    

