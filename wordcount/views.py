from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    worldlist = fulltext.split()

    wordDictionary = {}
    for word in worldlist:
        if word in wordDictionary:
            # Increase
            wordDictionary[word] += 1
        else:
            # add to the wordDictionary
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(),
                         key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(worldlist), 'sortedWords': sortedWords})
