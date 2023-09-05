from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from workshop.common.forms import CommentForm
from workshop.pets.models import Pet
from workshop.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm


@login_required
def add_pet(request):
    form = PetCreateForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = request.user
        pet.save()
        return redirect('profile details', pk=pet.user.id)
    context = {'form': form}
    return render(request, 'pets/pet-add-page.html', context=context)


@login_required
def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('homepage')
    form = PetDeleteForm(instance=pet)
    context = {
        'form': form,
    }
    return render(request, 'pets/pet-delete-page.html', context=context)


@login_required
def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    photos_count = all_photos.count()
    comment_form = CommentForm()
    context = {
        'pet': pet,
        'all_photos': all_photos,
        'photos_count': photos_count,
        'comment_form': comment_form,
    }
    return render(request, 'pets/pet-details-page.html', context=context)


@login_required
def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', username, pet_slug)
    context = {
        'form': form,
    }
    return render(request, 'pets/pet-edit-page.html', context=context)
