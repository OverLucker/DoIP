from django.shortcuts import render


# just view to render, nothin more
def main(request):
    return render(
        request,
        'index.html',
        context={}
    )
