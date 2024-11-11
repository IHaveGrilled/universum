########################################################################## LIBS

import viz
import vizshape
import vizcam
import vizact
import random

########################################################################## INIT

# vizard vides veidoshana
viz.setMultiSample(4)
viz.fov(60)  # Field of view
viz.go(viz.FULLSCREEN)
#viz.go()

# Piekļūst galvenajai gaismai un iestata tās intensitāti
head_light = viz.MainView.getHeadLight()
head_light.intensity(0.5)

# Pievieno virziena gaismu
dir_light = viz.addDirectionalLight()
dir_light.direction(0, -1, 0)
dir_light.intensity(0.8)

viz.clearcolor(viz.BLACK) # debesis

vizcam.PivotNavigate(center=[0,0,0], distance=20, sensitivity=[1.0,1.0]) # pivot kamera kas rotee ap centralo punktu

########################################################################## OBJEKTU IZVEIDE

# katrai planetai savs scale
mercury_scale = 0.38
venus_scale = 1.00  
earth_scale = 1.00  
mars_scale = 0.53
jupiter_scale = 11.21
saturn_scale = 9.45
uranus_scale = 4.01
neptune_scale = 3.88

mercury = viz.add('mercury.osgb')
mercury.setPosition(0, 0, 0)
mercury.setScale(mercury_scale, mercury_scale, mercury_scale)

venus = viz.add('venus.osgb')
venus.setPosition(0, 0, 0)
venus.setScale(venus_scale, venus_scale, venus_scale)

earth = viz.add('earth.osgb')
earth.setPosition(0, 0, 0)
earth.setScale(earth_scale, earth_scale, earth_scale)

mars = viz.add('mars.osgb')
mars.setPosition(0, 0, 0)
mars.setScale(mars_scale, mars_scale, mars_scale)

jupiter = viz.add('jupiter.osgb')
jupiter.setPosition(0, 0, 0)
jupiter.setScale(jupiter_scale, jupiter_scale, jupiter_scale)

saturn = viz.add('saturn.osgb')
saturn.setPosition(0, 0, 0)
saturn.setScale(saturn_scale, saturn_scale, saturn_scale)

uranus = viz.add('uranus.osgb')
uranus.setPosition(0, 0, 0)
uranus.setScale(uranus_scale, uranus_scale, uranus_scale)

neptune = viz.add('neptune.osgb')
neptune.setPosition(0, 0, 0)
neptune.setScale(neptune_scale, neptune_scale, neptune_scale)

# visus objektus japadara invisible, neskaitot pirmo
#mercury.visible(viz.OFF)
venus.visible(viz.OFF)
earth.visible(viz.OFF)
mars.visible(viz.OFF)
jupiter.visible(viz.OFF)
saturn.visible(viz.OFF)
uranus.visible(viz.OFF)
neptune.visible(viz.OFF)

########################################################################## OBJEKTU MANIPULACIJA

objects = {'1': mercury, '2': venus, '3': earth, '4': mars, '5': jupiter, '6': saturn, '7': uranus, '8': neptune}

