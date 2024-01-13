import os
import json


def extract_format_data(format_data):
    extension = format_data["ext"]
    format_name = format_data["format"]
    url = format_data["url"]
    return {
        "extension": extension,
        "format_name": format_name,
        "url": url
    }


def extract_video_data_from_url(url):
    command = f'youtube-dl "{url}" -j --no-playlist'
    output = os.popen(command).read()
    
    try:
        video_data = json.loads(output)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Raw output: {output}")
        return None

    title = video_data.get("title", "")
    formats = video_data.get("formats", [])
    thumbnail = video_data.get("thumbnail", "")
    
    formats = [extract_format_data(format_data) for format_data in formats]

    return {
        "title": title,
        "formats": formats,
        "thumbnail": thumbnail
    }
