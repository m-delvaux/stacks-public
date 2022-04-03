upstream = lambda ix, target: "upstream up"+str(ix)+" {server "+target+";}"
#upstream jhub {server jupyterhub:6000;}
nmap = lambda ix, fqdn: "\t"+fqdn+"\t up"+str(ix)+";"

def buildMap(env_var):
    assert "router_nginx_proxies" in env_var.keys(), "Missing 'ROUTER_NGINX_PROXIES' environment variable'"
    
    channels = env_var['router_nginx_proxies'].split(";")
    upstreams, maps = [], []
    
    for ix, channel in enumerate(channels):
        details = channel.split(",")
        assert len(details)==2, "The structure of the 'ROUTER_NGINX_PROXIES' should be 'domain1,mapping1:port1;domain2,mapping2:port2'"
        
        maps.append(nmap(ix, details[0]))
        upstreams.append(upstream(ix, details[1]))
    
    return  upstreams + ["", "map $http_host $backend {"] + maps + ["}"]

def buildWhiteList(env_var):
    assert "router_nginx_whitelists" in env_var.keys(), "Missing 'ROUTER_NGINX_WHITELISTS' environment variable'"
    
    open_sites = env_var['router_nginx_whitelists'].split(",")
    if(len(open_sites)==1 and open_sites[0]=""):
        open_sites=['none']
    return "server_name "+" ".join(open_sites)+";"

import os
env_var = {k.lower():v for k, v in dict(os.environ).items() if v!=''}

with open("/git/router-cloudflare/nginx/conf.d/map.conf", "w") as fw:
    for line in buildMap(env_var):
        fw.write(line+"\n")
        
with open("/git/router-cloudflare/nginx/conf.d/whitelist.conf", "w") as fw:
    fw.write(buildWhiteList(env_var)+"\n")