planet_texts = {
    '1': "Mercury: \nMercury is the smallest planet and the closest to the Sun, \nwith a rocky, cratered surface. \nIt has extreme temperature variations \ndue to its lack of atmosphere. \nDiameter: 4,880 km \nDistance from Sun: 57.9 million km \nDay Length: 58.6 Earth days \nTemperature Range: -173°C to 427°C \nHabitable: No",
    '2': "Venus: \nVenus is similar in size to Earth, with a thick atmosphere \nthat traps heat, creating extremely \nhigh surface temperatures. Its clouds \nare rich in sulfuric acid, \ngiving it a reflective, \nhazy appearance. \nDiameter: 12,104 km \nDistance from Sun: 108.2 million km \nDay Length: 243 Earth days \nAverage Temperature: 465°C \nHabitable: No",
    '3': "Earth: \nEarth is our home planet, known for its life-supporting oceans, \necosystems, and active geology. \nIt has a balanced climate and dynamic \ngeology, including active volcanism. \nDiameter: 12,742 km \nDistance from Sun: 149.6 million km \nDay Length: 24 hours \nAverage Temperature: 15°C \nHabitable: Yes",
    '4': "Mars: \nMars, known as the Red Planet, has a dusty terrain \nwith the largest volcano and canyon \nin the solar system. \nIt has polar ice caps and \nis a prime candidate for future exploration. \nDiameter: 6,779 km \nDistance from Sun: 227.9 million km \nDay Length: 24.6 hours \nTemperature Range: -125°C to 20°C \nHabitable: Possibly",
    '5': "Jupiter: \nJupiter is the largest planet in the solar system, \nprimarily composed of hydrogen and \nhelium, with a dense core. \nIts famous Great Red Spot \nis a massive storm larger than Earth. \nDiameter: 139,820 km \nDistance from Sun: 778.5 million km \nDay Length: 9.9 hours \nAverage Temperature: -108°C \nHabitable: No",
    '6': "Saturn: \nSaturn is known for its stunning ring system, \nmade primarily of ice particles and rock debris. \nIts atmosphere contains hydrogen, helium, \nand traces of methane. \nDiameter: 116,460 km \nDistance from Sun: 1.43 billion km \nDay Length: 10.7 hours \nAverage Temperature: -138°C \nHabitable: No",
    '7': "Uranus: \nUranus has a unique sideways rotation, causing extreme seasons \nand a striking blue-green color \ndue to methane in its atmosphere. \nIt has a ring system and many moons. \nDiameter: 50,724 km \nDistance from Sun: 2.87 billion km \nDay Length: 17.2 hours \nAverage Temperature: -195°C \nHabitable: No",
    '8': "Neptune: \nNeptune, the farthest known planet, is a cold \nblue giant with strong winds and storms, \nincluding the Great Dark Spot. \nIts atmosphere consists mainly of hydrogen, \nhelium, and methane. \nDiameter: 49,244 km \nDistance from Sun: 4.5 billion km \nDay Length: 16.1 hours \nAverage Temperature: -201°C \nHabitable: No"
}

sounds = {
    '1': viz.addAudio('mercury.mp3'),
    '2': viz.addAudio('venus.mp3'),
    '3': viz.addAudio('earth.mp3'),
    '4': viz.addAudio('mars.mp3'),
    '5': viz.addAudio('jupiter.mp3'),
    '6': viz.addAudio('saturn.mp3'),
    '7': viz.addAudio('uranus.mp3'),
    '8': viz.addAudio('neptune.mp3')
}

def play_planet_sound(key):
    # Stop any sound that's currently playing
    for sound in sounds.values():
        sound.stop()
    
    # Play the sound associated with the planet key
    if key in sounds:
        sounds[key].play()

# text
planet_text = viz.addText("", parent=viz.SCREEN)
planet_text.setPosition(0.1, 0.9)      
planet_text.fontSize(20)               
planet_text.color(viz.YELLOW)           
planet_text.font('Lucida Console')    
planet_text.setBackdrop(viz.BACKDROP_LEFT_BOTTOM)
planet_text.setBackdropColor([0.8, 0.8, 0.8])

def hide_all_objects():
    for obj in objects.values():
        obj.visible(viz.OFF)

def show_object(key):
    hide_all_objects()  # sakumaa paslepj visus objektus
    if key in objects:
        objects[key].visible(viz.ON)  # Show selected planet
        planet_text.message(planet_texts[key])  # Update text based on planet
        play_planet_sound(key)  # Play the sound for the selected planet

########################################################################## KEYBOARD KONTROLE

# katram taustinam savs objekts
vizact.onkeydown('1', lambda: show_object('1'))  # 1 mercury
vizact.onkeydown('2', lambda: show_object('2'))  # 2 venus
vizact.onkeydown('3', lambda: show_object('3'))  # 3 earth
vizact.onkeydown('4', lambda: show_object('4'))  # 4 mars
vizact.onkeydown('5', lambda: show_object('5'))  # 5 jupiter
vizact.onkeydown('6', lambda: show_object('6'))  # 6 saturn
vizact.onkeydown('7', lambda: show_object('7'))  # 7 uranus
vizact.onkeydown('8', lambda: show_object('8'))  # 8 neptuns

##########################################################################