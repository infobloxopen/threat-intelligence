# threat-intelligence

Infoblox's [Threat Intelligence Group (TIG)](https://www.infoblox.com/cyber-threat-intelligence/) detects, curates, and
publishes threat intelligence data pertaining to relevant cyber campaigns. TIG is sharing indicators of compromise (IOCs) 
related to threats that are of high interest to the cyber security community through this public repository. 
The following contains descriptions about the contents of each dataset (i.e data folder). All files are csv formatted 
and [MISP](https://www.misp-project.org/) compatible.


## ukraine
This folder contains IOCs related to the Russian invasion of Ukraine. 
The majority of the content is based on Infoblox internal analytics and validation analysis, though some OSINT is also 
included.  Our references should clearly indicate indicators that originated in OSINT. 

The file `ukraine_russia_malicous_suspicious_iocs.csv` contains malicious and suspicious IOCs that can cause harm to 
businesses and innocent users. Infoblox recommends blocking traffic from network indicators described in this file.

The `ukraine_russia_legitimate_iocs.csv` file contains confirmed indicators that, 
at the time of review, were not evidently associated with malicious activity. The related websites did not show indications 
of hosted malware or fraudulent behavior, but may host content that is not wanted by some users. 
This includes domains belonging to well-known donation sites providing support to Ukrainian civilians, or newly 
created support programs operated by entities positively acknowledged by the online community.  Many of these are
blocked by other vendors due to their new registration or other automated analytics. 

## ccb_indicators
This folder contains IOCs related to our [cyber campaign briefs (ccb)](https://blogs.infoblox.com/category/cyber-threat-intelligence/cyber-campaign-briefs/)

## cta_indicators
This folder contains IOCs related to our [cyber threat advisories (cta)](https://blogs.infoblox.com/category/cyber-threat-intelligence/cyber-threat-advisory/)

###### Schema Table
| Field              | Description |
| -----------        | ----------- |
| type               | The data type of the IOC. Possible options: domain, ip, url, sha256, and email.       |
| indicator          | Also known as an IOC, this analysis artifact is a piece of forensic data related to online activities regarding the Russia-Ukraine conflict.|
| classification     | Descriptive labels that explain the nature of the IOC. |
| references         | A web resource link that provides information related to the indicator and may have been a decision factor for the classification label.  |

### Publications

The indicators in this repo include those relevant to our publications on the threat environment. 

["Ukraine War" Malspam Delivers Remcos RAT](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-campaign-briefs/ukraine-war-malspam-delivers-remcos/)

[Ukraine Themed Malspam Delivers Agent Tesla](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-campaign-briefs/ukraine-themed-malspam-drops-agent-tesla/)

[Ukraine Support Fraud](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-threat-advisory/cyber-threat-advisory-ukrainian-support-fraud/)

### Additional Information

Infoblox customers can find additional detailed inforamtion about the decision criteria for a given indicator in the `notes`
field within the Threat Intelligence Data Exchange (TIDE) database. 

