# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work none it was
# obtained from any source other than material presented as part of the
# course.
import turtle
import random
import time

def main():
    density = float(input('Enter density of forest (0.1 - 1.0):'))
    pine = float(input('Enter percentage of pine tree (0.0 - 1.0):'))
    wetness = int(input('Enter wetness of forest (1 - 100):'))
    a=Forest(density,pine,wetness)
    a.rangen()

#Forest
class Forest:
    def __init__(self,density,pine,wetness):
        self.density=density
        self.pine=pine
        self.wetness=wetness
        turtle.speed(0)
        self.burnIter = 0
        turtle.setworldcoordinates(0,0,210,210)

    def rangen(self):
        scr=turtle.Screen()
        scr.tracer(0,0)
        i=1
        k=[]
        while i<=40:
            j=1
            while j<=40:
                denran=random.uniform(0,1)
                typeran=random.uniform(0,1)
                if denran<self.density:
                    if typeran<self.pine:
                        k.append(['Pine','notBurning',self.wetness,i,j])
                        j+=1
                    else:
                        k.append(['Oak','notBurning',self.wetness,i,j])
                        j+=1
                else:
                    k.append(['None','None',self.wetness,i,j])
                    j+=1
            i+=1
        for l in range(0,len(k)):
            if k[l][0] == 'Pine':
                b=Pine(0.95,False,self.wetness,k[l][3]*5,k[l][4]*5)
                b.draw()
            elif k[l][0] == 'Oak':
                c=Oak(0.45,False,self.wetness,k[l][3]*5,k[l][4]*5)
                c.draw()
            else:
                x=1
        
        turtle.ontimer(turtle.update(), 2000)
        while self.burnIter < 20:
            turtle.ontimer(self.redraw(k),2000)
        

    def redraw(self,k):
        turtle.clearscreen()
        scr=turtle.Screen()
        scr.tracer(0,0)
        turtle.speed(0)
        turtle.setworldcoordinates(0,0,210,210)
        print(len(k))
        for n in range(0,len(k)):
            if k[n][1]=='Burning':
                if n+1<1600 and n%40!=0:
                    if k[n+1][1]=='notBurning':
                        k[n+1][1]='Burning'
                if n-1>=0 and n%40!=1:
                    if k[n-1][1]=='notBurning':
                        k[n-1][1]='Burning'
                if n+40<1600:
                    if k[n+40][1]=='notBurning':
                        k[n+40][1]='Burning'
                if n-40>=0:
                    if k[n-40][1]=='notBurning':
                        k[n-40][1]='Burning'
                k[n][1]='None'

        for m in range(0,len(k)):
            if k[m][0] == 'Pine':
                if (random.random()<(0.95/k[m][2]) and k[m][1] != "None") or k[m][1] == 'Burning':
                    k[m][1]='Burning'
                    b=Pine(0.95,True,self.wetness,k[m][3]*5,k[m][4]*5)
                    b.draw()
                elif k[m][1]=='notBurning':
                    b=Pine(0.95,False,self.wetness,k[m][3]*5,k[m][4]*5)
                    b.draw()
                else:
                    x=1

            elif k[m][0] == 'Oak':
                if (random.random()<(0.45/k[m][2]) and k[m][1] != "None") or k[m][1] == 'Burning':
                    k[m][1]='Burning'
                    c=Oak(0.45,True,self.wetness,k[m][3]*5,k[m][4]*5)
                    c.draw()
                elif k[m][1]=='notBurning':
                    c=Oak(0.45,False,self.wetness,k[m][3]*5,k[m][4]*5)
                    c.draw()
                else:
                    x=1

        self.burnIter +=1
        turtle.update()
            

#Tree
class Tree:
    def __init__(self,probCatch=0,burning=False,wetness=1.0, xpos=0, ypos=0):
        self.probCatch=probCatch
        self.burning=burning
        self.wetness=wetness
        self.xpos=xpos
        self.ypos=ypos

class Oak(Tree):
    def __init__(self,probCatch=0.95,burning=False,wetness=1.0, xpos=0, ypos=0):
        self.probCatch=probCatch
        self.burning=burning
        self.wetness=wetness
        self.xpos=xpos
        self.ypos=ypos

    def draw(self):
        myt=turtle.Turtle()
        myt.hideturtle()
        if self.burning==True:
            myt.fillcolor('red')
        else:
            myt.fillcolor('green')
        myt.penup()
        myt.goto(self.xpos+1.5,self.ypos)
        myt.pendown()
        myt.begin_fill()
        myt.circle(1.5)
        myt.end_fill()

class Pine(Tree):
    def __init__(self,probCatch=0.45,burning=False,wetness=1.0, xpos=0, ypos=0):
        self.probCatch=probCatch
        self.burning=burning
        self.wetness=wetness
        self.xpos=xpos
        self.ypos=ypos

    def draw(self):
        myt=turtle.Turtle()
        myt.hideturtle()
        if self.burning==True:
            myt.fillcolor('red')
        else:
            myt.fillcolor('green')
        myt.penup()
        myt.goto(self.xpos,self.ypos)
        myt.pendown()
        myt.begin_fill()
        myt.forward(3)
        myt.left(120)
        myt.forward(3)
        myt.left(120)
        myt.forward(3)
        myt.left(120)
        myt.end_fill()
