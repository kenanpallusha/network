from pysnmp.hlapi import *

def get_snmp(ip, oid):
    iterator = getCmd(SnmpEngine(),
                      CommunityData('public'),
                      UdpTransportTarget((ip, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity(oid)))
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        return errorIndication
    else:
        return varBinds[0][1]

print("CPU Load:", get_snmp('192.168.1.1', '1.3.6.1.4.1.9.2.1.57.0'))
