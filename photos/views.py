from django.shortcuts import render


def gallery(request):
    return render(request, 'photos/gallery.html')


def photoView(request, pk):
    return render(request, 'photos/photo.html')


def addPhoto(request):
    return render(request, 'photos/add.html')
