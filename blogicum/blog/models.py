from django.contrib.auth import get_user_model
from django.db import models

from abstract.models import PublishedModel


User = get_user_model()


class Category(PublishedModel):
    """
    Модель представляет категорию, использующуюся для группировки объектов.

    Атрибуты:
        title: CharField -- Заголовок категории. Используется для
                            отображения и идентификации категории.
                            Ограничено 256 символами.
        description: TextField -- Полное описание категории.
                                Может содержать более подробную информацию.
        slug:  SlugField -- Уникальный идентификатор категории, который
                            используется в URL. Должен быть уникальным и
                            может содержать только буквы латиницы, цифры,
                            дефис и подчёркивание. Полезен для создания
                            удобных для SEO адресов.

    Метаданные:
        verbose_name (str): Человеко-читаемое имя
                            для единственного объекта - "категория".
        verbose_name_plural (str): Человеко-читаемое имя
                                для набора объектов - "Категории".

    Методы:
        __str__: Возвращает строковое представление объекта,
                совпадающее с его заголовком.
    """

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; '
            'разрешены символы латиницы, цифры, дефис и подчёркивание.'
        ),
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        if len(self.title) > 20:
            return self.title[:20] + '...'
        return self.title


class Location(PublishedModel):
    """
    Модель представляет местоположение, используемое в системе.

    Атрибуты:
        name: CharField -- Название места, ограниченное 256 символами.
            Используется для идентификации и отображения местоположений.

    Метаданные:
        verbose_name: str -- Человеко-читаемое имя для
                            единственного объекта - "местоположение".
        verbose_name_plural: str -- Человеко-читаемое имя для
                                    набора объектов - "Местоположения".

    Методы:
        __str__: Возвращает строковое представление объекта,
                совпадает с его названием места.
    """

    name = models.CharField(max_length=256, verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        if len(self.name) > 20:
            return self.name[:20] + '...'
        return self.name


class Post(PublishedModel):
    """
    Модель представляет публикацию в системе.

    Атрибуты:
        title: CharField -- Заголовок публикации, ограниченный 256 символами.
        text: TextField -- Основной текст публикации.
        pub_date: DateTimeField -- Дата и время публикации.
        Если установлено в будущем, позволяет создание отложенных публикаций.
        author: ForeignKey -- Владелец публикации, связанный с моделью User.
        При удалении пользователя удаляются его публикации.
        location: ForeignKey -- Местоположение, связано с моделью Location.
        Может быть пустым или отсутствующим.
        category: ForeignKey -- Категория публикации, связана с моделью
        Category. Может быть пустым или отсутствующим.

    Метаданные:
        verbose_name: str -- Человеко-читаемое имя
                        единственного объекта - "публикация".
        verbose_name_plural: str -- Человеко-читаемое название для
                                    набора объектов - "Публикации".

    Методы:
        __str__: Возвращает строковое представление объекта,
                совпадает с его заголовком.
    """

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем — можно '
            'делать отложенные публикации.'
        )
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        if len(self.title) > 20:
            return self.title[:20] + '...'
        return self.title
