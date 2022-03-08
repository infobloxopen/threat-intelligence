# threat-intelligence

Infoblox's [Threat Intelligence Group (TIG)](https://www.infoblox.com/cyber-threat-intelligence/) detects, curates, and
publishes threat intelligence data pertaining to relevant cyber campaigns. TIG is sharing indicators of compromise (IOCs) 
related to threats that are of high interest to the cyber security community through this public repository. 
The following contains descriptions about the contents of each dataset (i.e data folder). All files are csv formatted 
and [MISP](https://www.misp-project.org/) compatible.


### ukraine
This folder contains IOCs related to the Russia-Ukraine conflict. Majority of the content has been organically generated
using both internal and private data. 

The `ukraine_russia_legitimate_iocs.csv` file contains confirmed indicators that, 
at the time of review, were not evidently associated with malicious activity. The related websites did not show indications 
of hosted malware or fraudulent behavior, but may still host content that is not wanted by some users. 
This includes domains belonging to well-known donation sites providing support to Ukrainian civilians, or even newly 
created support programs operated by entities positively acknowledged by the online community. 

Oppositely, `ukraine_russia_malicous_suspicious_iocs.csv` contains malicious and suspicious IOCs that can cause harm to 
businesses and innocent users. Infoblox recommends blocking traffic from network indicators described in this file.

###### Schema Table
| Field              | Description |
| -----------        | ----------- |
| type               | The data type of the IOC. Possible options: domain, ip, url, sha256, and email.       |
| indicator          | Also known as an IOC, this analysis artifact is a piece of forensic data related to online activities regarding the Russia-Ukraine conflict.|
| classification     | Descriptive labels that explain the nature of the IOC. |
| references         | A web resource link that provides information related to the indicator and may have been a decision factor for the classification label.  |