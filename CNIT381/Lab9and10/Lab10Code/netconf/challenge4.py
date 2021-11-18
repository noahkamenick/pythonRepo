from ncclient import manager
import xml.dom.minidom as p
import routers
import xmltodict

m = manager.connect(**routers.router)

# NETCONF Config Template to use
netconf_template = open("config_templ_ietf_interface.xml").read()

print(netconf_template)

# Build the XML Configuration to Send
netconf_payload = netconf_template.format(int_name = "Loopback",
                                          int_num="100",
                                          int_desc="Configured by NETCONF with a Template",
                                          ip_address="100.1.1.1",
                                          subnet_mask="255.255.255.0"
                                          )
print("Config Payload")
print("--------------")
print(netconf_payload)

print("#"*80)
# Send NETCONF <edit-config>
netconf_reply = m.edit_config(target="running", config=netconf_payload)

# Print the NETCONF Reply
print(netconf_reply)