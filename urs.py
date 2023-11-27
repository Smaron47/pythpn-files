'''from cgitb import text
from ursina import *
from random import uniform
#from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#player=FirstPersonController(y=2, origin_y=-.5)
ground=Entity(model='cube', scale=(100, 1, 100), color=color.lime, texture="brick",
	texture_scale=(100, 100), collider='box')

wall_1=Entity(model="cube", collider="box", position=(-11, 0, 0), scale=(8, 5, 1), rotation=(0,0,0),
	texture="brick", texture_scale=(5,5), color=color.rgb(255, 128, 0))
wall_2 = duplicate(wall_1, z=5)
wall_3=duplicate(wall_1, z=20)
wall_4=Entity(model="cube", collider="box", position=(-15, 0, 10), scale=(1,5,20), rotation=(0,0,0),
	texture="download.jpeg", texture_scale=(1,1))
wall_5=Entity(model="cube", collider="box", position=(-5, 0, 10), scale=(1,5,20), rotation=(0,0,0),
	texture="download.jpeg", texture_scale=(1,1))


camera.parent= player
camera.y= 5
camera.z= -10
camera.rotation_x= 9.15

def input(key):
               
    if key == "a":
       player.x-= 1
        
    if key == "d":
       player.x+= 1
        
    if key == "w":
       player.z+= 1
        
    if key == "s":
       player.z-= 1
#sk=Sky(texture="0_592.mp4")
#apic=Entity(model="cube",parent=camera.ui,texture="download.jpeg")
#apic.positon=(-20,19)
app.run()'''

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

grass_color = color.rgb(1, 235, 113)
stone_color = color.rgb(138,141,143)
dirt_color = color.rgb(200, 157, 124)

block_pick = 1

def update():
    if held_keys['escape']:
        quit()

    global block_pick

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3

class Voxel(Button):
    def __init__(self, position = (0,0,0), color = color.white):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color,
            highlight_color = color,
                    )

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1:voxel = Voxel(position = self.position + mouse.normal, color = grass_color)
                if block_pick == 2:voxel = Voxel(position = self.position + mouse.normal, color = stone_color)
                if block_pick == 3:voxel = Voxel(position = self.position + mouse.normal, color = dirt_color)
            if key == 'left mouse down':
                destroy(self)
            
for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z), color = grass_color)

for y in range(3):
    for x in range(20):
        for z in range(20):
            voxel = Voxel(position=(x,y + -3,z), color = dirt_color)

player = FirstPersonController()
app.run()