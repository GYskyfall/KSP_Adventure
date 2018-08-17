import krpc

conn = krpc.connect()
vessel = conn.space_center.active_vessel

for res in vessel.resources.all:
    print("Part {} - Resources: {}".format(res.name, res.amount))

