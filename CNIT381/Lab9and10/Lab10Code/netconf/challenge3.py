from ncclient import manager
import xml.dom.minidom as p
import xmltodict

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
intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
intf_config = intf_details["interfaces"]["interface"]
intf_info = intf_details["interfaces-state"]["interface"]

print("")
print(" Interface Details:")
print(" Name: {}".format(intf_config["name"]["#text"]))
print(" Description: {}".format(intf_config["description"]))
print(" IPv4: {}".format(intf_config["ipv4"]["address"]["ip"]))
print(" Type: {}".format(intf_config["type"]["#text"]))
print(" MAC Address: {}".format(intf_info["phys-address"]))
print(" Packets Input: {}".format(intf_info["statistics"]["in-unicast-pkts"]))
print(" Packets Output: {}".format(intf_info["statistics"]["out-unicast-pkts"]))