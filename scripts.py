import os
import random

import django
from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid, Subject)
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


def get_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except MultipleObjectsReturned:
        print('Найдено учеников больше, чем один. Уточните имя!')
    except ObjectDoesNotExist:
        print('Ученик не найден, проверьте правильность имени')


def get_subject(commendation_subject, schoolkid):
    try:
        subject = Subject.objects.get(title=commendation_subject,
                                      year_of_study=schoolkid.year_of_study
                                      )
        return subject
    except ObjectDoesNotExist:
        print('Предмет не найден, проверьте правильность названия')


def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    bad_marks = Mark.objects.filter(schoolkid=schoolkid,
                                    points__lt=4
                                    )
    for mark in bad_marks:
        mark.points = random.randint(4, 5)
        mark.save()
    print(f'Оценки для {schoolkid_name} исправлены')


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    chatisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chatisements.delete()
    print(f'Замечания для {schoolkid_name} убраны')


def get_commendation(schoolkid_name, commendation_subject):
    schoolkid = get_schoolkid(schoolkid_name)
    commendation = [
        "Молодец",
        "Отлично",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!"
    ]
    if not schoolkid:
        return
    subject = get_subject(commendation_subject=commendation_subject,
                          schoolkid=schoolkid
                          )
    if not subject:
        return
    lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                    group_letter=schoolkid.group_letter,
                                    subject=subject
                                    )
    text_commendation = random.choice(commendation)
    Commendation.objects.create(text=text_commendation,
                                created=lessons.first().date,
                                schoolkid=schoolkid,
                                teacher=lessons.first().teacher,
                                subject=subject
                                )
    print(f'Добавлена похвала для {schoolkid_name} по предмету '
          f'{subject}: {text_commendation}')
