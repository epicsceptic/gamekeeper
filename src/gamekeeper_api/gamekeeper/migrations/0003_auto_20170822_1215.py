# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-22 12:15
from __future__ import unicode_literals

from django.db import migrations

import datetime

def get_records():
    return [
        {'andrew':[1],'keith':[2,3]},
        {'keith':[1,2,3],'glen':[]},
        {'keith':[1,2,3],'alec':[]},
        {'andrew':[1,2,3],'alec':[]},
        {'zaheer':[1,2],'alec':[3]},
        {'zaheer':[1],'andrew':[2,3]},
        {'keith':[1,2,3],'adrian':[]},
        {'tshepo':[1,2,3],'andrew':[]},
        {'glen':[1,2],'alec':[3]},
        {'keith':[1,2,3],'tshepo':[]},
        {'alec':[1],'tshepo':[2,3]},
        {'alec':[1,2],'adrian':[3]},
        {'tshepo':[1,2,3],'adrian':[]},
        {'andrew':[1,2],'glen':[3]},
        {'tshepo':[1,2],'glen':[3]},
        {'adrian':[1,2],'glen':[3]},
        {'andrew':[1,2],'adrian':[3]},
        {'zaheer':[3],'keith':[1,2]},
        {'zaheer':[3],'tshepo':[1,2]},
        {'zaheer':[1,2,3],'adrian':[]},
    ]

def import_scores(apps, schema_editor):
    Event = apps.get_model('gamekeeper', 'Event')
    Player = apps.get_model('gamekeeper', 'Player')
    Action = apps.get_model('gamekeeper', 'Action')
    ActionResult = apps.get_model('gamekeeper', 'ActionResult')
    Rule = apps.get_model('gamekeeper', 'Rule')
    league_event = Event.objects.filter(parent_id__isnull=True)[0]
    base_match = Event.objects.filter(name="Match 42")[0]
    game_win = Action.objects.filter(description="Game win")[0]
    game_loss = Action.objects.filter(description="Game loss")[0]
    high_score_action = Action.objects.filter(description="High score")[0]
    low_score_forced_action = Action.objects.filter(description="Bowled opponent out for lowest score")[0]
    high_score_rule = Rule.objects.filter(description="High score")[0]
    low_score_forced_rule = Rule.objects.filter(description="Bowled opponent out for lowest score")[0]
    base_game = base_match.child_events.all()[0]
    week_start = datetime.datetime.strptime('14 Aug 2017', '%d %b %Y')
    week_end = datetime.datetime.strptime('18 Aug 2017', '%d %b %Y')
    records = get_records()

    idx = 43

    for record in records:
        try:
            bonus = record.pop('bonus')
        except KeyError:
            bonus = None

        player1, player2 = map(lambda s: s.capitalize(), record)
        
        player1 = Player.objects.filter(full_name=player1)[0]
        player2 = Player.objects.filter(full_name=player2)[0]
        player1_score, player2_score = record.values()
        match = Event.objects.create(game=league_event.game,
                                     parent=league_event,
                                     name="Match %i" % idx,
                                     description="week 3",
                                     start_datetime=week_start,
                                     end_datetime=week_end)
        for rule in base_match.rules.all():
            match.rules.add(rule)
        match.rules.add(high_score_rule)
        match.rules.add(low_score_forced_rule)
        match.players.add(player1)
        match.players.add(player2)

        game1 = Event.objects.create(game=league_event.game,
                                     parent=match,
                                     name="Game 1",
                                     start_datetime=week_start,
                                     end_datetime=week_end)
        for action in base_game.actions.all():
            game1.actions.add(action)
        game1.actions.add(high_score_action)
        game1.actions.add(low_score_forced_action)
        game1.players.add(player1)
        game1.players.add(player2)
        
        game2 = Event.objects.create(game=league_event.game,
                                     parent=match,
                                     name="Game 2",
                                     start_datetime=week_start,
                                     end_datetime=week_end)
        for action in base_game.actions.all():
            game2.actions.add(action)
        game2.actions.add(high_score_action)
        game2.actions.add(low_score_forced_action)
        game2.players.add(player1)
        game2.players.add(player2)
        
        game3 = Event.objects.create(game=league_event.game,
                                     parent=match,
                                     name="Game 3",
                                     start_datetime=week_start,
                                     end_datetime=week_end)
        for action in base_game.actions.all():
            game3.actions.add(action)
        game3.actions.add(high_score_action)
        game3.actions.add(low_score_forced_action)
        game3.players.add(player1)
        game3.players.add(player2)

        for i in player1_score:
            game = match.child_events.all().filter(name="Game %i" % i)[0]
            ActionResult.objects.create(event=game,
                                        player=player1,
                                        action=game_win)
            ActionResult.objects.create(event=game,
                                        player=player2,
                                        action=game_loss)

        for i in player2_score:
            game = match.child_events.all().filter(name="Game %i" % i)[0]
            ActionResult.objects.create(event=game,
                                        player=player2,
                                        action=game_win)
            ActionResult.objects.create(event=game,
                                        player=player1,
                                        action=game_loss)
            
        idx+=1

class Migration(migrations.Migration):

    dependencies = [
        ('gamekeeper', '0002_auto_20170820_1924'),
    ]

    operations = [
        migrations.RunPython(import_scores),
    ]
