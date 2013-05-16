# -*- coding: utf-8 -*-

from collections import OrderedDict

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import transaction

import requests
import xml.etree.ElementTree as ET

from .models import *

@login_required
def home(request):
    return render(request, "{0}/{1}.html".format(settings.SITE_LAYOUT, "home"), locals())

def login_view(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("home")# Redirect to a success page.
        else:
            wrong = True

        #return HttpResponseRedirect("/account/invalid/")# Return a 'disabled account'
    return render(request, "{0}/{1}.html".format(settings.SITE_LAYOUT, "login"), locals())

@login_required
def search(request):

    if not request.GET.get('search', None):
        return redirect("home")# Redirect to a success page.

    response = requests.get('http://thetvdb.com/api/GetSeries.php?seriesname={query}&user={settings.THETVDB_ACCOUNT_ID}'.format(settings=settings, query=request.GET.get("search")))
    root = ET.fromstring(response.content)
    results = OrderedDict()

    for xmlserial in root.findall('Series'):
        results[xmlserial.find('seriesid').text] = xmlserial.find('SeriesName').text

    return render(request, "{0}/{1}.html".format(settings.SITE_LAYOUT, "search"), locals())

@login_required
def create(request, thetvdb_id):

    serial = get_or_none(Serial, thetvdb_id=thetvdb_id)

    if serial:
        return redirect(reverse('serial', kwargs={'slug': serial.slug})) # redirect

    # creazione

    response = requests.get('http://thetvdb.com/api/{settings.THETVDB_API_KEY}/series/{thetvdb_id}/all/en.xml'.format(settings=settings, thetvdb_id=thetvdb_id))
    root = ET.fromstring(response.content)

    serial = Serial.objects.create(
            name=root.find('.//Series/SeriesName').text,
            imdb_id=root.find('.//Series/IMDB_ID').text,
            thetvdb_id=root.find('.//Series/id').text,
            thetvdb_last_updated=root.find('.//Series/lastupdated').text,
            )

    seasons = []

    for episode in root.findall('Episode'):

        try:
            seasons[int(float(episode.find('Combined_season').text))] = int(float(episode.find('Combined_episodenumber').text))
        except IndexError:
            seasons.append(int(float(episode.find('Combined_episodenumber').text)))

    for idx, val in enumerate(seasons):
        Season.objects.create(
                serial=serial,
                number=idx,
                episode_number=val,
                )

    return render(request, "{0}/{1}.html".format(settings.SITE_LAYOUT, "search"), locals())

def serial(request, slug):

    serial = get_object_or_404(Serial, slug=slug)

    if serial in request.user.serials.all():
        user_serial = request.user.x_serials.get(serial=serial)

    return render(request, "{0}/{1}.html".format(settings.SITE_LAYOUT, "serial"), locals())

@transaction.commit_on_success
def watch(request, serial_id, episode, season_number):

    serial = get_object_or_404(Serial, id=serial_id)

    user_serial_qs = request.user.x_serials.filter(serial=serial)

    user_serial, created = UserSerial.objects.get_or_create(
        user=request.user, serial=serial,
        defaults={
            'language': Language.objects.get(iso="IT"),
            'completed': False,
            'current_season': serial.seasons.get(number=1),
            'last_episode_seen': 0,
            })

    user_serial.watch_next_episode()

    return redirect('serial', slug=serial.slug)# Redirect to a success page.
