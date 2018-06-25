'''
List all science experiment of a vessel
'''

import krpc

conn = krpc.connect()
vessel = conn.space_center.active_vessel

def makeScience(vessel, expType=None):
    '''
    Find the next experiement available for a defined type

    Parameters:
       Vessel: krpc vessel
       expType: Type of the experiment
          MK1Pod, MisteryGoo
    '''
    experimentsName = {'MK1Pod':'mk1pod', 'MisteryGoo':'GooExperiment'}

    experience = experimentsName[expType]
    
    experimentRan = False
    for part in vessel.parts.all:
        if part.experiment \
            and part.name == experience:
            if not part.experiment.deployed:
                print('Making science with {}'.format(experience))
                part.experiment.run()
                experimentRan = True
                break
    if not experimentRan:
        print('No experiment available')


experimentList = []

for part in vessel.parts.all:
    if part.experiment:
        experimentList.append(part)

for exp in experimentList:        
    print(exp.name)

makeScience(vessel, 'MK1Pod')
makeScience(vessel, 'MisteryGoo')
        
