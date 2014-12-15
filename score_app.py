"""This is the main score app"""
from flask import Flask, render_template, request
from team import Team
from game import Game

app = Flask(__name__)
GAME = Game()
@app.route('/')
def hello_world():    
    return render_template('index.html',name1=str(Team1.name),score1=str(Team1.score),name2=str(Team2.name),score2=str(Team2.score))
    

if __name__ == '__main__':
    Team1 = Team('Miami',0)
    Team2 = Team('Lakers',0)
    GAME.add_team(Team1)
    GAME.add_team(Team2)
    print "Game has been started!"
    print   
    app.run()
    while True:    	
    	print "##MENU##"
    	print "1 = Add score to", Team1.name
    	print "2 = Add score to", Team2.name
        question1 = raw_input("Selection: ")
        if len(question1) > 0:
            answer1 = question1 #question1.upper()
            if answer1 == "1":
                print "How many points for", Team1.name, "?"
                print "1 = 1 point"
                print "2 = 2 points"
                print "3 = 3 points"
                answer2 = raw_input("Selection: ")
                if len(answer2) > 0:
                	if answer2 == "1":
                		GAME.add_score(Team1,1)
                		print "1 Point has been added to", Team1.name
                	elif answer2 == "2":
                		GAME.add_score(Team1,2)
                		print "2 points has been added to", Team1.name
                	elif answer2 == "3":
                		GAME.add_score(Team1,3)
                		print "3 points has been added to", Team1.name
                	else:
                		print "Invalid input!"
                #break
            elif answer1 == "2":
                print "How many points for", Team2.name, "?"
                print "1 = 1 point"
                print "2 = 2 point"
                print "3 = 3 point"
                answer2 = raw_input("Selection: ")
                if len(answer2) > 0:
                	if answer2 == "1":
                		GAME.add_score(Team2,1)
                		print "1 Point has been added to", Team2.name
                	elif answer2 == "2":
                		GAME.add_score(Team2,2)
                		print "2 points has been added to", Team2.name
                	elif answer2 == "3":
                		GAME.add_score(Team2,3)
                		print "3 points has been added to", Team2.name
                	else:
                		print "Invalid input!"
                #break
            else:
                print "Invalid input!"
        print "Latest Scores:"
        print Team1.name," = ",GAME.get_team_score(Team1)
        print Team2.name," = ",GAME.get_team_score(Team2)
        print
        print
        hello_world()
        
        

    #cProfile.run('app.run(debug=True)', sort='time')
    #app.run(debug=True)
    




    
