from ncclient import manager
import xml.dom.minidom as p

m = manager.connect(
    host="192.168.56.102",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

netconf_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback0</name>
        </interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback0</name>
        </interface>
    </interfaces-state>
</filter>
"""
print('#'*80)
netconf_reply = m.get(netconf_filter)
print(p.parseString(netconf_reply.xml).toprettyxml())



