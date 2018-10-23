# Fraudlogix    
  https://www.fraudlogix.com/
  
### Overview

Fraudlogix is an online advertising fraud detection company. It is the first of its kind to cater to the unique challenges faced by the supply side (ad networks, ad exchanges, and SSPs) and DSPs within the online advertising marketplace, providing them with pre-bid fraud solutions for desktop, mobile, in-app, and video environments. Fraudlogix's pixel-based technology allows it to monitor data from over 640 million unique users, 1.2 billion unique devices, and 12 million URLs monthly. It's able to map the latest devices, locations, bots, behaviors, and hacking tactics that are being used by ad fraudsters. 

Fraudlogix also offers an IP Block List solution that can be used in multiple environments to block impression requests coming from IP addresses known to be associated with ad fraud. The subscription list includes over 4 million IP addresses and is updated hourly.

### PRE-REQUISITES to use Fraudlogix and DNIF  
Outbound access required to clone the Fraudlogix enrichment plugin 

| Protocol   | Source IP  | Source Port  | Direction	 | Destination Domain | Destination Port  |  
|:------------- |:-------------|:-------------|:-------------|:-------------|:-------------|  
| TCP | AD,A10 | Any | Egress	| github.com | 443 |  
| TCP | AD,A10 | Any | Egress	| fraudlogix.com | 443 |


### Using the Fraudlogix API with DNIF
 The Fraudlogix API is found on github at

https://github.com/dnif/enrich-fraudlogix

### Getting started with Fraudlogix API

1. ####    Login to your AD, A10 containers  
   ACCESS DNIF CONTAINER VIA SSH : [Click To Know How](https://dnif.it/docs/guides/tutorials/access-dnif-container-via-ssh.html)
2. ####    Move to the `/dnif/<Deployment-key>/enrichment_plugin` folder path.
```
$cd /dnif/CnxxxxxxxxxxxxV8/enrichment_plugin/
```
3. ####   Clone using the following command  
```  
git clone https://github.com/dnif/enrich-fraudlogix.git fraudlogix
```
### Fraudlogix API enrichment output structure
The output of the lookup call has the following structure (for the available data):

  | Fields        | Description  |
| ------------- |:-------------:|
| EvtType      | An IP address (IPv4/IPv6)|
| EvtName      | The IOC      |
| IntelRef | Feed Name      |
| IntelRefURL | Feed URL    |
| ThreatType | DNIF Feed Identification Name |      
| FLThreatDetail | More details on the threat |
| FLThreatActivityLevel | Activity for the threat indicator  |

An example of Fraudlogix API enrichment feed output
```
{'EvtType': 'IPv4',
'EvtName': '72.197.7.236',
'AddFields':{
'IntelRef': ['FRAUDLOGIX'],
'IntelRefURL': [''],
'ThreatType': ['Malicious'],
'FLThreatDetail': [u'Botnet/Infected Device'],
'FLThreatActivityLevel': ['High']}}
```
