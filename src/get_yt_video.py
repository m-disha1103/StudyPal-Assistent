import os
import requests
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def get_yt_video_link(query):
    """Search YouTube and return 3 video titles and links."""

    if not YOUTUBE_API_KEY:
        return [], []

    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 3,
        "key": YOUTUBE_API_KEY,
        "regionCode": "IN",
        "relevanceLanguage": "en"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        video_titles = []
        video_links = []

        for item in data.get("items", []):
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]

            video_titles.append(title)
            video_links.append(
                f"https://www.youtube.com/watch?v={video_id}"
            )

        return video_titles, video_links

    except requests.RequestException as e:
        print(f"YouTube API error: {e}")
        return [], []