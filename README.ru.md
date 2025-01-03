<p align="center">
  <a href="README.ru.md"><img src="https://img.shields.io/badge/Русский-Readme-blue" alt="Russian" /></a>&nbsp;&nbsp;
  <a href="README.md"><img src="https://img.shields.io/badge/English-Readme-blue" alt="English" /></a>&nbsp;&nbsp;
  <img src="https://visitor-badge.laobi.icu/badge?page_id=White-Tiger-PX.set-random-wallpaper-from-wallhaven" alt="visitors" />&nbsp;&nbsp;
  <img src="https://img.shields.io/github/stars/White-Tiger-PX/set-random-wallpaper-from-wallhaven?style=social" alt="GitHub stars" />
</p>

# set-random-wallpaper-from-wallhaven

Этот скрипт позволяет установить случайное изображение с Wallhaven в качестве обоев рабочего стола.

## Возможности

- Скачивает случайное изображение с Wallhaven, основываясь на выбранных категориях и параметрах сортировки.
- Автоматически устанавливает загруженное изображение в качестве обоев рабочего стола.
- Позволяет настроить категории изображений, сортировку и поиск по ключевым словам.

## Поддерживаемые операционные системы

Этот скрипт предназначен специально для Windows. Он использует библиотеку `ctypes` для взаимодействия с API Windows и установки обоев рабочего стола.

## Настройка

### Настройка папок для изображений

1. Откройте файл `config.py`.
2. Установите следующие значения:
   - `API_KEY`: Ваш API-ключ Wallhaven. Вы можете получить его, зарегистрировавшись на сайте Wallhaven.
   - `FOLDER_TO_IMAGES`: Путь к папке, куда будут сохраняться изображения.
   - `CATEGORIES`: Строка, представляющая категории изображений, которые вы хотите загрузить. Например:
     - `100`: Только общие изображения.
     - `010`: Только аниме-изображения.
     - `001`: Только изображения людей.
     - `110`: Общие и аниме-изображения.
   - `SORTING`: Параметры сортировки, такие как `'random'`, `'date_added'`, `'relevance'`, `'views'`, `'favorites'`.
   - `Q`: Необязательное ключевое слово для поиска.

### Автоматизация выполнения скрипта

Чтобы запускать скрипт автоматически при старте системы, настройте задачу в **Планировщике заданий Windows**:

1. Откройте **Планировщик заданий**, найдя его в меню Пуск (или нажмите `Win + R`, введите `taskschd.msc` и нажмите Enter).
2. Нажмите **Создать задачу** в правой панели.
3. Укажите имя задачи (например, "Установить случайные обои").
4. Перейдите на вкладку **Триггеры** и нажмите **Создать**.
   - Установите параметр **Начать задачу** на **При входе в систему**, чтобы задача запускалась при каждом входе в систему.
   - По желанию, установите флажок **Повторять задачу через** и укажите интервал (например, каждый 1 час), если вы хотите, чтобы задача выполнялась периодически.
5. Перейдите на вкладку **Действия**, нажмите **Создать**, и выберите **Запуск программы**.
6. Выберите исполнимый файл Python. По умолчанию он находится по пути:
   `C:\Users\ВАШЕ_ИМЯ_ПОЛЬЗОВАТЕЛЯ\AppData\Local\Programs\Python\ВАША_ВЕРСИЯ\python.exe`.
7. В поле **Добавить аргументы** укажите полный путь к вашему скрипту. Например:
   `(C:\путь\к\вашему\set_random_wallpaper_from_wallhaven.py)`
   *(Убедитесь, что путь заключен в кавычки, если он содержит пробелы.)*
8. Нажмите **ОК**, чтобы сохранить задачу.

<div style="justify-content: space-between; align-items: center;">
  <div style="text-align: center;">
    <img src="Task Scheduler - General.png" alt="Task Scheduler - General" width="75%" />
  </div>

  <div style="text-align: center;">
    <img src="Task Scheduler - Triggers.png" alt="Task Scheduler - Triggers" width="75%" />
  </div>

  <div style="text-align: center;">
    <img src="Task Scheduler - General.png" alt="Task Scheduler - General" width="75%" />
  </div>
</div>
