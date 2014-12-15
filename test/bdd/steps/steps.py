from lettuce import *
from nose.tools import assert_equal,assert_in
from flask import Flask
from webtest import TestApp
from score_app import app,GAME
from team import Team
from game import Game




@step(u'Given that "([^"]*)" earned 1 point')
def given_that_group1_earned_1_point(step, team_name):
    Team1 = Team(team_name,1)

@step(u'When I get the score of "([^"]*)"')
def when_i_get_the_score_of_group1(step, team_name):
    Team1 = Team(team_name,1)
    GAME.get_team_score(Team1)

@step(u'Then a score of "([^"]*)" is returned')
def then_a_score_of_group1_is_returned(step, team_name):
    Team1 = Team(team_name,1)
    GAME.add_team(Team1)
    score = GAME.get_team_score(Team1)
    assert_equal(1,score)

@step(u'Given that "([^"]*)" has a score of "([^"]*)"')
def given_that_group1_has_a_score_of_group2(step, team_name, score):
    Team1 = Team(team_name,score)
    GAME.add_team(Team1)
@step(u'And "([^"]*)" has a score of "([^"]*)"')
def and_group1_has_a_score_of_group2(step, team_name,score):
    Team2 = Team(team_name,score)
    GAME.add_team(Team2)

@step(u'Then "([^"]*)" and "([^"]*)" are displayed in the webpage')
def then_group1_and_group2_are_displayed_in_the_webpage(step, score1, score2):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)

