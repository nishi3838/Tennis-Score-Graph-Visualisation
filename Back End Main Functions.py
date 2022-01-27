import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
        
def count_games(ys):
    a_games, b_games = 0, 0
    a_score, b_score = 0, 0
    is_deuce = False
    game_ends = []
    game_scores = []
    for i in range(len(ys) - 1):
        if a_score == 3 and b_score == 3:
            is_deuce = True
    
        if ys[i + 1] > ys[i]:
            a_score += 1
            if a_score >= 4 and ((is_deuce and a_score >= b_score + 2) or not is_deuce):
                a_games += 1
                game_ends.append(i + 1)
                game_scores.append((a_games, b_games))
                a_score, b_score = 0, 0
                is_deuce = False

        else:
            b_score += 1
            if b_score >= 4 and ((is_deuce and b_score >= a_score + 2) or not is_deuce):
                b_games += 1
                game_ends.append(i + 1)
                game_scores.append((a_games, b_games))
                a_score, b_score = 0, 0
                is_deuce = False

    return game_ends, game_scores


def draw_game_lines(ys):
    game_ends, _ = count_games(ys)
    plt.vlines(x=game_ends, ymin=min(ys), ymax=max(ys), colors='black', linestyles='  bdashed', label='Vertical Line')



def draw_game_scores(ys):
    game_ends, game_scores = count_games(ys)


    for i in range(len(game_ends)):
        plt.text(game_ends[i], max(ys), '-'.join(map(str, game_scores[i])))


colourmap = np.array(['r', 'g', 'b','black'])
colourlist = [3]







def point_information_scattering():

    # set the default colour to be black
    colour_inp = input("input 0 or 1 or 2: ")
    colourlist.append(int(colour_inp))       
    ax1.scatter(range(len(ys)),ys, c=colourmap[colourlist])



textlist = ['']


        

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ys = [0] # ys stores all the y values as it the graph fluctuates


def animate(i):
    inp = input("input W or L: ")
    if inp == 'W':
        ys.append(ys[-1] + 1)
    else:
        ys.append(ys[-1] - 1)
    ax1.clear()
    ax1.plot(range(len(ys)), ys,c='black',linewidth=1)
    
    point_information_scattering()

    #ax1.scatter(range(len(ys)), ys,c='red')
    
    plt.yticks(np.arange(min(ys), max(ys)+1, 1.0))
    plt.xticks(np.arange(0, len(ys), 1.0))
    plt.hlines(0, 0, len(ys),colors='black', linestyles='dashed', label='Base')

    # draw_vertical_lines(input_y)
    draw_game_lines(ys)
    draw_game_scores(ys)


ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()



