import os
import random

import django

from datacenter.models import (
    Chastisement,
    Commendation,
    Lesson,
    Mark,
    Schoolkid,
    Subject,
    )
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


def get_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except MultipleObjectsReturned as e:
        print(f'Найдено учеников больше, чем один. Уточните имя!')
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
        mark.points = random.randint(4,5)
        mark.save()
    print(f'Оценки для {schoolkid_name} исправлены')



def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    bad_marks = Mark.objects.filter(schoolkid=schoolkid,
                                    points__lt=4
                                    )
    chatisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chatisements.delete()
    print(f'Замечания для {schoolkid_name} убраны')


def get_commendation(schoolkid_name, commendation_subject):
    schoolkid = get_schoolkid(schoolkid_name)
    commendation = {
        1: "Молодец",
        2: "Отлично",
        3: "Хорошо!",
        4: "Гораздо лучше, чем я ожидал!",
        5: "Ты меня приятно удивил!",
        6: "Великолепно!",
        7: "Прекрасно!",
        8: "Ты меня очень обрадовал!",
        9: "Именно этого я давно ждал от тебя!",
        10: "Сказано здорово – просто и ясно!",
        11: "Ты, как всегда, точен!",
        12: "Очень хороший ответ!",
        13: "Талантливо!",
        14: "Ты сегодня прыгнул выше головы!",
        15: "Я поражен!",
        16: "Уже существенно лучше!",
        17: "Потрясающе!",
        18: "Замечательно!",
        19: "Прекрасное начало!",
        20: "Так держать!",
        21: "Ты на верном пути!",
        22: "Здорово!",
        23: "Это как раз то, что нужно!",
        24: "Я тобой горжусь!",
        25: "С каждым разом у тебя получается всё лучше!",
        26: "Мы с тобой не зря поработали!",
        27: "Я вижу, как ты стараешься!",
        28: "Ты растешь над собой!",
        29: "Ты многое сделал, я это вижу!",
        30: "'Теперь у тебя точно все получится!"
    }
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
    text_commendation = commendation[random.randint(1,30)]
    Commendation.objects.create(text=text_commendation,
                                created=lessons.first().date,
                                schoolkid=schoolkid,
                                teacher=lessons.first().teacher,
                                subject=subject
                                )
    print(f'Добавлена похвала для {schoolkid_name} по предмету {subject}: {text_commendation}')


def main():
    pass


if __name__ == '__main__':
    main()