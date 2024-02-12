# Research Data
For our research we established a Pupy server and routed communications between the server and clients through our recursive resolvers. 
​
We collected those DNS query logs for our analysis and are making the logs available for research. The data covers several days of varying activity. Most of the time, we controlled the clients by establishing a reverse proxy and commands were sent through SSL. We suspect this is the case for Decoy Dog as well. 
​
However we did exercise all of the available commands via DNS responses from the server. Additionally, there are time periods with multiple clients active simultaneously and numerous client restarts. The scope of activity included should allow for the results in our paper to be recreated. 
​
You can find the ascosciated indicators with this part of the research data in  https://github.com/infobloxopen/threat-intelligence/blob/main/indicators/csv/decoy_dog_cta_20230714_iocs.csv

## Folder Architecture : 
   > - traffic.csv
   > - /binaries/
   >     -  /binaries/$HASH/keys.txt
   >     -  /binaries/$HASH/conf.txt
   > - decoy_dog.yar
   > - decoy_dog.telfhash
​
​
## Traffic logs : 
The query-response logs (`traffic.csv`) contain A record results and are packaged in a csv file that contains the following fields: 
    - timestamp: the time of the query in Unix epoch seconds.
    - query: the fully qualified domain name transmitted in the client query.
    - response: the set of IP addresses returned by the server.
    - client_payload_len: the number of payload bytes within the query, including the host information.  
    - server_payload_len: the number of payload bytes within the response. 
​
## Binary artifacts and rules 
In addition, we are providing some data that resulted from reverse engineering binary samples available on VirusTotal in the `binaries` folder. This includes the following: 
​
>   -    Embedded configuration parameters a `conf.txt` file per binary 
>   -    Embedded cryptographic keys and password - a `keys.txt` file per binary that contains :
>        -  BIND_PAYLOADS_PASSWORD
>        -   DCONFIG_PUBLIC_KEY (only for client v4)
>        -   DNSCNC_PUB_KEY_V2
>        -   ECPV_RC4_PRIVATE_KEY
>        -   ECPV_RC4_PUBLIC_KEY
>        -   SCRAMBLESUIT_PASSWD
>        -   SIMPLE_RSA_PUB_KEY
>        -   SIMPLE_RSA_PRIV_KEY
>        -   SSL_BIND_CERT
>        -   SSL_BIND_KEY 
>        -   SSL_CA_CERT
>        -   SSL_CLIENT_CERT
>        -   SSL_CLIENT_KEY
>
We also provide a yara rule to detect the Data Dog binaries (`decoy_dog.yar`), and a TELF hash that can be used for the same purpose.
