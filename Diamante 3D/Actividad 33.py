#Actividad 33
#Martha Elizabeth Inda Olvera 17400997
#C16

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

class Objeto:
    def __init__(self):
        self.vertices_aro = np.array(np.genfromtxt('diamante.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajo = np.array(np.genfromtxt('diamantebase.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajo11 = np.array(np.genfromtxt('diamantebase11.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajo1 = np.array(np.genfromtxt('diamantebase1.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajo2 = np.array(np.genfromtxt('diamantebase2.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajo3 = np.array(np.genfromtxt('diamantebase3.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajo33 = np.array(np.genfromtxt('diamantebase33.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajoinferior=np.array(np.genfromtxt('diamanteinferior.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajoinferior11=np.array(np.genfromtxt('diamanteinferior11.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajoinferior2=np.array(np.genfromtxt('diamanteinferior2.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajoinferior22=np.array(np.genfromtxt('diamanteinferior22.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajoinferior3=np.array(np.genfromtxt('diamanteinferior3.csv',delimiter=','),dtype=np.float32)
        self.vertices_arobajoinferior33=np.array(np.genfromtxt('diamanteinferior33.csv',delimiter=','),dtype=np.float32)
        
    def dibuja(self):
        glColor(.5,.3,.4)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_aro:
            glVertex3fv(v)
        glEnd()
        glColor(.5,.1,.3)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajo:
          glVertex3fv(v)
        glEnd()
        glColor(.234,.13,.25)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajo11:
          glVertex3fv(v)
        glEnd()
        glColor(.234,.13,.25)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajo1:
          glVertex3fv(v)
        glEnd()
        glColor(.5,.1,.3)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajo2:
          glVertex3fv(v)
        glEnd()
        glColor(.5,.1,.3)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajo3:
          glVertex3fv(v)
        glEnd()
        glColor(.234,.13,.25)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajo33:
          glVertex3fv(v)
        glEnd()
        glColor(.234,.13,.25)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajoinferior:
            glVertex3fv(v)
        glEnd()
        glColor(.234,.13,.25)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajoinferior11:
            glVertex3fv(v)
        glEnd()
        glColor(.5,.1,.3)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajoinferior2:
            glVertex3fv(v)
        glEnd()
        glColor(.5,.1,.3)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajoinferior22:
            glVertex3fv(v)
        glEnd()
        glColor(.5,.3,.4)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajoinferior3:
            glVertex3fv(v)
        glEnd()
        glColor(.5,.3,.4)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_arobajoinferior33:
            glVertex3fv(v)
        glEnd()
      
    def trasladar(self,tx,ty,tz):
        M = np.matrix([[1,0,0,tx],
                       [0,1,0,ty],
                       [0,0,1,tz],
                       [0,0,0,1]],dtype=np.float32)
        for i in range(len(self.vertices_aro)):
            P = np.matrix([[self.vertices_aro[i][0]],
                           [self.vertices_aro[i][1]],
                        [self.vertices_aro[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_aro[i][0] = MP[0]
            self.vertices_aro[i][1] = MP[1]
            self.vertices_aro[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo)):
             P = np.matrix([[self.vertices_arobajo[i][0]],
            [self.vertices_arobajo[i][1]],
            [self.vertices_arobajo[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo[i][0] = MP[0]
             self.vertices_arobajo[i][1] = MP[1]
             self.vertices_arobajo[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo11)):
             P = np.matrix([[self.vertices_arobajo11[i][0]],
            [self.vertices_arobajo11[i][1]],
            [self.vertices_arobajo11[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo11[i][0] = MP[0]
             self.vertices_arobajo11[i][1] = MP[1]
             self.vertices_arobajo11[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo1)):
             P = np.matrix([[self.vertices_arobajo1[i][0]],
            [self.vertices_arobajo1[i][1]],
            [self.vertices_arobajo1[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo1[i][0] = MP[0]
             self.vertices_arobajo1[i][1] = MP[1]
             self.vertices_arobajo1[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo2)):
             P = np.matrix([[self.vertices_arobajo2[i][0]],
            [self.vertices_arobajo2[i][1]],
            [self.vertices_arobajo2[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo2[i][0] = MP[0]
             self.vertices_arobajo2[i][1] = MP[1]
             self.vertices_arobajo2[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo3)):
             P = np.matrix([[self.vertices_arobajo3[i][0]],
            [self.vertices_arobajo3[i][1]],
            [self.vertices_arobajo3[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo3[i][0] = MP[0]
             self.vertices_arobajo3[i][1] = MP[1]
             self.vertices_arobajo3[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo33)):
             P = np.matrix([[self.vertices_arobajo33[i][0]],
            [self.vertices_arobajo33[i][1]],
            [self.vertices_arobajo33[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo33[i][0] = MP[0]
             self.vertices_arobajo33[i][1] = MP[1]
             self.vertices_arobajo33[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior)):
             P = np.matrix([[self.vertices_arobajoinferior[i][0]],
                           [self.vertices_arobajoinferior[i][1]],
                        [self.vertices_arobajoinferior[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajoinferior[i][0] = MP[0]
             self.vertices_arobajoinferior[i][1] = MP[1]
             self.vertices_arobajoinferior[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior11)):
            P = np.matrix([[self.vertices_arobajoinferior11[i][0]],
                           [self.vertices_arobajoinferior11[i][1]],
                        [self.vertices_arobajoinferior11[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior11[i][0] = MP[0]
            self.vertices_arobajoinferior11[i][1] = MP[1]
            self.vertices_arobajoinferior11[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior2)):
            P = np.matrix([[self.vertices_arobajoinferior2[i][0]],
                           [self.vertices_arobajoinferior2[i][1]],
                        [self.vertices_arobajoinferior2[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior2[i][0] = MP[0]
            self.vertices_arobajoinferior2[i][1] = MP[1]
            self.vertices_arobajoinferior2[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior22)):
            P = np.matrix([[self.vertices_arobajoinferior22[i][0]],
                           [self.vertices_arobajoinferior22[i][1]],
                        [self.vertices_arobajoinferior22[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior22[i][0] = MP[0]
            self.vertices_arobajoinferior22[i][1] = MP[1]
            self.vertices_arobajoinferior22[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior3)):
            P = np.matrix([[self.vertices_arobajoinferior3[i][0]],
                           [self.vertices_arobajoinferior3[i][1]],
                        [self.vertices_arobajoinferior3[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior3[i][0] = MP[0]
            self.vertices_arobajoinferior3[i][1] = MP[1]
            self.vertices_arobajoinferior3[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior33)):
            P = np.matrix([[self.vertices_arobajoinferior33[i][0]],
                           [self.vertices_arobajoinferior33[i][1]],
                        [self.vertices_arobajoinferior33[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior33[i][0] = MP[0]
            self.vertices_arobajoinferior33[i][1] = MP[1]
            self.vertices_arobajoinferior33[i][2] = MP[2]
    def escalar(self,sx,sy,sz,xf=0,yf=0,zf=0):
        M = np.matrix([[sx,0,0,((sx+xf)-xf)],
                       [0,sx,0,((sy+yf)-yf)],
                        [0,0,sz,((sz+zf)-zf)],
                       [0,0,0,1]],dtype=np.float32)
        for i in range(len(self.vertices_aro)):
            P = np.matrix([[self.vertices_aro[i][0]],
                           [self.vertices_aro[i][1]],
                        [self.vertices_aro[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_aro[i][0] = MP[0]
            self.vertices_aro[i][1] = MP[1]
            self.vertices_aro[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo)):
             P = np.matrix([[self.vertices_arobajo[i][0]],
            [self.vertices_arobajo[i][1]],
            [self.vertices_arobajo[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo[i][0] = MP[0]
             self.vertices_arobajo[i][1] = MP[1]
             self.vertices_arobajo[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo11)):
             P = np.matrix([[self.vertices_arobajo11[i][0]],
            [self.vertices_arobajo11[i][1]],
            [self.vertices_arobajo11[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo11[i][0] = MP[0]
             self.vertices_arobajo11[i][1] = MP[1]
             self.vertices_arobajo11[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo1)):
             P = np.matrix([[self.vertices_arobajo1[i][0]],
            [self.vertices_arobajo1[i][1]],
            [self.vertices_arobajo1[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo1[i][0] = MP[0]
             self.vertices_arobajo1[i][1] = MP[1]
             self.vertices_arobajo1[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo2)):
             P = np.matrix([[self.vertices_arobajo2[i][0]],
            [self.vertices_arobajo2[i][1]],
            [self.vertices_arobajo2[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo2[i][0] = MP[0]
             self.vertices_arobajo2[i][1] = MP[1]
             self.vertices_arobajo2[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo3)):
             P = np.matrix([[self.vertices_arobajo3[i][0]],
            [self.vertices_arobajo3[i][1]],
            [self.vertices_arobajo3[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo3[i][0] = MP[0]
             self.vertices_arobajo3[i][1] = MP[1]
             self.vertices_arobajo3[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo33)):
             P = np.matrix([[self.vertices_arobajo33[i][0]],
            [self.vertices_arobajo33[i][1]],
            [self.vertices_arobajo33[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo33[i][0] = MP[0]
             self.vertices_arobajo33[i][1] = MP[1]
             self.vertices_arobajo33[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior)):
             P = np.matrix([[self.vertices_arobajoinferior[i][0]],
                           [self.vertices_arobajoinferior[i][1]],
                        [self.vertices_arobajoinferior[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajoinferior[i][0] = MP[0]
             self.vertices_arobajoinferior[i][1] = MP[1]
             self.vertices_arobajoinferior[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior11)):
            P = np.matrix([[self.vertices_arobajoinferior11[i][0]],
                           [self.vertices_arobajoinferior11[i][1]],
                        [self.vertices_arobajoinferior11[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior11[i][0] = MP[0]
            self.vertices_arobajoinferior11[i][1] = MP[1]
            self.vertices_arobajoinferior11[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior2)):
            P = np.matrix([[self.vertices_arobajoinferior2[i][0]],
                           [self.vertices_arobajoinferior2[i][1]],
                        [self.vertices_arobajoinferior2[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior2[i][0] = MP[0]
            self.vertices_arobajoinferior2[i][1] = MP[1]
            self.vertices_arobajoinferior2[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior22)):
            P = np.matrix([[self.vertices_arobajoinferior22[i][0]],
                           [self.vertices_arobajoinferior22[i][1]],
                        [self.vertices_arobajoinferior22[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior22[i][0] = MP[0]
            self.vertices_arobajoinferior22[i][1] = MP[1]
            self.vertices_arobajoinferior22[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior3)):
            P = np.matrix([[self.vertices_arobajoinferior3[i][0]],
                           [self.vertices_arobajoinferior3[i][1]],
                        [self.vertices_arobajoinferior3[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior3[i][0] = MP[0]
            self.vertices_arobajoinferior3[i][1] = MP[1]
            self.vertices_arobajoinferior3[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior33)):
            P = np.matrix([[self.vertices_arobajoinferior33[i][0]],
                           [self.vertices_arobajoinferior33[i][1]],
                        [self.vertices_arobajoinferior33[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior33[i][0] = MP[0]
            self.vertices_arobajoinferior33[i][1] = MP[1]
            self.vertices_arobajoinferior33[i][2] = MP[2]
    def rotar_z(self,O,xr=0,yr=0,zr=0):
        O = np.radians(O)
        M = np.matrix([[np.cos(O),-np.sin(O),0,(xr*np.cos(O)-xr-np.sin(O)*yr)],
                       [np.sin(O),np.cos(O),0,(xr*np.sin(O)+(np.cos(O)*yr)-yr)],
                       [0,0,1,0],[0,0,0,1]],dtype=np.float32)
        for i in range(len(self.vertices_aro)):
            P = np.matrix([[self.vertices_aro[i][0]],
                           [self.vertices_aro[i][1]],
                        [self.vertices_aro[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_aro[i][0] = MP[0]
            self.vertices_aro[i][1] = MP[1]
            self.vertices_aro[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo)):
             P = np.matrix([[self.vertices_arobajo[i][0]],
            [self.vertices_arobajo[i][1]],
            [self.vertices_arobajo[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo[i][0] = MP[0]
             self.vertices_arobajo[i][1] = MP[1]
             self.vertices_arobajo[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo11)):
             P = np.matrix([[self.vertices_arobajo11[i][0]],
            [self.vertices_arobajo11[i][1]],
            [self.vertices_arobajo11[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo11[i][0] = MP[0]
             self.vertices_arobajo11[i][1] = MP[1]
             self.vertices_arobajo11[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo1)):
             P = np.matrix([[self.vertices_arobajo1[i][0]],
            [self.vertices_arobajo1[i][1]],
            [self.vertices_arobajo1[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo1[i][0] = MP[0]
             self.vertices_arobajo1[i][1] = MP[1]
             self.vertices_arobajo1[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo2)):
             P = np.matrix([[self.vertices_arobajo2[i][0]],
            [self.vertices_arobajo2[i][1]],
            [self.vertices_arobajo2[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo2[i][0] = MP[0]
             self.vertices_arobajo2[i][1] = MP[1]
             self.vertices_arobajo2[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo3)):
             P = np.matrix([[self.vertices_arobajo3[i][0]],
            [self.vertices_arobajo3[i][1]],
            [self.vertices_arobajo3[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo3[i][0] = MP[0]
             self.vertices_arobajo3[i][1] = MP[1]
             self.vertices_arobajo3[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo33)):
             P = np.matrix([[self.vertices_arobajo33[i][0]],
            [self.vertices_arobajo33[i][1]],
            [self.vertices_arobajo33[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo33[i][0] = MP[0]
             self.vertices_arobajo33[i][1] = MP[1]
             self.vertices_arobajo33[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior)):
             P = np.matrix([[self.vertices_arobajoinferior[i][0]],
                           [self.vertices_arobajoinferior[i][1]],
                        [self.vertices_arobajoinferior[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajoinferior[i][0] = MP[0]
             self.vertices_arobajoinferior[i][1] = MP[1]
             self.vertices_arobajoinferior[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior11)):
            P = np.matrix([[self.vertices_arobajoinferior11[i][0]],
                           [self.vertices_arobajoinferior11[i][1]],
                        [self.vertices_arobajoinferior11[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior11[i][0] = MP[0]
            self.vertices_arobajoinferior11[i][1] = MP[1]
            self.vertices_arobajoinferior11[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior2)):
            P = np.matrix([[self.vertices_arobajoinferior2[i][0]],
                           [self.vertices_arobajoinferior2[i][1]],
                        [self.vertices_arobajoinferior2[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior2[i][0] = MP[0]
            self.vertices_arobajoinferior2[i][1] = MP[1]
            self.vertices_arobajoinferior2[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior22)):
            P = np.matrix([[self.vertices_arobajoinferior22[i][0]],
                           [self.vertices_arobajoinferior22[i][1]],
                        [self.vertices_arobajoinferior22[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior22[i][0] = MP[0]
            self.vertices_arobajoinferior22[i][1] = MP[1]
            self.vertices_arobajoinferior22[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior3)):
            P = np.matrix([[self.vertices_arobajoinferior3[i][0]],
                           [self.vertices_arobajoinferior3[i][1]],
                        [self.vertices_arobajoinferior3[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior3[i][0] = MP[0]
            self.vertices_arobajoinferior3[i][1] = MP[1]
            self.vertices_arobajoinferior3[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior33)):
            P = np.matrix([[self.vertices_arobajoinferior33[i][0]],
                           [self.vertices_arobajoinferior33[i][1]],
                        [self.vertices_arobajoinferior33[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior33[i][0] = MP[0]
            self.vertices_arobajoinferior33[i][1] = MP[1]
            self.vertices_arobajoinferior33[i][2] = MP[2]
    def rotar_x(self,O,xr=0,yr=0,zr=0):
        O = np.radians(O)
        M = np.matrix([[1,0,0,0],
                       [0,np.cos(O),-np.sin(O),(-yr*np.cos(O)+zr*np.sin(O)+yr)],
                       [0,np.sin(O),np.cos(O),(-yr*np.sin(O)-zr*np.cos(O)+zr)],
                       [0,0,0,1]],dtype=np.float32)
        for i in range(len(self.vertices_aro)):
            P = np.matrix([[self.vertices_aro[i][0]],
                           [self.vertices_aro[i][1]],
                        [self.vertices_aro[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_aro[i][0] = MP[0]
            self.vertices_aro[i][1] = MP[1]
            self.vertices_aro[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo)):
             P = np.matrix([[self.vertices_arobajo[i][0]],
            [self.vertices_arobajo[i][1]],
            [self.vertices_arobajo[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo[i][0] = MP[0]
             self.vertices_arobajo[i][1] = MP[1]
             self.vertices_arobajo[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo11)):
             P = np.matrix([[self.vertices_arobajo11[i][0]],
            [self.vertices_arobajo11[i][1]],
            [self.vertices_arobajo11[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo11[i][0] = MP[0]
             self.vertices_arobajo11[i][1] = MP[1]
             self.vertices_arobajo11[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo1)):
             P = np.matrix([[self.vertices_arobajo1[i][0]],
            [self.vertices_arobajo1[i][1]],
            [self.vertices_arobajo1[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo1[i][0] = MP[0]
             self.vertices_arobajo1[i][1] = MP[1]
             self.vertices_arobajo1[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo2)):
             P = np.matrix([[self.vertices_arobajo2[i][0]],
            [self.vertices_arobajo2[i][1]],
            [self.vertices_arobajo2[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo2[i][0] = MP[0]
             self.vertices_arobajo2[i][1] = MP[1]
             self.vertices_arobajo2[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo3)):
             P = np.matrix([[self.vertices_arobajo3[i][0]],
            [self.vertices_arobajo3[i][1]],
            [self.vertices_arobajo3[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo3[i][0] = MP[0]
             self.vertices_arobajo3[i][1] = MP[1]
             self.vertices_arobajo3[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo33)):
             P = np.matrix([[self.vertices_arobajo33[i][0]],
            [self.vertices_arobajo33[i][1]],
            [self.vertices_arobajo33[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo33[i][0] = MP[0]
             self.vertices_arobajo33[i][1] = MP[1]
             self.vertices_arobajo33[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior)):
             P = np.matrix([[self.vertices_arobajoinferior[i][0]],
                           [self.vertices_arobajoinferior[i][1]],
                        [self.vertices_arobajoinferior[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajoinferior[i][0] = MP[0]
             self.vertices_arobajoinferior[i][1] = MP[1]
             self.vertices_arobajoinferior[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior11)):
            P = np.matrix([[self.vertices_arobajoinferior11[i][0]],
                           [self.vertices_arobajoinferior11[i][1]],
                        [self.vertices_arobajoinferior11[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior11[i][0] = MP[0]
            self.vertices_arobajoinferior11[i][1] = MP[1]
            self.vertices_arobajoinferior11[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior2)):
            P = np.matrix([[self.vertices_arobajoinferior2[i][0]],
                           [self.vertices_arobajoinferior2[i][1]],
                        [self.vertices_arobajoinferior2[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior2[i][0] = MP[0]
            self.vertices_arobajoinferior2[i][1] = MP[1]
            self.vertices_arobajoinferior2[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior22)):
            P = np.matrix([[self.vertices_arobajoinferior22[i][0]],
                           [self.vertices_arobajoinferior22[i][1]],
                        [self.vertices_arobajoinferior22[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior22[i][0] = MP[0]
            self.vertices_arobajoinferior22[i][1] = MP[1]
            self.vertices_arobajoinferior22[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior3)):
            P = np.matrix([[self.vertices_arobajoinferior3[i][0]],
                           [self.vertices_arobajoinferior3[i][1]],
                        [self.vertices_arobajoinferior3[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior3[i][0] = MP[0]
            self.vertices_arobajoinferior3[i][1] = MP[1]
            self.vertices_arobajoinferior3[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior33)):
            P = np.matrix([[self.vertices_arobajoinferior33[i][0]],
                           [self.vertices_arobajoinferior33[i][1]],
                        [self.vertices_arobajoinferior33[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior33[i][0] = MP[0]
            self.vertices_arobajoinferior33[i][1] = MP[1]
            self.vertices_arobajoinferior33[i][2] = MP[2]
    def rotar_y(self,O,xr=0,yr=0,zr=0):
        O = np.radians(O)
        M = np.matrix([[np.cos(O),0,np.sin(O),(-xr*np.cos(O)-zr*np.sin(O)+xr)],
                       [0,1,0,0],[-np.sin(O),0,np.cos(O),(xr*np.sin(O)-zr*np.cos(O)+zr)],
                       [0,0,0,1]],dtype=np.float32)
        for i in range(len(self.vertices_aro)):
            P = np.matrix([[self.vertices_aro[i][0]],
                           [self.vertices_aro[i][1]],
                        [self.vertices_aro[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_aro[i][0] = MP[0]
            self.vertices_aro[i][1] = MP[1]
            self.vertices_aro[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo)):
             P = np.matrix([[self.vertices_arobajo[i][0]],
            [self.vertices_arobajo[i][1]],
            [self.vertices_arobajo[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo[i][0] = MP[0]
             self.vertices_arobajo[i][1] = MP[1]
             self.vertices_arobajo[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo11)):
             P = np.matrix([[self.vertices_arobajo11[i][0]],
            [self.vertices_arobajo11[i][1]],
            [self.vertices_arobajo11[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo11[i][0] = MP[0]
             self.vertices_arobajo11[i][1] = MP[1]
             self.vertices_arobajo11[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo1)):
             P = np.matrix([[self.vertices_arobajo1[i][0]],
            [self.vertices_arobajo1[i][1]],
            [self.vertices_arobajo1[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo1[i][0] = MP[0]
             self.vertices_arobajo1[i][1] = MP[1]
             self.vertices_arobajo1[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo2)):
             P = np.matrix([[self.vertices_arobajo2[i][0]],
            [self.vertices_arobajo2[i][1]],
            [self.vertices_arobajo2[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo2[i][0] = MP[0]
             self.vertices_arobajo2[i][1] = MP[1]
             self.vertices_arobajo2[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo3)):
             P = np.matrix([[self.vertices_arobajo3[i][0]],
            [self.vertices_arobajo3[i][1]],
            [self.vertices_arobajo3[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo3[i][0] = MP[0]
             self.vertices_arobajo3[i][1] = MP[1]
             self.vertices_arobajo3[i][2] = MP[2]
        for i in range(len(self.vertices_arobajo33)):
             P = np.matrix([[self.vertices_arobajo33[i][0]],
            [self.vertices_arobajo33[i][1]],
            [self.vertices_arobajo33[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajo33[i][0] = MP[0]
             self.vertices_arobajo33[i][1] = MP[1]
             self.vertices_arobajo33[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior)):
             P = np.matrix([[self.vertices_arobajoinferior[i][0]],
                           [self.vertices_arobajoinferior[i][1]],
                        [self.vertices_arobajoinferior[i][2]],[1]],dtype=np.float32)
             MP = M * P
             self.vertices_arobajoinferior[i][0] = MP[0]
             self.vertices_arobajoinferior[i][1] = MP[1]
             self.vertices_arobajoinferior[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior11)):
            P = np.matrix([[self.vertices_arobajoinferior11[i][0]],
                           [self.vertices_arobajoinferior11[i][1]],
                        [self.vertices_arobajoinferior11[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior11[i][0] = MP[0]
            self.vertices_arobajoinferior11[i][1] = MP[1]
            self.vertices_arobajoinferior11[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior2)):
            P = np.matrix([[self.vertices_arobajoinferior2[i][0]],
                           [self.vertices_arobajoinferior2[i][1]],
                        [self.vertices_arobajoinferior2[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior2[i][0] = MP[0]
            self.vertices_arobajoinferior2[i][1] = MP[1]
            self.vertices_arobajoinferior2[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior22)):
            P = np.matrix([[self.vertices_arobajoinferior22[i][0]],
                           [self.vertices_arobajoinferior22[i][1]],
                        [self.vertices_arobajoinferior22[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior22[i][0] = MP[0]
            self.vertices_arobajoinferior22[i][1] = MP[1]
            self.vertices_arobajoinferior22[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior3)):
            P = np.matrix([[self.vertices_arobajoinferior3[i][0]],
                           [self.vertices_arobajoinferior3[i][1]],
                        [self.vertices_arobajoinferior3[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior3[i][0] = MP[0]
            self.vertices_arobajoinferior3[i][1] = MP[1]
            self.vertices_arobajoinferior3[i][2] = MP[2]
        for i in range(len(self.vertices_arobajoinferior33)):
            P = np.matrix([[self.vertices_arobajoinferior33[i][0]],
                           [self.vertices_arobajoinferior33[i][1]],
                        [self.vertices_arobajoinferior33[i][2]],[1]],dtype=np.float32)
            MP = M * P
            self.vertices_arobajoinferior33[i][0] = MP[0]
            self.vertices_arobajoinferior33[i][1] = MP[1]
            self.vertices_arobajoinferior33[i][2] = MP[2]
def dibuja_ejes():
    glColor(1,0,0)
    glBegin(GL_LINES)
    glVertex3i(-20,0,0)
    glVertex3i(20,0,0)
    glEnd()
    glColor(0,1,0)
    glBegin(GL_LINES)
    glVertex3i(0,-20,0)
    glVertex3i(0,20,0)
    glEnd()
    glColor(0,0,1)
    glBegin(GL_LINES)
    glVertex3i(0,0,20)
    glVertex3i(0,0,-20)
    glEnd()
   
def main():
    if not glfw.init():
        return

    window = glfw.create_window(500,500,"...",None,None)
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    glClearColor(1,1,1,0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-12,12,-12,12,1,50)
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
    gluLookAt(5,5,8,0,0,0,0,1,0) 
    
    obj = Objeto()
    #----- Métodos para cambiar posición ------
    obj.trasladar(2,2,0)
    obj.escalar(1,1,1)
    obj.rotar_z(100)
    obj.rotar_x(240) 
    obj.rotar_y(300) 
    x,z = 5,8
    r = np.sqrt(x**2+z**2)
    t = np.arctan(z/x)
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST) 
        #glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)#GL_LINE alambrico GL_FILL superficie

        dibuja_ejes()
        obj.dibuja()
        time.sleep(0.1)
        
        glMatrixMode(GL_MODELVIEW) 
        glLoadIdentity()
        gluLookAt(r*np.cos(t),5,r*np.sin(t),0,0,0,0,1,0)
        t += 0.1
        
        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()
