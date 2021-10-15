# ML-in-business
Machine Learning in Business

# КУРСОВОЙ ПРОЕКТ
## Описание датасета:

Датасет взят из kaggle - https://www.kaggle.com/blackmoon/russian-language-toxic-comments
Даны токсичные комментарии на русском языке - хорошие "нетоксичные" и токсичные.
Датасет содержит всего 2 столбца - комментарий и метка токсичности.
Задача - определить токсичность комментария
Базовый класс - 0 (хороший, "нетоксичный" комментарий)
Целевой класс - 1 (плохой, токсичный комметарий)

* более подробное описание - Course_project_AViatkina.ipynb

Т.к. работаем всего с 1 признаком, необходимо тщательно обрабоать комментарии

* Преобразования признаков: tfidf с собственным параметром tokenize
tokenize = lambda x: [SnowballStemmer(language="russian").stem(i) for i in word_tokenize(x, language="russian") if (i not in string.punctuation and i not in stopwords.words("russian")]

* Модель: logreg

* Из преобразования и модели собираем pipeline.

* Создаем файлы для дальйнешей работы: Dockerfile, docker-entrypoint.sh, requirements.txt
* В папке app создаем главный скрипт для запуска api Flask -  run_server.py

* Создаем образ
docker build -t classification_comments .

* Создаем контейнер. 

docker run -d -p 8183:8183 -v /Users/aleksandrinavatkina/Desktop/GeekBrains/'Машинное обучение в бизнесе'/les9_cp/course_project/app/models:/app/app/models     classification_comments.

По его номеру запускаем:  
Находим номер контейнера. 

docker ps -a     
  
Запускаем. 

docker logs 0780eb3bc348   

* Запускаем функцию get_prediction() - получаем наш прогноз
