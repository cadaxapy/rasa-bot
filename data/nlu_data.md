<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/rasa-starter-pack/704 --> 

## intent:goodbye <!--- The label of the intent --> 
- пока 			
- Пока 			
- Прощай
- До скорого
- Пока бот
- До свидания друг
- до свидания
- а сейчас до свидания
- увидимся позже
- должен идти
- Увидимся
- доброй ночи
- хорошего дня
- я ухожу
- Увидимся позже
- мы скоро поговорим

## intent:greet
- Привет
- привет
- Привет бот
- Эй, бот
- Здравствуйте
- Доброе утро
- Привет еще раз
- Привет народ
- привет мистер
- привет, приятель!
- всем привет
- Приветствую
- всем привет
- Привет, кто-нибудь там
- привет робот

## intent:thanks
- Спасибо
- Благодарю вас
- Огромное спасибо
- Спасибо, бот
- Спасибо за это
- ура
- ура братан
- хорошо спасибо!
- отлично спасибо
- большое спасибо за все
- Спасибо за помощь
- большое спасибо
- удивительно, спасибо
- хорошо, спасибо
- круто спасибо

## intent:affirm
- да
- Да, конечно
- абсолютно
- наверняка
- да да да
- определенно

## intent:name
- Меня зовут [Juste](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- я [Josh](name)
- зови меня [Lucy](name)
- можешь звать [Greg](name)
- It's [David](name)
- обычно ко мне обращаются [Amy](name)
- можешь звать меня [John](name)
<!--- 
- You can call me [Sam](name)
- Please call me [Linda](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I'm [Tracy](name)
- Call me [Sally](name)
- I am [Philipp](name)
<<<<<<< HEAD
- I am [Charlie](name)
- I am [Elaman](name)


## intent:joke
- Can you tell me a joke?
- I would like to hear a joke
- Tell me a joke
- A joke please
- Tell me a joke please
- I would like to hear a joke
- I would loke to hear a joke, please
- Can you tell jokes?
- Please tell me a joke
- I need to hear a joke

## intent:weather
- What is weather in [Bishkek](city)
- Weather in [Naryn](city)
- Какая погода в [London](city)
- what's the weather in [Berlin](city)
- what's the weather in [Moscow](city)
- what is the weather in [California](city)
- what is the weather in [New Zealand](city)
- whats the weather in [Dubai](city)
- what is the weather like in [Almaty](city)
- how is the weather in [Astana](city)
- how's the weather in [Osh](city)
- hows the weather in [Pekin](city)
=======
- I am [Charlie](name) -->


## intent:joke
- расскажи какую ни будь шутку ?
- Я хотел бы услышать шутку
- Расскажи мне шутку
- Шутка, пожалуйста
- Скажи мне, пожалуйста, шутку
- Я хотел бы услышать шутку
- Я хотел бы услышать шутку, пожалуйста
- Можешь рассказать анекдоты?
- Пожалуйста, скажи мне шутку
- Мне нужно услышать шутку
- шутку пожалуйста
>>>>>>> da22fe1336c7cb8f576e7733ba1df884c1d66865
