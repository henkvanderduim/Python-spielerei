# impoorteren libraries
import os
import json
from steamship import Steamship, TaskState
import telebot
from serpapi import GoogleSearch
import requests
import urllib
import subprocess
import time

f = open("cred.json", "rb")
params = json.load(f)
BOT_TOKEN = params["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, "Insert the audio of your song!")


bot.infinity_polling()


@bot.message_handler(content_types=["voice"])
def telegram_bot(message, bot_token=params["BOT_TOKEN"]):
    # insert audio
    file_info = bot.get_file(message.voice.file_id)
    # extract telegram's url of the audio
    audio_url = "https://api.telegram.org/file/bot{}/{}".format(
        bot_token, file_info.file_path
    )


bot.infinity_polling()


def convert_oga_to_mp3(audio_url):
    file = requests.get(audio_url)
    urllib.request.urlretrieve(audio_url, "audio.oga")
    subprocess.run(["ffmpeg", "-i", "audio.oga", "audio.mp3"])
    data = open("audio.mp3", "rb")


def get_url_mp3(bot_token, message):
    bot.reply_to(message, "Searching song...")
    data = open("audio.mp3", "rb")
    ret_msg = bot.send_voice(message.chat.id, data)
    file_info = bot.get_file(ret_msg.voice.file_id)
    audio_url = "https://api.telegram.org/file/bot{}/{}".format(
        bot_token, file_info.file_path
    )
    return audio_url


@bot.message_handler(content_types=["voice"])
def telegram_bot(message, bot_token=params["BOT_TOKEN"]):
    # insert audio
    file_info = bot.get_file(message.voice.file_id)
    # extract telegram's url of the audio
    audio_url = "https://api.telegram.org/file/bot{}/{}".format(
        bot_token, file_info.file_path
    )
    convert_oga_to_mp3(audio_url)
    audio_url = get_url_mp3(bot_token, message)


bot.infinity_polling()

# transcribe audio with Steamship's API
def transcribe_audio(audio_url: str, ship: Steamship):
    instance = ship.use("audio-markdown", "audio-markdown-crows-v27")
    transcribe_task = instance.invoke("transcribe_url", url=audio_url)
    task_id = transcribe_task["task_id"]
    status = transcribe_task["status"]

    retries = 0
    while retries <= 100 and status != TaskState.succeeded:
        response = instance.invoke("get_markdown", task_id=task_id)
        status = response["status"]
        if status == TaskState.failed:
            print(f"[FAILED] {response}['status_message']")
            break

        print(f"[Try {retries}] Transcription {status}.")
        if status == TaskState.succeeded:
            break
        time.sleep(2)
        retries += 1

    markdown = response["markdown"]
    return markdown


@bot.message_handler(content_types=["voice"])
def telegram_bot(message, bot_token=os.getenv("BOT_TOKEN")):
    client = Steamship(api_key=os.getenv("STEAM_API_KEY"))
    ...
    markdown = transcribe_audio(audio_url, client)
    bot.reply_to(message, markdown)


bot.infinity_polling()

## search the trascription on Google using SerpAPI
def search_words(words):
    params_serp = {
        "q": words,
        "hl": "en",
        "gl": "us",
        "google_domain": "google.com",
        "api_key": params["API_KEY"],
    }
    search = GoogleSearch(params_serp)
    results = search.get_dict()
    if "organic_results" in results.keys():
        if "title" in results["organic_results"][0].keys():
            return results["organic_results"][0]["title"]
        else:
            return ""
    else:
        return ""


@bot.message_handler(content_types=["voice"])
def telegram_bot(message, bot_token=params["BOT_TOKEN"]):
    ...
    client = Steamship(api_key=params["STEAM_API_KEY"])
    markdown = transcribe_audio(audio_url, client)
    bot.reply_to(message, markdown)
    result = search_words(markdown)
    ...
    if result == "":
        bot.reply_to(message, "Song not found!")
    else:
        bot.reply_to(message, result)


bot.infinity_polling()
