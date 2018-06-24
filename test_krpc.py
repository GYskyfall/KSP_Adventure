#!krpc-env/bin/python3
import krpc

conn = krpc.connect(
    name='Test Program',
    address='127.0.0.1',
    rpc_port=50000, stream_port=50001)

print('Connexion established!')
print('KRPC Version: {}'.format(conn.krpc.get_status().version))

