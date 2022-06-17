import sys
import subprocess

streamers = ["PoppedBit"]

def main():
    url = getStreamUrl(streamers[0])
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