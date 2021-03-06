# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from dndtools.dnd.menu import menu_item, submenu_item, MenuItem
from dndtools.dnd.dnd_paginator import DndPaginator
from dndtools.dnd.filters import DeityFilter
from dndtools.dnd.models import Deity


@menu_item(MenuItem.CHARACTER_OPTIONS)
@submenu_item(MenuItem.CharacterOptions.DEITIES)
def deity_list(request):
    f = DeityFilter(request.GET, queryset=Deity.objects.all())

    form_submitted = 1 if 'name' in request.GET else 0

    paginator = DndPaginator(f.qs, request)

    return render_to_response('dnd/deities/deity_list.html',
                              {
                                  'request': request,
                                  'deity_list': paginator.items(),
                                  'paginator': paginator,
                                  'filter': f,
                                  'form_submitted': form_submitted,
                              }, context_instance=RequestContext(request), )


@menu_item(MenuItem.CHARACTER_OPTIONS)
@submenu_item(MenuItem.CharacterOptions.DEITIES)
def deity_detail(request, deity_slug):
    # fetch the class
    deity = get_object_or_404(Deity.objects.select_related('favored_weapon', 'favored_weapon__rulebook'), slug=deity_slug)

    return render_to_response('dnd/deities/deity_detail.html',
                              {
                                  'deity': deity,
                                  'request': request,
                                  'i_like_it_url': request.build_absolute_uri(),
                                  'inaccurate_url': request.build_absolute_uri(),
                              }, context_instance=RequestContext(request), )

