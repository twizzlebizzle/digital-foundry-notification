# Digital Foundary Notification
Checks the digital foundary website for new videos and pushes the notification to my phone via the Pushover API, including the link

----
I wanted to get alerts when a new video is available to download/viea from the digital foundary website, I typically check this manually.

I'm still learning, any tips would be appreciated, future improvements will be to:
- Use SQLite3 to store the list of videos (not necessary but want to practise using it)
- Move pushover tokens to another file
- Implement email/discord options
- Use auth to automatically download the videos to a file of my choosing (useful with plex)

How to install.
- Clone the gihub
- install the requirements.txt through pip
- Add your auth tokens from pushover
- Run it on a crontab - I suggest 10m intervals */10 * * * *
