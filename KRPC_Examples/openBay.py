import krpc
import time

conn = krpc.connect()
vessel = conn.space_center.active_vessel

for part in vessel.parts.all:
    if part.name == 'ServiceBay.125':
        if part.cargo_bay:
            print("Part {} {}\n".format(part.name, part.cargo_bay.open))
            part.cargo_bay.open = True
time.sleep(5)
