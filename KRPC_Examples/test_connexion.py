#!python

'''
First test for KRPC

The script simply do a connexion to KSP and print the version of KRPC
'''

import krpc

conn = krpc.connect(
    name='Test Program',
    address='127.0.0.1',
    rpc_port=50000, stream_port=50001)

print('Connexion established!')
print('KRPC Version: {}'.format(conn.krpc.get_status().version))

