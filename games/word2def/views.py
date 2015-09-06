
import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.apps import apps

from engine.utils.views import QuestionView

from .game import Game
from .models import Question, Definition

ACCESS_TOKEN_IO = getattr(settings, 'ACCESS_TOKEN_IO')
ACCESS_TOKEN_STORE = getattr(settings, 'ACCESS_TOKEN_STORE')


class Word2DefQuestionView(QuestionView):
    template_name = 'word2def/game_play.html'

    def __init__(self, *args, **kwargs):
        super(Word2DefQuestionView, self).__init__(*args, **kwargs)
        app = apps.get_app_config('word2def')
        self._app = self.games_qs.get(name=app.get_module())
        self._game = Game(ACCESS_TOKEN_IO, ACCESS_TOKEN_STORE)
