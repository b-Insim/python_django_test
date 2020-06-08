#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.template import loader
from .models import Reference, Contact, Reservation, Stock, Menu, Comptoir

# def index(request):
#     message = "Salut tout le monde !"
#     return HttpResponse(message)

def index(request):
    menus = Menu.objects.filter(available=True) # .order_by('-ref')
    #formatted_menus = ["<li>{}</li>".format(menu.name) for menu in menus]
    # message = """<ul>{}</ul>""".format("\n".join(formatted_menus))
    # template = loader.get_template('telecom/index.html')
    context = {
        'menus': menus
    }
    return render(request, 'telecom/index.html', context)
    #return HttpResponse(template.render(context, request=request))

# def listing(request):
#     references = ["<li>{}</li>".format(REF['ref']) for REF in REFERENCES]
#     message = """<ul>{}</ul>""".format("\n".join(references))
#     return HttpResponse(message)

def listing(request):
    menus_list = Menu.objects.filter(available=True)
    paginator = Paginator(menus_list, 3)
    page = request.GET.get('page')
    try:
        menus = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        menus = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        menus = paginator.page(paginator.num_pages)
    # formatted_menus = ["<li>{}</li>".format(menu.ref) for menu in menus]
    # message = """<ul>{}</ul>""".format("\n".join(formatted_menus))
    context = {
        'menus': menus
    }
    return render(request, 'telecom/listing.html', context)
    #return HttpResponse(context)


# def detail(request, ref_id):
#     id = int(ref_id) # make sure we have an integer.
#     reference = REFERENCES[id] # get the reference with its id..
#     message = "{}, {}".format(reference['name'], reference['description'])
#     return HttpResponse(message)

def detail(request, ref_id):
    reference = get_object_or_404(Reference, pk=ref_id)
    #reference = Reference.objects.get(pk=ref_id)
    #message = "{}, {}".format(reference['name'], reference['description'])
    context = {
        'reference_ref': reference.ref,
        'reference_name': reference.name,
        'reference_id': reference.id,
    }
    return render(request, 'telecom/detail.html', context)
    #return HttpResponse(context)

def search(request):
    query = request.GET.get('query')
    if not query:
        reference = Reference.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        reference = Reference.objects.filter(ref__icontains=query)

    if not reference.exists():
        reference = Reference.objects.filter(name__icontains=query)

    if not reference.exists():
        message = "Misère de misère, nous n'avons trouvé aucun résultat !"
    else:
        reference = ["<li>{}</li>".format(ref.name) for ref in reference]
        message = """
            Nous avons trouvé les albums correspondant à votre requête ! Les voici :
            <ul>{}</ul>
        """.format("</li><li>".join(reference))
    title = "Résultats pour la requête %s"%query
    context = {
        'reference': reference,
        'title': title
    }
    return render(request, 'telecom/search.html', context)
    #return HttpResponse(context)

# def search(request):
#     query = request.GET.get('query')
#     if not query:
#         message = "Aucune biere n'est demandée"
#     else:
#         references = [
#             ref for ref in REFERENCES
#             if query==ref['name']
#         ]

#         if len(references) == 0:
#             message = "Misère de misère, nous n'avons trouvé aucun résultat !"
#         else:
#             references = ["<li>{}</li>".format(REF['ref']) for REF in REFERENCES]
#             message = """
#                 Nous avons trouvé des bières correspondant à votre requête ! Les voici :
#                 <ul>
#                     {}
#                 </ul>
#             """.format("</li><li>".join(references))

#     return HttpResponse(message)

# def comptoir(request):
#     comptoirs = ["<li>{}</li>".format(comp['name']) for comp in COMPTOIRS]
#     message = """<ul>{}</ul>""".format("\n".join(comptoirs))
#     return HttpResponse(message)

# def stock(request, ID_COMPTOIR):
#     id = int(ID_COMPTOIR) # make sure we have an integer.
#     stocks = STOCKS[id] # get the reference with its id..
#     message = "{}, {}".format(stocks['name'], stocks['description'])
#     return HttpResponse(message)