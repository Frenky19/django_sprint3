from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.constants import POSTS_LIMIT
from blog.models import Category, Post


def index(request):
    """
    Выводит 5 последних по времени постов на главную страницу.

    'blog/index.html' -- шаблон рендеринга
    Фильтрация постов:
    -дата публикации не позднее теущей даты (можно делать отложенные посты)
    -пост опубликован
    -категория поста опубликована
    """
    template_name = 'blog/index.html'
    now = timezone.now()
    posts = (
        Post.objects
        .filter(
            pub_date__lte=now,
            is_published=True,
            category__is_published=True
        )
        .order_by('-pub_date')[:POSTS_LIMIT]
    )
    context = {'posts': posts}
    return render(request, template_name, context)


def post_detail(request, post_id):
    """
    Принимает номер поста. Возвращает содержимое отдельного поста.

    Возвращает ошибку 404, если поста с указанным id не существует.
    post_id: int -- идентификационный номер('id') поста
    'blog/detail.html' -- шаблон рендеринга
    """
    template_name = 'blog/detail.html'
    now = timezone.now()
    post = get_object_or_404(
        Post.objects.filter(
            pub_date__lte=now,
            is_published=True,
            category__is_published=True
        ),
        id=post_id
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    """
    Принимает категорию поста. Возвращает список постов отдельной категории.

    Возвращает ошибку 404, если категории не существует
    category_slug: slug -- идентификатор категории
    'blog/category.html' -- шаблон рендеринга
    Фильтрация категорий:
    -Категория опубликована
    -Идентификатор категории соответсвует принимаему category_slug
    """
    template_name = 'blog/category.html'
    now = timezone.now()
    category = (
        Category.objects
        .filter(
            slug=category_slug,
            is_published=True
        )
        .first()
    )
    if not category:
        raise Http404('Такой категории пока что не существует')
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=now
    ).order_by('-pub_date')
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, template_name, context)
