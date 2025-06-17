from django.shortcuts import render

def index(request):
    return render(request, "edtech/index.html")
def live_stt_view(request):
    return render(request, "edtech/live_stt.html")
