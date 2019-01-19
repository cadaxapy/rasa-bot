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

## intent:weather
- What is weather in [Bishkek](city)
- Weather in [Naryn](city)
- weather in [Bangkok](city)
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

## intent:joke
- расскажи каtensorflow_embeddingкую ни будь шутку ?
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

## intent:translate
- Please, translate [cat](word) to [russian](lang)
- translate [dog](word) to [english](lang)
- can you translate [apple](word) to [german](lang)
- translate pls [bottle](word) to [chinese](lang)
- translate me [table](word) to [kyrgyz](lang)
- translate me please [window](word) to [french](lang)
- translate word [tea](word) to [polish](lang)
- translate me plz [spoon](word) to [romanian](lang)
- translate me [mouse](word) to [korean](lang)
- translate me [banana](word) to [turkish](lang)
- what is [laptop](word) in [japanese](lang)

## intent:wiki
- what u know about [bishkek](wiki_word)
- do u know what is [python](wiki_word)
- give me information about [acer](wiki_word)
- show me info about [xiaomi](wiki_word)
- what is [apple](wiki_word)
- what you know about [microsoft](wiki_word)
- give me some information about [starbucks](wiki_word)
- tell me what is [cola](wiki_word)
- give me information about [dell](wiki_word)
- show me information about [asus](wiki_word)
- show me information about [auca](wiki_word)
- information about [namba](wiki_word)
