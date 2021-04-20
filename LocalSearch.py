"""
Created on Mon Oct 19 19:10:48 2020

@author: christina sarkisyan (will be reffered to as 'chris' from hereon out for brevity)
         Assignment instructions by Sterling 

-Documentation key (for quick search):  
    - #provided: shows where code has been provided by another author (Sterling McLeod)     
        - #end of provided section: signals end of provided section
    - #changed: signals where a provided section was altered by the author
    - #temp : denotes a temporary solution or piece of code
    - #todo : denotes a place where something needs to be done
    - #note : specific testing or implementation based information for the programmer


Contents:
    -imports
    -constants
    -get f(T) function
    -main funcion
             
"""

import nqueens


INITIAL_T = 100 #the initial value for T should be 100. this value was #provided by Sterling McLeod
WAIT_TIME = 100
#todo: what is a linear scheduling function?

'''
get f(T) function:
    calculates f(T) based on the function f(T) = T * decay_rate
       
    Parameters:
        - T: the current temperature
        - decay_rate: the current decay rate
        
    Return: the value of f(T) given the current decay rate
       
'''
def get_ft(T, decay_rate):
    return (T * decay_rate)

'''
main() function
    cycles through testing for 3 dimensions:
        -grid size (uses test values provided by Sterling McLeod)
        -threshold and decay rate pairs (uses test values provided by Sterling McLeod)
        -iterations (10)
            -just ten repetitions with randomly set-up boards
    prints out the results of the testing to the console

'''
#todo: maybe get it to print output to a file so you can see it better?

def main():
    T = INITIAL_T # temperature variable is set to it's initial value
    decay_rate = [.9, .75, .5] #test values for decay rate. values #provided by Sterling McLeod
    threshold = [0.000001, 0.0000001, 0.00000001] #test values for threshold T must reach to terminate the loop. values #provided by Sterling McLeod
    board_size = [4, 8, 16] # testor board sizes #provided by instructor
    time = 0 #todo: do we actualy need this variable?
    board = None
    waittime = 0
    sum_fin_h_vals = 0 #will hold the sum of all final h values
    num_iterations = 10 #the number of times each threshold-decay-rate pairing is tested
    suc_states = None
    h_vals = [] #temp testor variable holder
    fin_board = None
    
    
    
    for x in range(len(board_size)):
        print("_" * 51, "\n\nFor board size ", board_size[x], "\n_", "_" * 50, "\n")
        for y in range(len(threshold)):
            testVals = [threshold[y], decay_rate[y]] #stores this iteration's testing values
            print("_" * 21, "\n\nThreshold: ", testVals[0], "\nDecay Rate: ", testVals[1], "\n_", "_" * 20, "\n")
            sum_fin_h_vals = 0 #resets the sum of final h values variable
            for z in range(num_iterations):
                if z == 2:
                    print("Please keep in mind this may take a momment to execute")
                #print("i looped. ", x, ", ", y, ", " ,  z)#temp: testor #note: this loop has been proven to work the correct number of times
                print("run #: ", z)
                T = INITIAL_T # temperature variable is set to it's initial value
                time = 0 #resets time                                
                board= nqueens.Board(board_size[x])
                board.rand()
                board.h = nqueens.numAttackingQueens(board)
                print("intitial state: ", "\t\t\t\t\t\t\t\tintial h-value: ", board.h)
                print(board.printBoard())
                #print("h-val after printboard ", board.h)#temp testor
                    
                while(T >= testVals[0] and board.h !=0):                    
                    suc_states = nqueens.getSuccessorStates(board)
                    #print("suc states", suc_states)#temp testor
                    for i in suc_states:
                        temp_h = nqueens.numAttackingQueens(i)                        
                        if (temp_h < board.h):
                            board.h = temp_h
                            fin_board = i
                 
                   #     h_vals.append(board.h)#temp testing mechanism
                   # print("h-val during suc_states loop ", h_vals)#temp testor
                   # print("h after the sucstates loop", board.h)
                   
                   
                    T = get_ft(T, testVals[1]) #decrements T
                    time += 1 #increments time
                    
                    
                   # print("\t\t T = ", T, "at time ", time, "h val is ",  board.h)#temp testor
                    # while(input("************************************please Press enter to continue***************************************************") != "" ):
                    #     waittime += 1
                
                sum_fin_h_vals += board.h   
                print("final state: ", "\t\t\t\t\t\t\t\tfinal h-value: ", board.h)
                print(fin_board.printBoard())
                while(input("**************************please Press enter to continue****************************") != "" ):
                        waittime += 1 #just a placeholder so the syntax will work
            avg_time = (sum_fin_h_vals / num_iterations)
            print("_" * 21, "\n\nAverage h-value for decay rate", testVals[1], " and threshold ", testVals[0], " is : ", avg_time, "\n_", "_" * 20, "\n\n", "*" * 20)#todo: make this display the threshold and decay rate info too            
            while(input("**********************please Press enter to continue*****************************") != "" ):
                waittime += 1 #just a placeholder so the syntax will work
                
    print("done")#temp testor
    
main() #included for easier testing