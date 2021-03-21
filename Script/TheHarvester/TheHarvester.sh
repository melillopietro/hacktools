#!/bin/bash
clear
echo '+--------------------------------------------+'
echo '|                                            |'
echo '|                theHarvester                |'
echo '|                                            |'
echo '+--------------------------------------------+'

echo """
Opzioni disponibili:
  d) DOMAIN, --domain DOMAIN
                        Company name or domain to search.
  l) LIMIT, --limit LIMIT
                        Limit the number of search results, default=500.
  S) START, --start START
                        Start with result number X, default=0.
  g) --google-dork     Use Google Dorks for Google search.
  p) --proxies         Use proxies for requests, enter proxies in proxies.yaml.
  s) --shodan          Use Shodan to query discovered hosts.
  --screenshot SCREENSHOT
                        Take screenshots of resolved domains specify output directory:
                        --screenshot output_directory
  v) --virtual-host    Verify host name via DNS resolution and search for virtual hosts.
  e) DNS_SERVER, --dns-server DNS_SERVER
                        DNS server to use for lookup.
  t) DNS_TLD, --dns-tld DNS_TLD
                        Perform a DNS TLD expansion discovery, default False.
  r) --take-over       Check for takeovers.
  n) --dns-lookup      Enable DNS server lookup, default False.
  c) --dns-brute       Perform a DNS brute force on the domain.
  f) FILENAME, --filename FILENAME
                        Save the results to an HTML and/or XML file.
  b) SOURCE, --source SOURCE
                        baidu, bing, bingapi, bufferoverun, certspotter, crtsh, dnsdumpster, duckduckgo,
                        exalead, github-code, google, hackertarget, hunter, intelx, linkedin, linkedin_links,
                        netcraft, otx, pentesttools, projectdiscovery, qwant, rapiddns, securityTrails,
                        spyse, sublist3r, threatcrowd, threatminer, trello, twitter, urlscan, virustotal, yahoo
"""
read -p "Seleziona le opzioni da utilizzare: " opzioni
comando="theHarvester"

lung=${#opzioni}
for i in `seq $lung`
do
	case ${opzioni:$i-1:1} in
		d)
			read -p "Dominio da ricercare: " tmp
			comando="${comando} -d ${tmp}"
		;;
		
		l)
			read -p "Quante pagine: " tmp
			comando="${comando} -l ${tmp}"
		;;
		
		S)
			read -p "Pagina da cui partire: " tmp
			comando="${comando} -l ${tmp}"
		;;
		
		g)
		
		;;
		
		p)
		
		;;
		
		s)
		
		;;
		
		v)
		
		;;
		
		e)
		
		;;
		
		t)
		
		;;
		
		r)
		
		;;
		
		n)
		
		;;
		
		c)
		
		;;
		
		f)
			read -p "Nome del file: " tmp
			cartella=$(echo $tmp | awk 'BEGIN{FS = "."} ; {print $1}')
			mkdir ./TheHarvester/Scan/$cartella
			comando="${comando} -f ./TheHarvester/Scan/${cartella}/${tmp}"
		;;
		
		b)
			read -p "Dove vuoi ricercare: " tmp
			comando="${comando} -b ${tmp}"
		;;
	esac
done
clear
echo $comando
$comando
clear
echo $comando
$comando
