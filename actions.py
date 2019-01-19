# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
from weather import Weather, Unit
from googletrans import Translator

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []


class ActionWeather(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('city')
        weather = json.loads(requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=16be1a7a58efb5cb152a9053a7c36422').text)
        print(weather['main'])
        dispatcher.utter_message("Weather in "+ city +" is " + str(weather['main']['temp']) + "C")  # send the message back to the user
        return []


class ActionTranslate(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_translate"

    def run(self, dispatcher, tracker, domain):
        word = tracker.get_slot('word')
        lang = tracker.get_slot('lang')
        print(word)
        print(lang)
        translator = Translator()
        translation = translator.translate(word, dest=lang)
        print(translation)
        dispatcher.utter_message(translation.text)  # send the message back to the user
        return []
