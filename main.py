from lib2to3.fixes.fix_input import context
from typing import Final
import re
import os
from telegram import Update, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Bot,InputMediaVideo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext, CallbackQueryHandler
from pytube import YouTube
import openai
from requests import get
import json
from time import sleep
from keep_alive import keep_alive
from youtube_transcript_api import YouTubeTranscriptApi

# import AI
keep_alive()
BOT = os.environ['BOT_TOKEN']
TOKEN: Final = BOT
bot = Bot(TOKEN)
BOT_USERNAME: Final = "@Yt3_downloader_helper" //enter your telegram  bot username 
path = os.getcwd()

#AI
openai.api_key = os.environ['OPENAI_API_KEY']
def response(a:str):
  response = openai.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      response_format={"type": "json_object"},
      messages=[
          {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
          {"role": "user", "content": f"{a}Make a summary"}
      ]
  )
  str12 = response.choices[0].message.content
  return str12
# bold

# YouTube



# def reshigh(a:str,b:str):
#      y = YouTube.thumbnail_url(a)
#      s = y.streams.get_highest_resolution()
#      vd = s.download()

async def start_commmand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Simply share the link and choose the Function✨.")


async def pay_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pay in this below UPI id")
    await update.message.reply_photo("spinach.jpg")

    # AI.getter(gen, g, name, n, h, w)


t1: str = "URL"
t2: str = "Title"
t3: str = "Channel Name"
t4: str = "Views"
t5: str = "Length"
class F:
  var:int=0

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global message1
    message_type: str = update.message.chat.type
    message1 = update.message.text
    with open("link.txt",'w') as f:
        f.write(message1)
    print(update.message.chat.username, update.message.chat_id)
    r = get(message1)
    
    if not ("Video unavailable" in r.text):
        vd = YouTube(message1)
        image = get(vd.thumbnail_url).content
        tt = vd.title
        ch_name = vd.author
        views = vd.views
        leng = vd.length
        await update.message.reply_photo(image)
        await update.message.reply_text(f"{t1}:{message1}\n{t2}:{tt}\n{t3}:{ch_name}\n{t4}:{views}\n{t5}:{leng}secs")
        button =[[InlineKeyboardButton("Click here to verify",url="https://instantlinks.in/nrgCm",callback_data="click")]]
        reply1 = InlineKeyboardMarkup(button)
        await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(button),
                                           text="     Formats⬇️     ")
        sleep(8)
        buttons = [[InlineKeyboardButton("1080p" ,callback_data="1080p")],
                   [InlineKeyboardButton("720p" ,callback_data="720p")],
                   [InlineKeyboardButton('360p', callback_data="360p")],
                   [InlineKeyboardButton("144p", callback_data="144p")],
                   [InlineKeyboardButton("Audio", callback_data="mp4")],
                   [InlineKeyboardButton("Summary", callback_data="summary")]]
        reply = InlineKeyboardMarkup(buttons)
        await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                                       text="     Formats⬇️     ")
  

    else:
        await update.message.reply_text("Invalid Link")

# query
def func(a:str)->str:
    text =""
    for i in range(0, len(a)):
        dic = dict(a[i])
        text += dic.get('text')
    return text
def getPath(path:str):
  path = './/' + path
  return path
lis =[]
def lisfunc(a:str):

  lis.append(a)
  return lis
async def query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query.data
    await update.callback_query.answer()
    print(query)
    lis = lisfunc(query)
    print(lis)
    # await context.bot.send_message(chat_id=update.effective_chat.id,text="Click this link below to verify your download")
    # await context.bot.send_message(chat_id=update.effective_chat.id,text="")
  
    with open("link.txt",'r') as f:
        urllis = f.readlines()
    lik = urllis[-1]
    url = YouTube(lik)
    print(url)
    if "click" in lis[0]:
        if "1080p" in lis[-1]:
            file_name = "1" + ".mp4"
            file_name = getPath(file_name)
            print(file_name)
            url.streams.get_highest_resolution() .download(filename="1.mp4",skip_existing=True,max_retries=4)
            await context.bot.send_message(chat_id=update.effective_chat.id,text="downloading!")
            await context.bot.send_video(chat_id=upddate.effective_chat.id,video=file_name)
        if "720p" in lis[-1]:
            file_name = "1" + ".mp4"
            file_name = getPath(file_name)
            print(file_name)
            url.streams.get_by_resolution("720p").download(filename="1.mp4",skip_existing=True,max_retries=4)
            await context.bot.send_message(chat_id=update.effective_chat.id, text="downloading!")
            await context.bot.send_video(chat_id=update.effective_chat.id,video=file_name)
            os.remove(file_name)
        if "360p" in lis[-1]:
            file_name = "1" + ".mp4"
            file_name = getPath(file_name)
            print(file_name)
            url.streams.get_by_resolution("360p").download(filename="1.mp4",skip_existing=True,max_retries=4)
            await context.bot.send_message(chat_id=update.effective_chat.id,text="downloading!")
            await context.bot.send_video(chat_id=update.effective_chat.id,video=file_name)
            os.remove(file_name)
        if "144p" in lis[-1]:
            file_name = "1" + ".mp4"
            file_name = getPath(file_name)
            url.streams.get_by_resolution("144p").download(filename="1.mp4",skip_existing=True,max_retries=4)
            await context.bot.send_message(chat_id=update.effective_chat.id, text="downloading!")
            await context.bot.send_video(chat_id=update.effective_chat.id, video=file_name)
            os.remove(file_name)
        if "mp4" in lis[-1]:
            file_name = "1" + ".mp3"
            file_name = getPath(file_name)
            url.streams.get_audio_only().download(filename="1.mp3",skip_existing=True,max_retries=4)
            await context.bot.send_message(chat_id=update.effective_chat.id, text="downloading!")
            await context.bot.send_audio(chat_id=update.effective_chat.id, audio=file_name)
            os.remove(file_name)
        if "summary" in lis[-1]:
            text:str
            try:
               s = YouTubeTranscriptApi.get_transcript(url.video_id)

            except:
               s = 0
               await context.bot.send_message(chat_id=update.effective_chat.id,text="video has no transcription")
               text = ""
            text1 =func(s)
            str = response(text1)
            dic = json.loads(str)
            text1=dic["summary"]
            await context.bot.send_message(chat_id=update.effective_chat.id,text=text1)
    # if "p4" in query:
    #         file_name = url.title+".mp3"
    #         file_path:str = os.path.join(path,file_name)
    #         await context.bot.send_audio(chat_id=update.effective_chat.id,audio=file_path)
    # if "p" in query:
    #
    #     await context.bot.send_video(chat_id=update.effective_chat.id, video=file_path)

        # await context.bot.send_message(chat_id=update.effective_chat.id,text=

# async def dietp
lis.clear()
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"update{update}caused error{context.error}")


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_commmand))
    app.add_handler(CommandHandler('pay', pay_command))
    app.add_error_handler(error)
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    #app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_mes))
    app.add_handler(CallbackQueryHandler(query_handler))

    app.run_polling(poll_interval=3)
