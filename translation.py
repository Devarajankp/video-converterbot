class Translation(object):


#This will be appeared when anyone use start command

      START = """Hello {0}

I can convert file to video or video to file with custom thumbnail support. {1}
"""


#This will be appeared when anyone use help command

      HELP = """**Hey you need help 🤔 ?**

1. Send me the telegram file or video which you wanted to convert.

2. Send me the thumbnail(photo) optional.

3. Reply to video /converttofile for converting into file.

4. Reply to file /converttovideo for converting into video.

"""


#Please don't change this about command 🙏

      ABOUT = """
**📝 Language:** Python 3

**🧰 Framework:** Pyrogram

**👨‍💻 Owner:** [KP](https://t.me/devarajankp)

**📮 Cloned from:** [Converter NS BOT](https://t.me/converter_Ns_bot)

**💻 Source Code:**[Press Me](https://github.com/devarajankp/yt-downloader)

"""

##############################################################################################################################
##############################################################################################################################


#DON'T CHANGE THE NUMBERS IN THE FLOWER BRACKETS AND THE ORDER OF PERCENTAGE, DONE, TOTAL, SPEED, ETA ONLY CHANGE THE THEME 

      PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
       
      DOWNLOAD_PROGRESS = "▪️"
      UPLOAD_PROGRESS = "▫️"

##############################################################################################################################
##############################################################################################################################

      DOWNLOAD_START = "Trying to Download 📥"
      DOWNLOAD_COMPLETE = "✅ Media Downloaded successfully\nPreparing for upload"
      UPLOAD_START = "Trying to Upload 📤"
      UPLOAD_COMPLETE = "THANKS FOR USING ME"
      SAVED_CUSTOM_THUMB_NAIL = "✅ Saved Thumbnail Successfully. This will be deleted in 24hrs"
      BANNED_TEXT = "YOU ARE BANNED. SO YOUR ARE NOT ABLE TO USE ME 🐒"
      REPLY_TEXT = "👩‍✈️ Reply to the media which you need to convert"
      DEL_ETED_CUSTOM_THUMB_NAIL = "Thumbnail Deleted Successfully ✅"
