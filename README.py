
dvmbhu = [
    "https://files.catbox.moe/pcmd3f.mp4",
    "https://files.catbox.moe/1858da.mp4",
    "https://files.catbox.moe/xhdt01.mp4",
    "https://files.catbox.moe/pu6ql4.mp4",
    "https://files.catbox.moe/dbbwh8.mp4"
]
vid = random.choice(dvmbhu)
vipurl = "https://raw.githubusercontent.com/d-vmb/B/main/users.txt"

def findtime():
    try:
        return datetime.now()
    except Exception:
        print(" ㅤㅤ\033[1;31m[ ⚚ ]    𝐔𝚗𝚎𝚡𝚙𝚎𝚌𝚝𝚎𝚍 𝐄𝚛𝚛𝚘𝚛. ¹⚠️")
        sys.exit(1)

def sendmessage(bottoken, chatid, text, markup=None):
    try:
        url = f"https://api.telegram.org/bot{bottoken}/sendMessage"
        payload = {
            "chat_id": chatid,
            "text": text,
            "parse_mode": "HTML"
        }
        if markup:
            payload["reply_markup"] = markup
        requests.post(url, json=payload, timeout=30)
    except Exception:
        pass

def makebuttons():
    return json.dumps({
        "inline_keyboard": [
            [{"text": "𝐂𝚘𝚗𝚝𝚊𝚌𝚝 𝐃𝚎𝚟 👨‍💻", "url": "https://t.me/dvvmb"}],
            [{"text": "𝐉𝚘𝚒𝚗 𝐂𝚘𝚖𝚖𝚞𝚗𝚒𝚝𝚢 👑", "url": "https://t.me/addlist/-zdOU4i16nNjZjll"}]
        ]
    })


def left(diff):
    months = diff.days // 30
    days = diff.days % 30
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    if months > 0:
        return f"{months} 𝐌𝚘𝚗𝚝𝚑{'' if months == 1 else '𝚜'} {days} 𝐃𝚊𝚢{'' if days == 1 else '𝚜'}"
    elif days > 0:
        return f"{days} 𝐃𝚊𝚢{'' if days == 1 else '𝚜'} {hours} 𝐇𝚘𝚞𝚛{'' if hours == 1 else '𝚜'}"
    else:
        return f"{hours} 𝐇𝚘𝚞𝚛{'' if hours == 1 else '𝚜'} {minutes} 𝐌𝚒𝚗𝚞𝚝𝚎{'' if minutes == 1 else '𝚜'}"
        

def sendvideo(bottoken, chatid, videourl, caption=None, markup=None):
    try:
        url = f"https://api.telegram.org/bot{bottoken}/sendVideo"
        payload = {
            "chat_id": chatid,
            "video": videourl
        }
        if caption:
            payload["caption"] = caption
            payload["parse_mode"] = "HTML"
        if markup:
            payload["reply_markup"] = markup
        requests.post(url, json=payload, timeout=20)
    except Exception:
        pass

def getuserdetail(bottoken, userid):
    try:
        url = f"https://api.telegram.org/bot{bottoken}/getChat"
        params = {"chat_id": userid}
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("ok"):
                user = data.get("result", {})
                fname = user.get("first_name", "")
                lname = user.get("last_name", "")
                uname = user.get("username", "")
                return {
                    "id": userid,
                    "name": f"{fname} {lname}".strip() or "𝐔𝚗𝚔𝚗𝚘𝚠𝚗",
                    "uname": f"@{uname}" if uname else "𝐔𝚗𝚔𝚗𝚘𝚠𝚗"
                }
        return {"id": userid, "name": "𝐔𝚗𝚔𝚗𝚘𝚠𝚗", "uname": "𝐔𝚗𝚔𝚗𝚘𝚠𝚗"}
    except Exception:
        return {"id": userid, "name": "𝐔𝚗𝚔𝚗𝚘𝚠𝚗", "uname": "𝐔𝚗𝚔𝚗𝚘𝚠𝚗"}

