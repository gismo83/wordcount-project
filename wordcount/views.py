from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request,'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    text = fulltext.split()
    count_list = {}
    count = 0
    for word in text:
        count += 1
        try:
            count_list[word] += 1
        except KeyError:
            count_list[word] = 1

    print('Es sind ' + str(count) + ' Wörter ' + str(count_list))
    sorted_words = sorted(count_list.items(),key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html', {'count': count, 'dict': sorted_words, 'fulltext': fulltext})


def eggs(request):
    return render(request, 'eggs.html')


def about(request):
    return render(request, 'about.html')
