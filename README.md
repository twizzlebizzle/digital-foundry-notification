# Digital Foundary Notification
Checks the digital foundary website for new videos and pushes the notification to my phone via the Pushover API, including the link

----
I wanted to get alerts when a new video is available to download/viea from the digital foundary website, I typically check this manually.

I'm still learning, any tips would be appreciated, future improvements will be to:
- Use SQLite3 to store the list of videos (not necessary but want to practise using it)
- <s>Move pushover tokens to another file</s>
- Implement email/discord options
- Use auth to automatically download the videos to a file of my choosing (useful with plex)

How to install.
- Clone the gihub
- install the requirements.txt through pip
- Add your auth tokens for pushover in a file called "pushover_auth.txt", in the format:

```
token [TOKEN HERE]
user [TOKEN HERE]
```

- Run it on a crontab - I suggest 10m intervals */10 * * * *
- When run as a crontab you need to hardcode the videos.txt page - eg /home/user/digital-foundry-notification/videos.txt
- Crontab doesn't know the current directory.
