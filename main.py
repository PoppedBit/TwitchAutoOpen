import sys
import subprocess
import requests


def main():

    # Make sure a username is passed in.
    if(len(sys.argv) < 2):
        print("The username of a streamer is required as an argument, none provided")
        return

    streamer = sys.argv[1]
    isLive = isChannelLive(streamer)
    if isLive:
        openStream(streamer)

# Pings a channel to find out if it is live
def isChannelLive(channel):
    url = getStreamUrl(channel)
    response = requests.get(url).content.decode('utf-8')
    return 'isLiveBroadcast' in response

# Opens channel in browser
def openStream(userName):
    url = getStreamUrl(userName)
    openUrl(url)

# Given a URL, open it in the default browser
def openUrl(url):
    if sys.platform=='win32':
        os.startfile(url)
    elif sys.platform=='darwin':
        subprocess.Popen(['open', url])
    else:
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            print('Unable to open url: '+url)

# Given a Twitch streamer's username, return the URL to their channel
def getStreamUrl(userName):
    return "https://www.twitch.tv/"+userName


if __name__ == "__main__":
    main()