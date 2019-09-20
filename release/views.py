from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def room(request):
    return render(request, 'release/room.html', {
        'room_name_json': mark_safe(json.dumps('release_data'))
    })
