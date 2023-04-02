import os
import requests
from praw import Reddit

# Replace the following values with your Reddit API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
user_agent = 'your_user_agent'

# Set the target subreddit and download directory
subreddit_name = 'videos'
download_directory = 'downloaded_videos'

# Initialize the Reddit API client
reddit = Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

def download_video(url, filepath):
    response = requests.get(url)
    with open(filepath, 'wb') as file:
        file.write(response.content)

def main():
    # Get the most upvoted post from the target subreddit
    subreddit = reddit.subreddit(subreddit_name)
    top_post = subreddit.top('day', limit=1).next()

    # Generate the video filename
    filename = f"{subreddit_name}_{top_post.title}.mp4"
    filepath = os.path.join(download_directory, filename)

    # Download and save the video
    os.makedirs(download_directory, exist_ok=True)
    download_video(top_post.url, filepath)
    print(f"Downloaded video: {filepath}")

if __name__ == '__main__':
    main()
