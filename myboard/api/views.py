from cms.models import Book

import collections
import json

# Create your views here.
def book_list(request):
    books = []
    for book in Book.objects.all().order_by("id"):
        #get impression
        impressions = []
        for impression in book.impressions.all().order_by("id"):
            impression_dict = OrderedDict([
                ('id', impression.id),
                ('comment', impression.comment),
            ])
            impressions.append(impression_dict)



        book_dict = OrderedDict([
            ('id', book.id),
            ('name', book.name),
            ('publisher', book.publisher),
            ('price', book.price),
         ])
        books.append(book_dict)

    data = OrderedDict([('books', books)])
    return render_json_response(reqeust, data)
def render_json_response(reqeust, data, status=None):
    json_str = json.dumps(data, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  #외부에서 들어올때
    if callbalck:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type="application/javascript;charset=UTF-8", status=status)
    else:
        response = HttpResponse(json_str, content_type="application/json;charset=UTF-8", status=status)
