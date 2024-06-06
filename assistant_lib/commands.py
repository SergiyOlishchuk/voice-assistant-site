from random import choice
import json
import requests
import anthropic
from .params_parser import extract_params, normilaze_city
from .speak import say

with open('assistant_config.json', 'r', encoding='UTF-8') as file:
    CONFIG = json.load(file)


def find_in_google(command, save_audio_path):
    keywords = CONFIG["find_in_google"]["keywords"]
    ban_words = CONFIG["find_in_google"]["ban_words"]
    params = extract_params(command, keywords, ban_words)

    pattern_phrases = CONFIG["find_in_google"]["pattern_phrases"]

    answer_to_say = choice(pattern_phrases)

    link = "https://www.google.com/search?q=" + "+".join(params.split())

    say(answer_to_say, save_audio_path)

    return answer_to_say + f'<br><a href="{link}">'


def find_video(command, save_audio_path):
    keywords = CONFIG["find_video"]["keywords"]
    ban_words = CONFIG["find_video"]["ban_words"]
    params = extract_params(command, keywords, ban_words)

    pattern_phrases = CONFIG["find_video"]["pattern_phrases"]

    answer_to_say = choice(pattern_phrases)

    link = "https://www.youtube.com/results?search_query=" + "+".join(params.split())

    say(answer_to_say, save_audio_path)

    return answer_to_say + f'<br><a href="{link}">'


def weather(command, save_audio_path):
    try:
        keywords = CONFIG["weather"]["keywords"]
        ban_words = CONFIG["weather"]["ban_words"]
        params = extract_params(command, keywords, ban_words)

        city = normilaze_city(params)
        base_url = CONFIG["weather"]["base_url"]
        api_key = CONFIG["weather"]["api_key"]

        params = {"q": city, "appid": api_key, "units": "metric", "lang": "uk"}

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]

            answer_to_say = f"Погода в {city}. Опис: {weather_description}. Температура: {temperature} градусів Цельсія. Відчувається як: {feels_like} градусів Цельсія. Вологість: {humidity} відсотків."
            answer_to_print = f"Погода в {city}.<br> Опис: {weather_description}.<br> Температура: {temperature} °C.<br> Відчувається як: {feels_like} °C.<br> Вологість: {humidity}%."

        else:
            answer_to_say = answer_to_print = (
                "Нажаль, я зараз не можу відповісти на цей запит"
            )

        say(answer_to_say, save_audio_path)
        return answer_to_print
    except Exception:
        say(CONFIG["weather"]["error_message"], save_audio_path)
        return CONFIG["weather"]["error_message"]


def lang_model_answer(command, save_audio_path, api_key):
    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=0,
            system="Ти помічник для користувача",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": command,
                        }
                    ],
                }
            ],
        )
    except anthropic.AuthenticationError:
        say(CONFIG["lang_model_answer"]["error_auth_message"], save_audio_path)
        return CONFIG["lang_model_answer"]["error_auth_message"]

    answer = message.content[0].text

    answer_to_say = answer.replace("\n", " ")
    answer_to_print = answer.replace("\n", "<br>")

    say(answer_to_say, save_audio_path)
    return answer_to_print
