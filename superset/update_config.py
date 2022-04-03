def google_config(env_var):
    assert "superset_client_id" in env_var.keys(), "Missing 'superset_CLIENT_ID' environment variable'"
    assert "superset_client_secret" in env_var.keys(), "Missing 'superset_CLIENT_SECRET' environment variable'"
    
    addl_config = open("/git/superset/addl_config.google.py", "r").read()
    
    return (
    addl_config.replace("__CLIENT_ID__", env_var["superset_client_id"])
               .replace("__CLIENT_SECRET__", env_var["superset_client_secret"])
           )


def auth0_config(env_var):
    assert "superset_client_id" in env_var.keys(), "Missing 'superset_CLIENT_ID' environment variable'"
    assert "superset_client_secret" in env_var.keys(), "Missing 'superset_CLIENT_SECRET' environment variable'"
    assert "superset_auth0_subdomain" in env_var.keys(), "Missing 'SUPERSET_AUTH0_SUBDOMAIN' environment variable'"
    
    addl_config = open("/git/superset/addl_config.auth0.py", "r").read()
    return (
    addl_config.replace("__AUTH0_DOMAIN__", env_var["superset_auth0_subdomain"])
               .replace("__CLIENT_ID__", env_var["superset_client_id"])
               .replace("__CLIENT_SECRET__", env_var["superset_client_secret"])
           )


providers_config = {
    'google': google_config,
    'auth0': auth0_config
}


import os
env_var = {k.lower():v for k, v in dict(os.environ).items() if v!=''}

if("superset_oauth_provider" in env_var.keys()):
    assert env_var["superset_oauth_provider"].lower() in providers_config.keys(), "Provider "+env_var['superset_oauth_provider']+" not supported ("+', '.join(providers_config.keys())+" only"
    
    addl_config = providers_config[env_var["superset_oauth_provider"].lower()](env_var)

    with open("/git/superset/docker-setup/pythonpath_dev/superset_config_docker.py", "w") as fw:
        fw.write(addl_config+"\n")