from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.constants import POSTS_LIMIT
from blog.models import Category, Post


def get_filtered_posts():
    """
    Возвращает базовый набор постов, отфильтрованный по общим критериям:

    - Дата публикации не позднее текущей даты (можно делать отложенные посты)
    - Пост опубликован
    - Категория поста опубликована
    """
    now = timezone.now()
    return (
        Post.objects
        .select_related(
            'category',
            'location',
            'author'
        ).filter(
            pub_date__lte=now,
            is_published=True,
            category__is_published=True
        )
    )


def index(request):
    """
    Выводит 5 последних по времени постов на главную страницу.

    'blog/index.html' -- шаблон рендеринга
    """
    posts = get_filtered_posts()[:POSTS_LIMIT]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """
    Принимает номер поста. Возвращает содержимое отдельного поста.

    Возвращает ошибку 404, если поста с указанным id не существует.
    post_id: int -- идентификационный номер('id') поста
    'blog/detail.html' -- шаблон рендеринга
    """
    post = get_object_or_404(get_filtered_posts(), id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """
    Принимает категорию поста. Возвращает список постов отдельной категории.

    Возвращает ошибку 404, если категории не существует
    Идентификатор категории соответсвует принимаему category_slug
    category_slug: slug -- идентификатор категории
    'blog/category.html' -- шаблон рендеринга
    """
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = (
        get_filtered_posts()
        .filter(category=category)
    )
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category.html', context)
