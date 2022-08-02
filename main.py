from pyzabbix import ZabbixAPI

zapi = ZabbixAPI("http://192.168.32.166/zabbix")
zapi.login("zadmin", "password")
# You can also authenticate using an API token instead of user/pass with Zabbix >= 5.4
# zapi.login(api_token='xxxxx')
groupid = "" # Group ID
groupToGet = "A" # Clinet Group
Hosts = [] # List of hosts

# Get's a client group's ID
for h in zapi.hostgroup.get(output="extend", filter={"name":[groupToGet]} ):
    # print("Group ID: " + h['groupid'])
    groupid = h['groupid']+""

# Get's All Hosts in a client group
for h in zapi.host.get(groupids=groupid):
    # print("Name: " + h['name'])
    Hosts.append(h['hostid'])

# Get's all graphs in a client group
for i in range(len(Hosts)):
    for h in zapi.graph.get(output="extend", hostids=Hosts[i]):
        if h['name'] in ["CPU utilization", "Memory utilization"]:
            print("Name of Graph: " + h['name'] + " || Graphid: " + h['graphid'] + " || Host ID: " + Hosts[i])

#print(Hosts)