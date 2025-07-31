from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import get_object_or_404



@api_view(['POST'])
def article_new(request):
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST

        title = data.get('title')
        content = data.get('content')
        user_id = data.get('user_id')

        if not all([title, content, user_id]):
            return Response(
                {'error': 'Tous les champs (title, content, user_id) sont requis'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Vérifie que l'utilisateur existe
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)

        article = Article(title=title, content=content, user=user)
        article.save()

        return Response(
            {'message': 'Article créé avec succès', 'id': article.id},
            status=status.HTTP_201_CREATED
        )

    except json.JSONDecodeError:
        return Response({'error': 'JSON invalide'}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@login_required
def article_new_html(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if not all([title, content]):
            error = 'Tous les champs sont requis.'
            return render(request, 'newpost.html', {'error': error})

        article = Article(title=title, content=content, user=request.user)
        article.save()
        return redirect('accueil')
    else:
        return render(request, 'newpost.html')

@login_required
def delete_post(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    if request.method == 'POST':
        
        if article.user == request.user :
            article.delete()
        return redirect('profile')
    return render(request, 'delete_post.html', {'article': article})

@login_required
def edit_post(request, article_id):
    article = get_object_or_404(Article, id = article_id)

    if article.user != request.user:
        return redirect('profile')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if not all([title, content]):
            error = "Tous les champs sont requis."
            return render(request, 'edit_post.html', {'article': article, 'error': error})

        article.title = title
        article.content = content
        article.save()
        return redirect('profile')
    
    return render(request, 'edit_post.html', {'article': article})
