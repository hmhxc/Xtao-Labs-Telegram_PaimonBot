from ci import admin_id
from pyrogram import Client
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

HELP_MSG_PRE = '<a href="https://gitlab.com/Xtao-Labs/Telegram_PaimonBot">PaimonBot</a> ' \
               '0.4.0beta By Xtao-Labs\n\n' \
               'ð ä»¥ä¸æ¯å°æ´¾èæå­¦ä¼äºçåè½ï¼é¨åï¼ï¼\n'
HELP_MSG = """â  [æ­¦å¨/ä»æ¥æ­¦å¨] æ¥çä»æ¥æ­¦å¨ææåæ­¦å¨
â¡ [å¤©èµ/ä»æ¥å¤©èµ] æ¥çä»æ¥å¤©èµææåè§è²
â¢ [å¨æ¬] æ¥çå¨æ¬ææåäººç©
â£ [è¿å¿ (åå­)] æ¥çä»æ¥è¿å¿
   ð  <code>è¿å¿ (éäº)</code>
   ð  <code>è®¾ç½®è¿å¿ (éäº)</code>
â¤ [è§è²æ¥è¯¢ åå­] æ¥çäººç©ç®ä»
   ð  <code>è§è²æ¥è¯¢ éäº</code>
â¥ [å½åº§ åå­] æ¥çäººç©å½åº§
   ð  <code>å½åº§ éäºä¸å½</code>
â¦ [æ­¦å¨æ¥è¯¢ æ­¦å¨å] æ¥çæ­¦å¨èµæ
   ð  <code>æ­¦å¨æ¥è¯¢ æ²æµ´é¾è¡çå</code>
â§ [åé­æ¥è¯¢ åé­å] æ¥çåé­èµæ
   ð  <code>åé­æ¥è¯¢ ä¸ä¸äºº</code>
â¨ [é£ç©æ¥è¯¢ é£ç©/é£æå] æ¥çé£ç©èµæ
   ð  <code>é£ç©æ¥è¯¢ ççè±/ççè±é¿é¸¡</code>
â© [å£éç©æ¥è¯¢ å£éç©å¥è£å] æ¥çå£éç©å¥è£èµæ
   ð  <code>å£éç©æ¥è¯¢ éé£çæµæ</code>
======
(11) [æ½å¡] æ½å¡
   ð  <code>æ½å¡</code>
   ð  <code>æ½å¡ 2</code>
   ð  <code>æ½å¡ æ­¦å¨</code>
   ð  <code>æ½å¡ å¸¸é©»</code>
(12) [åç¥é»å] æ¥çéæºçæçåç¥é»å
(13) [æ´»å¨åè¡¨] æ¥çä»æ¥æ´»å¨åè¡¨åç¥æ¿åè¡¨
(14) [å£éç©è¯å] æä¹æ³æ¥æè¿ç§åæ°çå£éç©(åå®)
(15) [åªéæ (èµæºå)] æ¥çèµæºçä½ç½®
(16) [èµæºåè¡¨] æ¥çåç¥ææèµæºï¼ç§èï¼
(17) [çè¯­é³] åç¾¤åä¸èµ·ç©çè¯­é³å°æ¸¸æå§ï¼ï¼ç¾¤èï¼
   ð  <code>çè¯­é³</code>
   ð  <code>çè¯­é³ æ å°½æ¨¡å¼</code>
(18) [æä¹å» (è§è²å)] è¾åºè§è²éç¨æ­¦å¨&å£éç©
(19) [ç»è°ç¨ (æ­¦å¨å)] è¾åºæ­¦å¨éç¨è§è²
(20) [ç±³æ¸¸ç¤¾/hoyolab] ç±³æ¸¸ç¤¾/hoyolabç¸å³åè½
   ð  <a href="https://telegra.ph/PaimonBot-02-18">ç¹å»æ¥ç</a>"""


async def welcome_command(client: Client, message: Message):
    # åéæ¬¢è¿æ¶æ¯
    await message.reply('ä½ å¥½ï¼ææ¯åç¥å°å©æ - æ´¾è ã', quote=True)


async def ping_command(client: Client, message: Message):
    # æéå¨çº¿ç¶æ
    await message.reply("poi~", quote=True)


async def leave_command(client: Client, message: Message):
    # éåºç¾¤ç»
    chat_id = message.text.split()[-1]
    # æéæ£æ¥
    if message.from_user.id == admin_id:
        return
    try:
        await client.leave_chat(chat_id)
        await message.reply('æåæ§è¡éåºç¾¤ç»å½ä»¤ã')
    except Exception as e:
        await message.reply(f'éè¯¯ï¼\n{e}')


async def help_command(client: Client, message: Message):
    text = HELP_MSG_PRE + HELP_MSG.split("\n======\n")[0]
    await message.reply(text, quote=True, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ä¸ä¸é¡µ", callback_data="help_1")],
        ]))


async def help_callback(client: Client, query: CallbackQuery):
    data = query.data.replace("help_", "")
    try:
        data = int(data)
    except ValueError:
        data = 1
    text = HELP_MSG_PRE + HELP_MSG.split("\n======\n")[data]
    await query.message.edit(text, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ä¸ä¸é¡µ" if data else "ä¸ä¸é¡µ",
                                  callback_data="help_0" if data else "help_1")],
        ]))
