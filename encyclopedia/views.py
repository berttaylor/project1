from django.shortcuts import render, redirect
import markdown2
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_detail(request, title):
    try:
        with open(f'entries/{title}.md', 'r') as file:
            content = file.read()
            html_content = markdown2.markdown(content)
    except FileNotFoundError:
        html_content = None

    return render(request, 'encyclopedia/entry_detail.html', {
        "content": html_content
    })

def search_results(request):
    search_query = request.GET.get('q')
    if search_query:
        matching_entries = [entry for entry in util.list_entries() if search_query.lower() in entry.lower()]
        if search_query.lower() in [entry.lower() for entry in util.list_entries()]:
            return redirect('entry_detail', title=search_query)
        else:
            return render(request, 'encyclopedia/searchbox_results.html', {"matching_entries": matching_entries, "search_query": search_query})
    else:
        return redirect('page_not_found')

def page_not_found(request):
    return render(request, "encyclopedia/404.html")

def new_page(request):
    return render(request, "encyclopedia/new_page.html")

def save_new_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            util.save_entry(title, content)
        except util.EntryAlreadyExistsError as e:
            error_message = str(e)
            return render(request, "encyclopedia/new_page.html", {
                "error_message": error_message
            })
        return entry_detail(request, title=title)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def edit_page(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit_page.html", {
        "content": content,
        "title": title
    })

def random_page(request):
    list_of_entries = util.list_entries()
    random_number = random.randint(0, (len(list_of_entries)) -1)
    random_page = list_of_entries[random_number]
    return redirect('entry_detail', title=random_page)
    