'''
Mission I: First Vessel

Launch first vessel, get science from launch pad and from altitude
and come back on Kerbin
'''

import krpc
import time

def makeScience(vessel, expType=None):
    '''
    Find the next experiement available for a defined type

    Parameters:
       Vessel: krpc vessel
       expType: Type of the experiment
          MK1Pod, MysteryGoo
    '''
    experimentsName = {'MK1Pod':'mk1pod', 'MysteryGoo':'GooExperiment'}

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


def countDown(start=20):
    print('Countdown...')
    for i in range(start, 0, -1):
        print('{}...'.format(i))
        time.sleep(1)

# Connect to KSP
conn = krpc.connect(
    name='Mission I',
    address='127.0.0.1',
    rpc_port=50000, stream_port=50001)

# Get the active vessel
vessel = conn.space_center.active_vessel

# Set the initial flight parameters
vessel.auto_pilot.target_pitch_and_heading(90, 90)
#vessel.control.throttle = 1
time.sleep(1)

# Make science
makeScience(vessel, 'MK1Pod')
makeScience(vessel, 'MysteryGoo')

# Start the count down
countDown()

# Ignit the solid fuel booster
print('Ignition!')
vessel.auto_pilot.engage()
vessel.control.activate_next_stage()

fuel_amount = conn.get_call(vessel.resources.amount, 'SolidFuel')
expr = conn.krpc.Expression.less_than(
    conn.krpc.Expression.call(fuel_amount),
    conn.krpc.Expression.constant_float(0.1))
event = conn.krpc.add_event(expr)
with event.condition:
    event.wait()

vessel.auto_pilot.disengage()
    
# When there is no more fuel print a message
print('Engine stopped')

# Wait to reach the apoapsis
refframe = vessel.orbit.body.reference_frame
altitude = conn.add_stream(getattr, vessel.flight(refframe), "surface_altitude")
vertical_speed = conn.add_stream(getattr, vessel.flight(refframe), "vertical_speed")

while(vertical_speed() > 0.0):
    time.sleep(.5)

# Make science
makeScience(vessel, 'MK1Pod')
makeScience(vessel, 'MysteryGoo')

# Wait the altitude or the limit velocity to release the parachute (264m/s)

while(altitude() > 3000.0 and vertical_speed() > -250.0):
    time.sleep(.5)

print('Release The parachute')
vessel.control.activate_next_stage()

    


