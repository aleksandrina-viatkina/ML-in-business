# ML-in-business
Machine Learning in Business
____
# Course project.    
____
Датасет взят с kaggle - https://www.kaggle.com/blackmoon/russian-language-toxic-comments 

Дано:  комментарии на русском языке - хорошие "нетоксичные" и токсичные.    
Датасет содержит всего 2 признака  - текст комментария (comment) и метка класса (toxic).    
Задача: Определить является комментарий токсичным или нет. Бинарная классификация.  

Преобразования признаков: tfidf с построенным параметром tokenizer: токенизация текста, удаление знаков препинания, стоп слов и последующая стемматизация (удаление суффиксов и окончаний, преобразований словоформ)
  
Модель: Logistic Regression 

Сохраненная модель - logreg_pipeline_.dill

**Работа с Docker**. 

Созданы файлы Dockerfile, docker-entrypoint.sh, скрипт run_server.py для получения классификации с помощью модели через api

*Создаем образ*      
docker build -t classification_comments .

*Собираем контейнер*    
docker run -d -p 8183:8183 -v /Users/aleksandrinavatkina/Desktop/GeekBrains/'Машинное обучение в бизнесе'/les9_cp/course_project/app/models:/app/app/models classification_comments

Запуская контейнер, вызываем фукнцию get_prediction и получаем классификацию поданных в функицю комментариев.


**Более подробно - Course_project_AViatkina.ipynb**
