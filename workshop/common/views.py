from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy
from workshop.common.forms import CommentForm, SearchForm
from workshop.common.models import Like
from workshop.photos.models import Photo


def apply_likes_count(photo):
    photo.likes_count = photo.like_set.count()
    return photo


def apply_user_liked_photos(photo):
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def homepage(request):
    all_photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    all_photos = [apply_user_liked_photos(photo) for photo in all_photos]
    comment_form = CommentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = Photo.objects.all().filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(request, template_name='common/home-page.html', context=context)


@login_required
def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def get_user_liked_photos(photo_id):
    return Like.objects.filter(to_photo_id=photo_id)


@login_required
def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_id,
        )

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required
def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
