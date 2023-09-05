from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from workshop.accounts.forms import RegisterUserForm, LoginUserForm, EditUserForm


UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('homepage')


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class EditUserView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    form_class = EditUserForm
    model = UserModel

    def get_success_url(self):
        return reverse_lazy(
            'profile details',
            kwargs={'pk': self.object.pk}
        )


class DetailsUserView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = self.request.user.pet_set.all()

        return context


class DeleteUserView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('login')

    def post(self, *args, pk):
        self.request.user.delete()
