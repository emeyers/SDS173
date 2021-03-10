
class Baseball_Game:
    
    # Constructor
    def __init__(self): 

        self.end_of_game = False
        self.inning = 1
        self.top_of_inning = True
        self.outs = 0
        self.balls = 0
        self.strikes = 0
        self.runner_on_first = False
        self.runner_on_second = False
        self.runner_on_third = False
        self.home_score = 0
        self.away_score = 0
 
    
    # for printing the game state
    def __str__(self):
        
        if self.top_of_inning:
            top_bottom_inning_name = "top"
        else:
            top_bottom_inning_name = "bottom"
          
        if self.inning == 1:
            inning_suffix = "st"
        elif self.inning == 2:
            inning_suffix = "nd"
        elif self.inning == 3:
            inning_suffix = "rd"
        else:
            inning_suffix = "th"
        
        inning_string = "{} of the {}{}\n".format(top_bottom_inning_name, self.inning, inning_suffix)
        
        score_string = "Away: {}   Home: {}\n".format(self.away_score, self.home_score)
        
        # should fix the plural on outs, balls and strikes
        outs_balls_strikes_string = "{} outs, {} balls, and {} strikes\n".format(self.outs, self.balls, self.strikes)
        
        running_string = ""
        if self.runner_on_first:
            running_string = "runner on 1st\n"
        
        if self.runner_on_second:
            running_string = running_string + "runner on 2nd\n"

        if self.runner_on_third:
            running_string = running_string + "runner on 3rd\n"

        if running_string == "":
            running_string = "bases empty\n"
            
        if self.end_of_game:
            end_of_game_string = "end of game"
        else:
            end_of_game_string = ""
            
        #return inning_string + "\n" + score_string + "\n" + "\n" + running_string + "\n" + outs_balls_strikes_string + "\n" + end_of_game_string 
        return inning_string + score_string +  running_string + outs_balls_strikes_string  + end_of_game_string + "\n"
    
    
    
    def update_half_inning(self): 
        
        if self.end_of_game:
            return
        
        # check if it is the end of the game and the home team won
        if (self.inning >= 9) and (self.home_score > self.away_score):
            self.end_of_game = True
            return
        
       # check if it is the end of the visiting team won
        if (self.inning >= 9) and (self.top_of_inning == False) and (self.home_score < self.away_score):
            self.end_of_game = True
            return
        
        
        # otherwise it's not the end of the game so update the half inning
        if self.top_of_inning == True:
            self.top_of_inning = False
        else:
            self.top_of_inning = True
            self.inning = self.inning + 1

        self.outs = 0

        self.runner_on_first = self.runner_on_second = self.runner_on_third = False
    


    def add_runs(self, num_runs = 1):
        
        if self.top_of_inning:
            self.away_score = self.away_score + num_runs
        else:
            self.home_score = self.home_score + num_runs
        

    # add an out
    def add_outs(self, num_outs = 1): 
        
        self.outs = self.outs + num_outs
        self.balls = 0
        self.strikes = 0
        
        if self.outs > 2:
            self.update_half_inning()
      
    # add strike
    def add_strike(self): 
        
        self.strikes = self.strikes + 1

        if self.strikes == 3:
            self.add_outs(1)

    
    def add_runner_on_first(self):
        
        if self.runner_on_first and self.runner_on_second and self.runner_on_third:  
            self.add_runs(1)
            
        elif self.runner_on_first and self.runner_on_second:
            self.runner_on_third = True
        
        elif self.runner_on_first:
            self.runner_on_second = True        
        
        self.runner_on_first = True
        
        # reset the balls and strikes if a runner reaches base
        self.balls = 0
        self.strikes = 0
        
    
    # add ball
    def add_ball(self): 
        
        self.balls = self.balls + 1

        if self.balls == 4:
            self.add_runner_on_first()

            
    def add_single(self):
        
        # runnings from second and third score on a single
        if self.runner_on_third:
            self.add_runs(1)
            self.runner_on_third = False
            
        if self.runner_on_second:
            self.add_runs(1)
            self.runner_on_second = False

        if self.runner_on_first:
            self.runner_on_second = True
    
        self.runner_on_first = True
    
    

    def add_double(self):
        self.add_runs(self.runner_on_first + self.runner_on_second + self.runner_on_third)
        self.runner_on_first = self.runner_on_third = False
        self.runner_on_second = True
        # reset the balls and strikes if a runner reaches base         
        self.balls = 0
        self.strikes = 0
            
            
    def add_triple(self):
        self.add_runs(self.runner_on_first + self.runner_on_second + self.runner_on_third)
        self.runner_on_first = self.runner_on_second = False
        self.runner_on_third = True
        # reset the balls and strikes if a runner reaches base         
        self.balls = 0
        self.strikes = 0
            
    def add_home_run(self):
        self.add_runs(self.runner_on_first + self.runner_on_second + self.runner_on_third + 1)
        self.runner_on_first = self.runner_on_second = self.runner_on_third = False
        # reset the balls and strikes after a home run     
        self.balls = 0
        self.strikes = 0
        
    
    
    
    def display_game(self, batter_name = "", center_string = ""):
        
        import matplotlib.pyplot as plt
        
        # draw the baseball diamond
        plt.plot([0, 1], [0, 1], color = "black");
        plt.plot([0, -1], [2, 1], color = "black");

        plt.axis("square")

        
        
        # put the runners on base
        plt.plot([1], [1], color = "red", marker=".", markersize=25);
       
        
            

        # add the balls, strikes and outs
        plt.text(.7, .3, "Balls: " + str(self.balls));


        
        # add the top and bottom of the innning 

        
        
        # add the scores


        
        # add the center string and batter string
        
        
        
        # turn off the axes to make the plot look better
        plt.axis("off");

        