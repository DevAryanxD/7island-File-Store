class script(object):
    START_TXT = """<b>ʜᴇʏ {}, ɪ ᴀᴍ {} 👋, ɪ ᴀᴍ ʟᴀᴛᴇꜱᴛ & ᴍᴏsᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ, ғᴀsᴛᴇʀ ᴛʜᴀɴ ᴇᴠᴇʀ ᴡɪᴛʜ ʙᴀᴛᴄʜ sᴜᴘᴘᴏʀᴛ
    
🔋 ᴡᴏʀᴋɪɴɢ ᴜɴᴅᴇʀ - <a href=https://t.me/x7islandDevs>@x𝟽ɪsʟᴀɴᴅᴅᴇᴠs</a></b>"""

    CAPTION = """<b>{file_caption}</b>""" 

    SHORTENER_API_MESSAGE = """<b>ᴛᴏ ᴀᴅᴅ ᴏʀ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ API, /api (ᴀᴘɪ)
            
<b>Ex: /api 𝟼LZǫ𝟾𝟻𝟷sXᴏғғғPHᴜɢɪKQǫ

<b>Cᴜʀʀᴇɴᴛ Wᴇʙsɪᴛᴇ: {base_site}

Cᴜʀʀᴇɴᴛ Sʜᴏʀᴛᴇɴᴇʀ API:</b> `{shortener_api}`

If You Want To Remove Api Then Copy This And Send To Bot - `/api None`"""

    CLONE_START_TXT = """<b>ʜᴇʟʟᴏ {}, ᴍʏ ɴᴀᴍᴇ {} 👋, ɪ ᴀᴍ ʟᴀᴛᴇꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ᴘᴏᴡᴇʀꜰᴜʟ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ + ᴄᴜꜱᴛᴏᴍ ᴜʀʟ ꜱʜᴏʀᴛɴᴇʀ ꜱᴜᴘᴘᴏʀᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ sᴜᴘᴘᴏʀᴛ ᴀɴᴅ ʙᴇꜱᴛ ᴜɪ ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇ

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ᴛʜᴇɴ ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ ᴄʟᴏɴᴇ ʙᴏᴛ ғʀᴏᴍ ᴍʏ <a href=https://t.me/x7islandDevs>ᴘᴀʀᴇɴᴛ</a></b>"""

    ABOUT_TXT = """<b>ʜɪ ɪ ᴀᴍ ᴘᴇʀᴍᴀɴᴇɴᴛ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ,, ᴡᴏʀᴋɪɴɢ ᴜɴᴅᴇʀ 𝟽ɪsʟᴀɴᴅ ᴄᴏʀᴘᴏʀᴀᴛɪᴏɴ, ʜᴏsᴛᴇᴅ ᴏɴ sᴜᴘᴇʀғᴀsᴛ ᴠᴘs sᴇʀᴠᴇʀ

🤖 ᴍʏ ɴᴀᴍᴇ: {}

📝 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>ᴘʏᴛʜᴏɴ𝟹</a>

📚 ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org>ᴘʏʀᴏɢʀᴀᴍ</a>

🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/MoggerKing>ᴛᴇᴀᴍ 𝟽ɪsʟᴀɴᴅ</a>

👥 ɪɴsᴛᴀ ᴄᴏᴍ: <a href=https://instagram.com/@7stoical>ᴄᴏᴍᴍᴜɴɪᴛʏ</a>

📢 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href=https://t.me/x7islandDevs>𝟽ɪsʟᴀɴᴅ</a></b>
"""

    CABOUT_TXT = """<b>ʜɪ ɪ ᴀᴍ ᴘᴇʀᴍᴀɴᴇɴᴛ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ + ᴄᴜsᴛᴏᴍ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ɪᴛ ᴍᴇᴀɴs ᴀɴʏ ᴜsᴇʀ ᴄᴀɴ sᴇᴛ ʜɪs ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀɴᴅ + ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ.

🤖 ᴍʏ ɴᴀᴍᴇ: {}

📝 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>𝐏𝐲𝐭𝐡𝐨𝐧𝟑</a>

📚 ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=tg://user?id={}>ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></b>
"""

    CLONE_TXT = """<b>ʜᴇʟʟᴏ {} 👋

First Send /clone command then follow below steps.
    
1) sᴇɴᴅ <code>/newbot</code> ᴛᴏ @BotFather
2) ɢɪᴠᴇ ᴀ ɴᴀᴍᴇ ꜰᴏʀ ʏᴏᴜʀ ʙᴏᴛ.
3) ɢɪᴠᴇ ᴀ ᴜɴɪǫᴜᴇ ᴜsᴇʀɴᴀᴍᴇ.
4) ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ.
5) ꜰᴏʀᴡᴀʀᴅ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ.

ᴛʜᴇɴ ɪ ᴀᴍ ᴛʀʏ ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ᴄᴏᴘʏ ʙᴏᴛ ᴏғ ᴍᴇ ғᴏʀ ʏᴏᴜ ᴏɴʟʏ 😌</b>"""

    HELP_TXT = """<b><u>💢 HOW TO USE THE BOT ☺️</u>

🔻 /link - ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴏʀ ғɪʟᴇ ᴛᴏ ɢᴇᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ

🔻 /batch - sᴇɴᴅ ғɪʀsᴛ ʟɪɴᴋ ᴏғ ғɪʟᴇ sᴛᴏʀᴇ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛ ᴛʜᴇɴ ʟᴀsᴛ ᴘᴏsᴛ ʟɪɴᴋ ᴀɴᴅ ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ғɪʟᴇ sᴛᴏʀᴇ ᴄʜᴀɴɴᴇʟ
ᴇx - /batch https://t.me/x7islandDevs/25 https://t.me/x7islandDevs/30

🔻 /broadcast - ʀᴇᴘʟʏ ᴛᴏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ (ʙᴏᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</b>"""


    CHELP_TXT = """<b>💢 Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ ☺️

🔻 /link - ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴏʀ ғɪʟᴇ ᴛᴏ ɢᴇᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ

🔻 /base_site - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ʟɪɴᴋ ᴅᴏᴍᴀɪɴ
ᴇx - /base_site ʏᴏᴜʀᴅᴏᴍᴀɪɴ.ᴄᴏᴍ

🔻 /api - sᴇᴛ ʏᴏᴜʀ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴀᴘɪ
ᴇx - /api ʙᴀᴏᴡɢᴡᴋʟᴀᴀʙᴀᴋʟ

🔻 /broadcast - ʀᴇᴘʟʏ ᴛᴏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ (ʙᴏᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</b>"""


    LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""
