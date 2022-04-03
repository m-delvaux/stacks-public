import random, string

genkey = lambda app_name, client_id, client_secret: hashlib.md5(f"{app_name}_{client_id}_{client_secret}".encode("utf-8")).hexdigest()

def google_config(env_var):
    assert "router_client_id" in env_var.keys(), "Missing 'ROUTER_CLIENT_ID' environment variable'"
    assert "router_client_secret" in env_var.keys(), "Missing 'ROUTER_CLIENT_SECRET' environment variable'"
    
    addl_config = open("/git/router-cloudflare/oauth2proxy/config.template.cfg", "r").read()
    
    app_name = "Authentication" if "router_app_name" not in env_var.keys() else env_var["router_app_name"]
    client_id, client_secret = env_var["router_client_id"], env_var["router_client_secret"]
    
    
    return (
        addl_config.replace("__CLIENT_ID__", env_var["router_client_id"])
                   .replace("__CLIENT_SECRET__", env_var["router_client_secret"])
                   .replace("__WHITELISTED_DOMAINS__", '"*"' if "router_whitelisted_domains" not in env_var.keys() 
                                                             else '"'+'",'.join(env_var["router_whitelisted_domains"].split(","))+'"'
                           )
                   .replace("__PROVIDER__", "google")
                   .replace("__APP_NAME__", app_name)
                   .replace("__APP_SECRET__", genkey(app_name, client_id, client_secret))
           )

providers_config = {
    'google': google_config
}


import os
env_var = {k.lower():v for k, v in dict(os.environ).items() if v!=''}

if("router_oauth_provider" in env_var.keys()):
    assert env_var["router_oauth_provider"].lower() in providers_config.keys(), "Provider "+env_var['router_oauth_provider']+" not supported ("+', '.join(providers_config.keys())+" only"
    
    addl_config = providers_config[env_var["router_oauth_provider"].lower()](env_var)

    with open("/git/router-cloudflare/oauth2proxy/config.cfg", "w") as fw:
        fw.write(addl_config+"\n")