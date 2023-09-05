from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from workshop.common.forms import CommentForm
from workshop.common.views import get_user_liked_photos, apply_likes_count, apply_user_liked_photos
from workshop.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from workshop.photos.models import Photo
from django.views import generic as views


class PhotoAddView(views.CreateView):
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photo details', kwargs={
            'pk': self.object.pk,
        })


# @login_required
# def add_photo(request):
#     if request.method == 'GET':
#         form = PhotoCreateForm()
#     else:
#         form = PhotoCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             photo = form.save()
#             return redirect('photo details', pk=photo.pk)
#     context = {
#         'form': form,
#     }
#     return render(request, template_name='photos/photo-add-page.html', context=context)



@login_required
def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    comment_form = CommentForm()
    context = {
        'photo': photo,
        'likes_count': apply_likes_count(photo),
        'is_liked_by_user': apply_user_liked_photos(photo),
        'comment_form': comment_form,
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)


@login_required
def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PhotoEditForm()
    else:
        form = PhotoEditForm()
        if form.is_valid():
            form.save()
            redirect('photo details', pk=pk)
    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, template_name='photos/photo-edit-page.html', context=context)


@login_required
def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PhotoDeleteForm()
    else:
        form = PhotoDeleteForm()
        photo.delete()
        redirect('homepage')
    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, template_name='photos/photo-delete-page.html', context=context)

