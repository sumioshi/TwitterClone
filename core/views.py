from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Tweet, Profile
from .forms import TweetForm

@login_required(login_url='login')
def feed_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            profile, created = Profile.objects.get_or_create(user=request.user)  # Garante que o Profile existe
            tweet.author = profile  # Salva o autor como o perfil do usuário logado
            tweet.save()
            messages.success(request, 'Seu tweet foi publicado com sucesso!')
            return redirect('feed')
    else:
        form = TweetForm()

    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'core/feed.html', {'form': form, 'tweets': tweets})

@login_required(login_url='login')
def delete_tweet(request, id):
    tweet = get_object_or_404(Tweet, id=id)

    # Verifica se o usuário logado é o autor do tweet
    if tweet.author.user != request.user:
        messages.error(request, "Você não tem permissão para excluir este tweet.")
        return redirect('feed')  # Redireciona de volta ao feed com a mensagem de erro

    if request.method == 'POST':
        tweet.delete()
        messages.success(request, "Tweet excluído com sucesso.")
        return redirect('feed')

    return redirect('feed')  # Caso alguém acesse diretamente a URL de exclusão, redireciona ao feedder(request, 'core/delete_confirmation.html', {'tweet': tweet})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Mensagem de boas-vindas ao logar com sucesso
                messages.success(request, f'Bem-vindo, {username}! Você se logou com sucesso.')
                return redirect('feed')
        else:
            # Mensagem de erro para credenciais incorretas
            messages.error(request, 'Credenciais incorretas. Por favor, tente novamente.')
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Cria o perfil para o usuário registrado
            login(request, user)
            # Mensagem de sucesso ao registrar e logar automaticamente
            messages.success(request, 'Cadastro realizado com sucesso! Bem-vindo!')
            return redirect('feed')
        else:
            for msg in form.errors.as_data():
                messages.error(request, form.errors[msg])
    else:
        form = UserCreationForm()

    return render(request, 'core/register.html', {'form': form})

@login_required(login_url='login')
def logout_view(request):
    # Limpa todas as mensagens antes de adicionar a mensagem de logout
    storage = messages.get_messages(request)
    storage.used = True  # Isso garante que as mensagens anteriores sejam removidas
    logout(request)
    # Mensagem específica apenas para logout
    messages.success(request, 'Você saiu da conta com sucesso.')
    return redirect('login')

@login_required(login_url='login')
def create_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            profile = Profile.objects.get(user=request.user)
            Tweet.objects.create(author=profile, content=content)
            messages.success(request, 'Seu tweet foi publicado com sucesso!')
            return redirect('feed')
    return render(request, 'core/create_tweet.html')
