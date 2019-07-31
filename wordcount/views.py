from django.shortcuts import render
import logging
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects

    return render(request, 'home.html',{'posts':posts})


def about(request):

    return render(request, 'about.html')

def result(request):
    title = request.GET['title']
    text = request.GET['fulltext']
    post=Post()
    post.title=title
    post.body=text
    post.save()

    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    sorted_word_list=sorted(word_dictionary.items(), key=(lambda x : x[1]), reverse = True)
    word_dictionary=dict(sorted_word_list)
    logging.error(word_dictionary)
    return render(request, 'result.html',{'full':text, 'total':len(words), 'dictionary':word_dictionary.items()})
