import sys
import subprocess
import requests

streamers = ["PoppedBit"]

def main():
    isLive = isChannelLive(streamers[0])
    # if isLive:
    #     url = getStreamUrl(streamers[0])
    #     openUrl(url)

# Pings a channel to find out if it is live
def isChannelLive(channel):
    url = getStreamUrl(channel)
    response = requests.get(url).content.decode('utf-8')
    print(response)

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