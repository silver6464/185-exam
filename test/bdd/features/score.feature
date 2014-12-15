
Feature: A scoring application that will record scores given 2 teams in a basketball game.

As a scorer I wish to be able to add scores in a team with scoring 1 pt/2 pts/3 pts
and display the latest scores in a webpage


Scenario: Add 1 point and retrieve score.
Given that "Miami" earned 1 point
When I get the score of "team 1"
Then a score of "1" is returned

Scenario: Get score of "Miami"
Given that "Miami" is added a score of "2"
When I get the score of "Miami"
Then "2" is returned
