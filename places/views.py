"""
Views for the favorite places app.

created on: 14/09/2026
created by: Daryna Bogaevska
"""

import random

from django.http import Http404
from django.shortcuts import render

from .data import DEFAULT_PLACES


def get_all_places(request):
    """
    Return fixed places plus the ones added in this session.
    """
    user_places = request.session.get("user_places", [])
    return DEFAULT_PLACES + user_places


def place_list(request):
    """
    Show the full list of favorite places.
    """
    places = get_all_places(request)
    return render(request, "places/place_list.html", {"places": places})


def home(request):
    """
    Show the home page with an optional random place suggestion.
    """
    suggestion = None
    if request.GET.get("suggest"):
        places = get_all_places(request)
        weights = [place["rating"] for place in places]
        suggestion = random.choices(places, weights=weights, k=1)[0]
    return render(request, "places/home.html", {"place": suggestion})


def place_add(request):
    """Show the form for adding a new place."""
    return render(request, "places/place_form.html", {})


def place_detail(request, place_id):
    """Show one place with its full description."""
    places = get_all_places(request)
    for place in places:
        if place["id"] == place_id:
            return render(request, "places/place_detail.html", {"place": place})
    raise Http404("Place not found")
