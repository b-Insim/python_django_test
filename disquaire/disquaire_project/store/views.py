from django.shortcuts import render, get_object_or_404
from .models import Album, Artist, Contact, Booking
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from .forms import ContactForm


from .models import Album, Artist, Contact, Booking
from .forms import ContactForm, ParagraphErrorList


def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    context = {
        'albums': albums
    }
    return render(request, 'store/index.html', context)

def listing(request):
    albums_list = Album.objects.filter(available=True)
    paginator = Paginator(albums_list, 9)
    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        albums = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        albums = paginator.page(paginator.num_pages)
    context = {
        'albums': albums,
        'paginate': True
    }
    return render(request, 'store/listing.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    artists_name = " ".join([artist.name for artist in album.artists.all()])
    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            email = request.POST.get('email')
            name = request.POST.get('name')
            
            contact = Contact.objects.filter(email=email)
            if not contact.exists():
                contact = Contact.objects.create(
                    email=email,
                    name=name
                )
            album = get_object_or_404(Album, id=album_id)
            booking = Booking.objects.create(
                contact=contact,
                album=album
            )
            album.available = False
            album.save()
            context = {
                'album_title': album.title
            }
            return render(request, 'store/merci.html', context)
        else:
            context['errors'] = form.errors.items()
    else:
        form = ContactForm()

    context['form'] = form
    return render(request, 'store/detail.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)

    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)

    title = "Résultats pour la requête %s"%query
    context = {
        'albums': albums,
        'title': title
    }

    return render(request, 'store/search.html', context)