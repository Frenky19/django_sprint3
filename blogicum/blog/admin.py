from django.contrib import admin

from .models import Category, Location, Post


admin.site.empty_value_display = 'Не задано'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Настраивает отображение и функциональность модели Post в админке.

    Атрибуты:
        list_display: tuple -- Определяет поля, которые будут
                            отображаться в списке записей.
        list_editable: tuple -- Указывает поля, которые можно
                                редактировать прямо из списка.
        search_fields: tuple -- Перечисляет поля, по которым можно
                            осуществлять поиск через панель администратора.
        list_filter: tuple -- Определяет фильтры, которые можно
                            применять в списке записей.
        list_display_links: tuple -- Устанавливает, какие поля являются
                    ссылками на детальное представление из списка записей.
    """

    list_display = (
        'title',
        'is_published',
        'category',
        'location',
        'author',
        'pub_date',
        'created_at',
    )
    list_editable = (
        'is_published',
        'location',
        'category',
    )
    search_fields = (
        'title',
        'category',
        'location',
        'is_published',
        'author',
        'pub_date',
        'created_at',
    )
    list_filter = (
        'is_published',
        'category',
        'location',
        'author',
        'pub_date',
        'created_at',
    )
    list_display_links = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Настраивает отображение и функциональность модели Category в админке.

    Атрибуты:
        list_display: tuple -- Определяет поля, которые будут
                            отображаться в списке записей.
        list_editable: tuple -- Указывает поля, которые можно
                                редактировать прямо из списка.
        search_fields: tuple -- Перечисляет поля, по которым можно
                            осуществлять поиск через панель администратора.
        list_filter: tuple -- Определяет фильтры, которые можно
                            применять в списке записей.
        list_display_links: tuple -- Устанавливает, какие поля являются
                    ссылками на детальное представление из списка записей.
    """

    list_display = (
        'title',
        'is_published',
        'slug',
        'created_at',
    )
    list_editable = (
        'is_published',
    )
    search_fields = (
        'title',
        'is_published',
        'created_at',
    )
    list_filter = (
        'title',
        'is_published',
        'created_at',
    )
    list_display_links = ('title',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """
    Настраивает отображение и функциональность модели Location в админке.

    Атрибуты:
        list_display: tuple -- Определяет поля, которые будут
                            отображаться в списке записей.
        list_editable: tuple -- Указывает поля, которые можно
                                редактировать прямо из списка.
        search_fields: tuple -- Перечисляет поля, по которым можно
                            осуществлять поиск через панель администратора.
        list_filter: tuple -- Определяет фильтры, которые можно
                            применять в списке записей.
        list_display_links: tuple -- Устанавливает, какие поля являются
                    ссылками на детальное представление из списка записей.
    """

    list_display = (
        'name',
        'is_published',
        'created_at',
    )
    list_editable = (
        'is_published',
    )
    search_fields = (
        'name',
        'is_published',
        'created_at',
    )
    list_filter = (
        'name',
        'is_published',
        'created_at',
    )
    list_display_links = ('name',)

