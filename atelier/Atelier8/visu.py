import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def visuPhysicalStates(path):
    ## this function read output Physical states file
    ## then create png picture
    ## path the directory with files   
    WIDTH=500
    HEIGHT=100
    myFile = open(path, 'r')
    id_line = 1   # line ID
    id_colms = 14     # colms ID
    listX1 = []      # list x coordinnate
    listY1 = []      # list y coordinate
    listX2 = []      # list x coordinnate
    listY2 = []      # list y coordinate
    listX3 = []      # list x coordinnate
    listY3 = []      # list y coordinate
    listX4 = []      # list x coordinnate
    listY4 = []      # list y coordinate
    # read line by line
    ligne = 0
    for iLine in myFile.readlines():
        
        # split \t
        iLine = iLine.split(' ')
        # read each line elements
        for it in iLine:
            incrementation = (ligne//10) *10
            if (it == '\n'):
                pass
            # si j ai un 0 unburnt
            elif (it == 0):
                pass
            # si j ai un 1 yellow state heating
            elif (it == "Humain"):
                listX1.append(id_colms-incrementation*50)
                listY1.append(id_line+95-incrementation)
            # nothink
            # si j ai un 3 orange state cooling
            elif (it == "Tauren"):
                listX3.append(id_colms-incrementation*50)
                listY3.append(id_line+95-incrementation)
            # si j ai un 4 red state burning
            elif (it == "Obstacle"):
                listX4.append(id_colms-incrementation*50)
                listY4.append(id_line+95-incrementation)
            # if -1 black state burnt
            else:
                listX2.append(id_colms-incrementation*50)
                listY2.append(id_line+95-incrementation)    
            id_colms+=50
            ligne += 1
        id_colms=1
        id_line+=1
    myFile.close()
    # take the time in the name file
    txt = path.split('.')[0][len(path.split('.')[0])-3:len(path.split('.')[0])]
    #Refresh the plot
    plt.cla()
    plt.plot(listX1, listY1, label='humain', color='blue', linestyle='None', marker='s',markerfacecolor='blue', markeredgecolor='blue', markersize=10)
    plt.plot(listX4, listY4, label='Obstacle', color='red', linestyle='None', marker='s',markerfacecolor='red', markeredgecolor='red', markersize=10)
    plt.plot(listX3, listY3, label='Tauren', color='green', linestyle='None', marker='s',markerfacecolor='green', markeredgecolor='green', markersize=10)
    plt.plot(listX2, listY2, label='rien', color='black', linestyle='None', marker='s',markerfacecolor='black', markeredgecolor='black', markersize=10)
    plt.text(WIDTH-150, HEIGHT--5, r'time:'+str(txt))
    plt.text(WIDTH-500, HEIGHT-115, r'noir : libre')
    plt.text(WIDTH-400, HEIGHT-115, r'rouge : obstacle')
    plt.text(WIDTH-250, HEIGHT-115, r'bleu : humain')
    plt.text(WIDTH-100, HEIGHT-115, r'vert : tauren')
    plt.axis([0, WIDTH, 0, HEIGHT])
    #plt.legend()
    #plt.show()
    # create the output path
    myDir = path.split('/')[0]+'.visu.out'
    if not os.path.exists(myDir):
        os.mkdir(myDir)
    path = path.split('/')[1]
    # creat the output name file
    path = myDir+'/'+path.split('.')[0]+'.png'
    # save file
    plt.savefig(path)
    
# main('output/activity',option='activity or phisicalStates')
def main(directory):
    ## this function launch fileManag function for all files in the directory
    time = 0
    print ("Start plot")
    print ("file: "+directory)
    lstFile = os.listdir(directory)
    for i in lstFile:
        fname = directory+'/'+i
        visuPhysicalStates(fname)
        time+=1
        print ("picture "+str(time)+" create")

main("txt_java")