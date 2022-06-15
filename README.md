
# Взламывай электронный дневник

Код поможет исправить оценки, убрать замечания и добавить хвалебные отзывы в БД электронного дневника.


## Установка

Для начала скачайте репозиторий электронного дневника в текущую папку с кодом: 
https://github.com/devmanorg/e-diary/tree/master

И настройте БД, как это указано в
https://github.com/devmanorg/e-diary/blob/master/README.md

Не забудьте создать файл ``.env``, пример: 

```
DEBUG=True
SECRET_KEY="2323wfsdfsf"
ALLOWED_HOSTS=''
DATABASE_NAME="schoolbase.sqlite3"
```

Запустите сервер c дневником:

```
$python3 manage.py runserver
```
Дневник будет доступен по указанному адресу.

## Использование скрипта

Запустите ``shell`` в терминале:

```
python3 manage.py shell
```

Введите команду:

```
from scripts import get_schoolkid, fix_marks, get_subject, remove_chastisements, get_commendation
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
```

### Исправление оценок

Для исправления плохих оценок (менье 4 балов) введите следующую команду:
```
fix_marks(schoolkid_name)
```
``schoolkid_name`` - Фамилия и Имя (можно добавить и отчество, если необходимо) ученика формата "Иванов Иван"

Например:

```
fix_marks("Иван Иванов")
```

### Удаление замечаний

Для удаления замечаний от учителей введите следующую команду:
```
remove_chastisements(schoolkid_name)
```
``schoolkid_name`` - Фамилия и Имя (можно добавить и отчество, если необходимо) ученика формата "Иванов Иван"

Например:

```
remove_chastisements("Иван Иванов")
```

### Добавление похвалы от учителей

Для добавления похвалы от учителя введите следующую команду:
```
get_commendation(schoolkid_name, subject)
```
``schoolkid_name`` - Фамилия и Имя (можно добавить и отчество, если необходимо) ученика формата "Иванов Иван"
``subject`` -  Название предмета, например ``"Математика"``

Похвала будет добавлена к последнему уроку по указанному предмету.

Например:

```
get_commendation("Иван Иванов", "Математика")
```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте Devman.