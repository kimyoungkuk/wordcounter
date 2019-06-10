from django.shortcuts import render
import logging

# Create your views here.

def home(request):

    return render(request, 'home.html')


def about(request):

    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
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