def getbotdetail(bottoken):
    try:
        url = f"https://api.telegram.org/bot{bottoken}/getMe"
        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("ok"):
                bot = data.get("result", {})
                return {
                    "name": bot.get("first_name", "𝐔𝚗𝚔𝚗𝚘𝚠𝚗"),
                    "uname": f"@{bot.get('username', 'unknown')}",
                    "token": bottoken
                }
        return {"name": "𝐔𝚗𝚔𝚗𝚘𝚠𝚗 𝐁𝚘𝚝", "uname": "@unknown", "token": bottoken}
    except Exception:
        return {"name": "𝐔𝚗𝚔𝚗𝚘𝚠𝚗", "uname": "@error", "token": bottoken}

def info_msg(user, bot, status, timeleft=""):
    usermention = f'<a href="tg://user?id={user["id"]}">{user["name"]}</a>'
    botmention = f'<a href="https://t.me/{bot["uname"][1:] if bot["uname"].startswith("@") else bot["uname"]}">{bot["name"]}</a>'
    username = user["uname"][1:] if user["uname"].startswith("@") else user["uname"]
    botuname = bot["uname"][1:] if bot["uname"].startswith("@") else bot["uname"]
    return f"""
<b>𝐇𝚎𝚢𝚢 {usermention}  👋, 𝐘𝚘𝚞 𝐀𝚛𝚎 𝐔𝚜𝚒𝚗𝚐 <a href="https://t.me/dvvmb">𝐃𝐕𝐌𝐁</a>'𝚜 𝐓𝚘𝚘𝚕</b>

<blockquote> <b>👤 𝒀𝒐𝒖𝒓 𝑰𝒏𝒇𝒐 —</b>
  <b>├ 𝐍𝚊𝚖𝚎 ➛</b> <b>{usermention}</b>
  <b>├ 𝐔𝚜𝚎𝚛𝚗𝚊𝚖𝚎 ➛ @{username}</b>
  <b>└ 𝐓𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝐈𝙳 ➛</b> <code>{user["id"]}</code></blockquote>
<blockquote> <b>🤖 𝑩𝒐𝒕 𝑰𝒏𝒇𝒐 —</b>
  <b>├ 𝐁𝚘𝚝 𝐍𝚊𝚖𝚎 ➛</b> {botmention}
  <b>├ 𝐁𝚘𝚝 𝐔𝚜𝚎𝚛𝚗𝚊𝚖𝚎 ➛ @{botuname}</b>
  <b>└ 𝐀𝚙𝚒 𝐓𝚘𝚔𝚎𝚗 ➛</b> <code>{bot["token"]}</code></blockquote>
<blockquote> <b>💸 𝑻𝒐𝒐𝒍 𝑺𝒕𝒂𝒕𝒖𝒔 —</b>
  <b>├ 𝐍𝚊𝚖𝚎 ➛ 𝐫𝖆𝖓𝖌𝖊𝐬¹¹¹.py</b>
  <b>├ 𝐒𝚞𝚋𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗 ➛ {status}</b>
  <b>└ 𝐓𝚒𝚖𝚎 𝐋𝚎𝚏𝚝 ➛ {timeleft if timeleft else "𝐍𝚘𝚗𝚎"}</b></blockquote>
"""

