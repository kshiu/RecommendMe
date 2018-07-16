import requests
from .. import credentials

def get_video_title(video_id):
    base_url = "https://www.googleapis.com/youtube/v3/videos?part=id%2C+snippet&id={}&key={}"
    request_url = base_url.format(video_id, credentials.get_youtube_api_key())
    r = requests.get(request_url)
    json = r.json()
    return json["items"][0]["snippet"]["title"]