import json
dic_data2={
    'router':[
    {"model":'7206VXR',
     "so" :'Cisco IOS',
     "vendor" :'Cisco',
     "type" :'hardware' 
     }],
    'server1':[
    {'name':'server_Sergio',
     'service':'WEB',
     'remote_conection':'SSH',
     'linux distribution':'Mint'
                }],
    'server2':[
    {'name':'server_Gemma',
     'service1':'DNS',
     'service2':'WEB',
     'linux distribution':'Centos 8'
                }],
    'server3':[
    {'name':'server_Ana',
     'service1':'FTP',
     'service2':'DHCP',
     'linux distribution':'Centos 8'
                }]
    }
print(json.dumps(dic.data, indent=2))