def checkvip(teleid, bottoken):
    try:
        now = findtime()
        user = getuserdetail(bottoken, teleid)
        bot = getbotdetail(bottoken)

        status = ""
        timeleft = ""
        found = False
        response = requests.get(vipurl, timeout=15)
        if response.status_code != 200:
            print(" ㅤㅤ\033[1;31m[ ⚚ ]    𝐔𝚗𝚎𝚡𝚙𝚎𝚌𝚝𝚎𝚍 𝐄𝚛𝚛𝚘𝚛. ² ⚠️")
            sys.exit(1)

        lines = response.text.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue

            if line == "DVMB":
                if i + 2 < len(lines):
                    expdate = lines[i+1].strip().replace("\t", "")
                    exptime = lines[i+2].strip().replace("\t", "")
                    exstr = f"{expdate} {exptime}"
                    expdt = datetime.strptime(exstr, "%d/%m/%y %H:%M")
                if now <= expdt:
                    diff = expdt - now
                    timeleft = left(diff)
                    status = "𝐅𝚛𝚎𝚎 𝐕𝚎𝚛𝚜𝚒𝚘𝚗 ⭐"
                    print(" ㅤㅤ\033[1;32m[ ⚚ ]    𝐃𝕧ᴍ𝙱 𝐇𝚊𝚜 𝐆𝚒𝚟𝚎𝚗 𝐀𝚌𝚌𝚎𝚜𝚜 𝐓𝚘 𝐀𝚕𝚕 ✅")
                    found = True
                    break

                i += 3
                continue

            parts = line.split("\t")
            uid = parts[0].strip()
            if uid == str(teleid):
                if i + 2 < len(lines):
                    expdate = lines[i+1].strip().replace("\t", "")
                    exptime = lines[i+2].strip().replace("\t", "")
                    exstr = f"{expdate} {exptime}"
                    expdt = datetime.strptime(exstr, "%d/%m/%y %H:%M")
                    if now <= expdt:
                        diff = expdt - now
                        status = "𝐏𝚊𝚒𝚍 𝐒𝚞𝚋𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗 ✅"
                        timeleft = left(diff)
                        print(" ㅤㅤ\033[1;32m[ ⚚ ]    𝐀𝚌𝚌𝚎𝚜𝚜 𝐆𝚛𝚊𝚗𝚝𝚎𝚍, 𝐏𝚛𝚘𝚌𝚎𝚎𝚍𝚒𝚗𝚐 . . . ✅")
                        found = True
                        break
                    else:
                        status = "𝐄𝚡𝚙𝚒𝚛𝚎𝚍 🚫"
                        print(" ㅤㅤ\033[1;31m[ ⚚ ]    ❌ 𝐒𝚞𝚋𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗 𝐄𝚡𝚙𝚒𝚛𝚎𝚍")
                        found = True
                        break
                found = True
                break
            i += 1

        if not found:
            status = "𝐏𝚞𝚛𝚌𝚑𝚊𝚜𝚎 𝐀𝚌𝚌𝚎𝚜𝚜 😾"
            print(" ㅤㅤ\033[1;33m[ ⚚ ]    𝐘𝚘𝚞 𝐇𝚊𝚟𝚎 𝐓𝚘 𝐏𝚞𝚛𝚌𝚑𝚊𝚜𝚎 𝐓𝚑𝚎 𝐓𝚘𝚘𝚕")
            print(" ㅤㅤ\033[1;33m[ ⚚ ]    𝐎𝚛 𝐖𝚊𝚒𝚝 𝐈𝚗 𝐓𝚑𝚎 𝐂𝚑𝚊𝚗𝚗𝚎𝚕 𝐅𝚘𝚛 𝐅𝚛𝚎𝚎 𝐀𝚌𝚌𝚎𝚜𝚜 ")

        msg = info_msg(user, bot, status, timeleft)
        sendvideo(bottoken, teleid, vid, msg, makebuttons())
        if status in ["𝐄𝚡𝚙𝚒𝚛𝚎𝚍 🚫", "𝐏𝚞𝚛𝚌𝚑𝚊𝚜𝚎 𝐀𝚌𝚌𝚎𝚜𝚜 😾"]:
            sys.exit()
    except Exception as e:
        print(f" ㅤㅤ\033[1;31m[ ⚚ ]    𝐔𝚗𝚎𝚡𝚙𝚎𝚌𝚝𝚎𝚍 𝐄𝚛𝚛𝚘𝚛. ³⚠️")
        sys.exit(1)
