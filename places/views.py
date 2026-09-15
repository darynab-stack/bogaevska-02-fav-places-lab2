"""
Views for the favorite places app.

created on: 14/09/2026
created by: Daryna Bogaevska
"""

import random
from datetime import date

from django.http import Http404
from django.shortcuts import redirect, render

from .data import DEFAULT_PLACES
from .forms import NewPlaceForm


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
    """Add a new place to the current session list."""
    if request.method == "POST":
        form = NewPlaceForm(request.POST)
        if form.is_valid():
            user_places = request.session.get("user_places", [])
            all_places = get_all_places(request)
            new_place = {
                "id": max(place["id"] for place in all_places) + 1,
                "name": form.cleaned_data["name"],
                "place_type": form.cleaned_data["place_type"],
                "location": form.cleaned_data["location"],
                "rating": form.cleaned_data["rating"],
                "description": form.cleaned_data["description"],
                "created_at": date.today().isoformat(),
            }
            user_places.append(new_place)
            request.session["user_places"] = user_places
            return redirect("places:place_list")
        return render(request, "places/place_form.html", {"form": form})
    return render(request, "places/place_form.html", {"form": NewPlaceForm()})


def place_detail(request, place_id):
    """Show one place with its full description."""
    places = get_all_places(request)
    for place in places:
        if place["id"] == place_id:
            return render(request, "places/place_detail.html", {"place": place})
    raise Http404("Place not found")
