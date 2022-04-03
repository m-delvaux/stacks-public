def process(env_var):
    assert "router_cloudflare_username" in env_var.keys(), "Missing 'ROUTER_CLOUDFLARE_USERNAME' environment variable'"
    assert "router_cloudflare_token" in env_var.keys(), "Missing 'ROUTER_CLOUDFLARE_TOKEN' environment variable'"
    assert "router_cert_email" in env_var.keys(), "Missing 'ROUTER_CLOUDFLARE_TOKEN' environment variable'"
    assert "router_cert_domain" in env_var.keys(), "Missing 'ROUTER_CLOUDFLARE_TOKEN' environment variable'"
    
    addl_config = open("/git/router-cloudflare/robocert/robocert.config.template.yml", "r").read()
    
    return (
        addl_config.replace("__EMAIL_ACCOUNT__", env_var["router_cert_email"])
                   .replace("__CLOUDFLARE_USERNAME__", env_var["router_cloudflare_username"])
                   .replace("__CLOUDFLARE_TOKEN__", env_var["router_cloudflare_token"])
                   .replace("__DOMAIN__", env_var["router_cert_domain"])
    )

import os
env_var = {k.lower():v for k, v in dict(os.environ).items() if v!=''}

config = process(env_var)
with open("/git/router-cloudflare/robocert/robocert.config.yml", "w") as fw:
    fw.write(addl_config+"\n")