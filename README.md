# threat-intelligence

Infoblox's [Threat Intelligence Group (TIG)](https://www.infoblox.com/threat-intel/) detects, curates, and
publishes threat intelligence data pertaining to relevant cyber campaigns. TIG is sharing indicators of compromise (IOCs)
related to threats that are of high interest to the cyber security community through this public repository.
The following contains descriptions about the contents of each dataset (i.e data folder). The folders within this repository
contain csv and JSON files that are [MISP](https://www.misp-project.org/) compatible.

This material is being provided by Infoblox under the Creative Commons CC BY 4.0 license. This license allows you to
share and adapt the material, in particular to use it for both commercial and non-commercial security purposes, under
the terms of: attribution to Infoblox and the license. For more details, see the LICENSE file in our repo or visit
https://creativecommons.org/licenses/by/4.0/

## indicators
The indicators folder contains both csv and JSON formatted files that are compatible with MISP. The contents relate to
compelling cyber crime events, such as IOCs controlled by specific DNS threat actors or cyber campaigns related to major 
war conflicts and natural disasters. 

The majority of the content is based on Infoblox internal analytics and validation analysis, though some OSINT is also
included. Files contain a classification column describing the threat severity of indicators. Indicators with malicious 
classifications are largely confirmed threats and suspicious classifications are high risk. Infoblox recommends blocking 
traffic from high threat severity network indicators described in these files.

## research_data
This folder contains useful information associated with malicious binaries that can help security professionals 
find other related software on their networks. Information includes configuration settings or encryption keys used by
malware. We also provide [YARA rules](https://yara.readthedocs.io/en/stable/writingrules.html) for specific threats. 
Security operation center (SOC) teams and threat researchers can run these rules retrospectively to determine if their
networks were previously targeted by malware.

## sample-code
Infoblox is sharing code with the cybersecurity community in the hopes of facilitating threat research, investigation, 
and automated detection. This includes utility code that can help researchers re-produce the results we describe and 
share via our publications. We normally distribute our code samples under the GNU General Public License v3.0+ license.

###### Schema Table
| Field          | Description                                                                                                                                  |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| type           | The data type of the IOC. Possible options: domain, ip, url, sha256, and email.                                                              |
| indicator      | Also known as an IOC, this analysis artifact is a piece of forensic data related to online activities regarding the Russia-Ukraine conflict. |
| classification | Descriptive labels that explain the nature of the IOC.                                                                                       |
| detected_date  | The value is formatted in ISO 8601 and is the date when we detected the IOC.                                                                 |

### Publications

The indicators in this repo include those relevant to our publications on the threat environment.

["Ukraine War" Malspam Delivers Remcos RAT](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-campaign-briefs/ukraine-war-malspam-delivers-remcos/)

[Ukraine Themed Malspam Delivers Agent Tesla](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-campaign-briefs/ukraine-themed-malspam-drops-agent-tesla/)

[Ukraine Support Fraud](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-threat-advisory/cyber-threat-advisory-ukrainian-support-fraud/)

[Scammers First on the Scene for Türkiye's “Disaster of the Century”](https://blogs.infoblox.com/cyber-threat-intelligence/scammers-first-on-the-scene-for-turkiyes-disaster-of-the-century/)

[Cybercrime Central: VexTrio Operates Massive Criminal Affiliate Program](https://blogs.infoblox.com/cyber-threat-intelligence/cybercrime-central-vextrio-operates-massive-criminal-affiliate-program/)

[Prolific Puma: Shadowy Link Shortening Service Enables Cybercrime](https://blogs.infoblox.com/cyber-threat-intelligence/prolific-puma-shadowy-link-shortening-service-enables-cybercrime/)

[Open Tangle Creates a Phishing Net for Consumers](https://blogs.infoblox.com/cyber-threat-intelligence/open-tangle-creates-a-phishing-net-for-consumers/)

[VIGORISH VIPER: A VENOMOUS BET](https://www.infoblox.com/threat-intel/threat-actors/vigorish-viper/)

### Additional Information

Infoblox customers can find additional detailed information about the decision criteria for a given indicator in the `notes`
field within the Threat Intelligence Data Exchange (TIDE) database.
