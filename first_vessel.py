#!krpc-env/bin/python3
'''
First Mission: First Vessel

Launch first vessel and get science from launch pad and from altitude
'''

import krpc
import time

def countDown(start=5):
    print('Countdown...')
    for i in range(start, 0, -1):
        print('{}...'.format(i))
        time.sleep(1)
    
conn = krpc.connect(
    name='Mission I',
    address='127.0.0.1',
    rpc_port=50000, stream_port=50001)

vessel = conn.space_center.active_vessel

vessel.auto_pilot.target_pitch_and_heading(90, 90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
time.sleep(1)

countDown()

print('Ignition!')
vessel.control.activate_next_stage()

fuel_amount = conn.get_call(vessel.resources.amount, 'SolidFuel')
expr = conn.krpc.Expression.less_than(
    conn.krpc.Expression.call(fuel_amount),
    conn.krpc.Expression.constant_float(0.1))
event = conn.krpc.add_event(expr)
with event.condition:
    event.wait()
print('Booster separation')

fight = conn.get_call(vessel.flight())
expr = conn.krpc.Expression.less_than(
    conn.krpc.Expression.call(flight).speed,
    conn.krpc.Expression.constant_float(30.0))
event = conn.krpc.add_event(expr)
with event.condition:
    event.wait()
    
print('Release Parachute')
vessel.control.activate_next_stage()


