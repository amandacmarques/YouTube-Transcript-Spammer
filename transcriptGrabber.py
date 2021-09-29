from apiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import sys, pyautogui, time

if (len(sys.argv) != 3):
    raise ValueError("Please enter your Google API key and the video id you would like to spam!")

api_key = sys.argv[1]
channel_id = "X1rf8TSJ06s&ab_channel=_•CucumberR•_2.0."
youtube = build('youtube', 'v3', developerKey=api_key)
t = 5

try:
    responses = YouTubeTranscriptApi.get_transcript("X1rf8TSJ06s&ab_channel=_•CucumberR•_2.0.", languages=['en'])
    print(responses)
    for response in responses:
        time.sleep(t)
        if t > 0.75:
            t *= 0.5
        pyautogui.typewrite(response['text'])
        pyautogui.press('enter')
except Exception as e:
	print(e)