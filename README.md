# Веб-застосунок голосового асистента з використанням технологій штучного інтелекту
## Опис
Було розроблено систему голосового асистента, який може розпізнавати мову, синтезувати мову, розпізнавати команди (за допомогою логістичної регресії), а також виокремлювати параметри з команди користувача (за допомогою NLP).
Також на основі створеної системи було розроблено веб-застосунок, серверна частина якого написана за допомогою фреймворку Django для Python.
## Використані технології
gtts - синтез мови<br>
speech_recognition - розпізнавання мови<br>
scikit-learn - для логістичної регресії<br>
spacy - для NLP<br>
Django - backend<br>
## Власна розробка
Було розроблено функції для виокремлення параметрів з команди за допомогою NLP. На просторах інтернету я такого підходу не зустрічав.
