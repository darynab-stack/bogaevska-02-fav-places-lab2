"""
Views for the favorite places app.

created on: 14/09/2026
created by: Daryna Bogaevska
"""

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
    """Show the home page with a random place suggestion."""
    return render(request, "places/home.html", {})


def place_add(request):
    """Show the form for adding a new place."""
    return render(request, "places/place_form.html", {})
