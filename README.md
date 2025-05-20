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
| indicator      | Also known as an IOC, this analysis artifact is a piece of forensic data related to online activities. |
| classification | Descriptive labels that explain the nature of the IOC.                                                                                       |
| detected_date  | The value is formatted in ISO 8601 and is the date when we detected the IOC.                                                                 |

### Publications

The indicators in this repo include those relevant to our publications on the threat environment.

["Ukraine War" Malspam Delivers Remcos RAT](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-campaign-briefs/ukraine-war-malspam-delivers-remcos/)

[Ukraine Themed Malspam Delivers Agent Tesla](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-campaign-briefs/ukraine-themed-malspam-drops-agent-tesla/)

[Ukraine Support Fraud](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-threat-advisory/cyber-threat-advisory-ukrainian-support-fraud/)

[Scammers First on the Scene for Türkiye's “Disaster of the Century”](https://blogs.infoblox.com/cyber-threat-intelligence/scammers-first-on-the-scene-for-turkiyes-disaster-of-the-century/)

[The Smish is Coming from Inside the House](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-threat-advisory/the-smish-is-coming-from-inside-the-house/)

[VexTrio DDGA Domains Spread Adware, Spyware, and Scam Web Forms](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-threat-advisory/vextrio-ddga-domains-spread-adware-spyware-and-scam-web-forms/)

[Vast Malvertising Network Hijacks Browser Settings to Spread Riskware](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-threat-advisory/vast-malvertising-network-hijacks-browser-settings-to-spread-riskware/)

[Emotet: A Malware Family That Keeps Going](https://blogs.infoblox.com/cyber-threat-intelligence/emotet-a-malware-family-that-keeps-going/)

[Scams Using Fake Celebrity Endorsements Target EU Countries](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-threat-advisory/scams-using-fake-celebrity-endorsements-target-eu-countries/)

[French Smishing Campaign Uses Fake Social Security Portal](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-threat-advisory/french-smishing-campaign-uses-fake-social-security-portal/)

[Don’t Dial that Number! Distribution of Phishing Lookalikes through Fake Support Calls](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-campaign-briefs/dont-dial-that-number-distribution-of-phishing-lookalikes-through-fake-support-calls/)

[Dog Hunt: Finding Decoy Dog Toolkit via Anomalous DNS Traffic](https://blogs.infoblox.com/cyber-threat-intelligence/cyber-threat-advisory/dog-hunt-finding-decoy-dog-toolkit-via-anomalous-dns-traffic/)

[Decoy Dog is No Pupy (Indicators of Compromise)](https://blogs.infoblox.com/cyber-threat-intelligence/decoy-dog-is-no-ordinary-pupy-distinguishing-malware-via-dns/)

[Decoy Dog is No Ordinary Pupy (Whitepaper)](https://www.infoblox.com/resources/whitepaper/decoy-dog-is-no-ordinary-pupy-distinguishing-malware-via-dns)

[Suspicious DGA Domains, Discovered in DNS, Turn up in Malware Campaigns](https://blogs.infoblox.com/cyber-threat-intelligence/suspicious-dga-domains-discovered-in-dns-turn-up-in-malware-campaigns/)

[Open Tangle Creates a Phishing Net for Consumers](https://blogs.infoblox.com/cyber-threat-intelligence/open-tangle-creates-a-phishing-net-for-consumers/)

[Prolific Puma: Shadowy Link Shortening Service Enables Cybercrime](https://blogs.infoblox.com/cyber-threat-intelligence/prolific-puma-shadowy-link-shortening-service-enables-cybercrime/)

[Your Package Can’t Be Delivered: Identifying USPS Smishing Infrastructure](https://blogs.infoblox.com/cyber-threat-intelligence/phishers-weather-the-storm-the-dns-landscape-of-us-postal-smishing-attacks/)

[Cybercrime Central: VexTrio Operates Massive Criminal Affiliate Program](https://blogs.infoblox.com/cyber-threat-intelligence/cybercrime-central-vextrio-operates-massive-criminal-affiliate-program)

[Beware the Shallow Waters: Savvy Seahorse Lures Victims to Fake Investment Platforms Through Facebook Ads](https://blogs.infoblox.com/cyber-threat-intelligence/beware-the-shallow-waters-savvy-seahorse-lures-victims-to-fake-investment-platforms-through-facebook-ads/)

[RDGAs: The Next Chapter In Domain Generation Algorithms](https://blogs.infoblox.com/threat-intelligence/rdgas-the-next-chapter-in-domain-generation-algorithms/)

[VIGORISH VIPER: A VENOMOUS BET](https://www.infoblox.com/threat-intel/threat-actors/vigorish-viper/)

[LET'S BE CAREFUL OUT THERE](https://blogs.infoblox.com/threat-intelligence/lets-be-careful-out-there/)

[NO, ELON MUSK WAS NOT IN THE U.S. PRESIDENTIAL DEBATE](https://blogs.infoblox.com/threat-intelligence/no-elon-musk-was-not-in-the-us-presidential-debate/)

[DNS PREDATORS ATTACK: VIPERS AND HAWKS HIJACK SITTING DUCKS DOMAINS](https://insights.infoblox.com/resources-research-report/infoblox-research-report-dns-predators-attack-vipers-hawks-hijack-sitting-ducks-domains)

[A PHISHING TALE OF DOH AND DNS MX ABUSE](https://blogs.infoblox.com/threat-intelligence/a-phishing-tale-of-doh-and-dns-mx-abuse/)

[TELEGRAM TANGO: DANCING WITH A SCAMMER](https://blogs.infoblox.com/threat-intelligence/telegram-tango-dancing-with-a-scammer/)

[CLOUDY WITH A CHANCE OF HIJACKING. FORGOTTEN DNS RECORDS ENABLE SCAN ACTORS](https://blogs.infoblox.com/threat-intelligence/cloudy-with-a-chance-of-hijacking-forgotten-dns-records-enable-scam-actor/)

### Additional Information

Infoblox customers can find additional detailed information about the decision criteria for a given indicator in the `notes`
field within the Threat Intelligence Data Exchange (TIDE) database.
