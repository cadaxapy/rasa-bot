## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye  

## story_thanks
* thanks
 - utter_thanks

## story_name
* name{"name":"Sam"}
 - utter_greet
## story_joke_01
* joke
 - action_joke
## story_weather
* weather{"city":"Bishkek"}
 - action_weather
## story_translate
* translate("word":"cat", "lang":"russian")
 - action_translate
## story_joke_02
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* joke
 - action_joke
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 
 
 ## story_born_01
* origin
 - utter_origin
* enter_data{"location": "Ош"}
- utter_great
## story_dialog
* greet
- utter_name

* name
- utter_greet

* how_are_you
- utter_good 

* user_joking
- utter_laugh

* thanks
- utter_welcome

* age
- utter_age

* compliment
- utter_thanks

* insult
- utter_bye

* workoreduc
- utter_work

* hobby
- utter_hobby

* good
- utter_good

* bad
- utter_why

* myage
- utter_confirmed
