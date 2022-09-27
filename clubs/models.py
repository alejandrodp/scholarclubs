from django.contrib.auth.models import User
from django.db.models import Model, CharField, PositiveSmallIntegerField, ForeignKey, CASCADE


class Club(Model):
    name = CharField(max_length=100, unique=True)
    student = ForeignKey(User, on_delete=CASCADE)
    LANG = 0
    ARTS = 1
    SPORTS = 2
    MUSIC = 3
    OTHERS = 4

    TAG_CHOICES = (
        (LANG, 'Idiomas'),
        (ARTS, 'Artes'),
        (SPORTS, 'Deportes'),
        (MUSIC, 'Música'),
        (OTHERS, 'Otros'),
    )
    tag = PositiveSmallIntegerField(choices=TAG_CHOICES)

    def __str__(self):
        return f"{self.name}, Category: {self.TAG_CHOICES[self.tag][1]}"
