google_config = lambda callback_url, client_id, client_secret: [
    f"from oauthenticator.google import LocalGoogleOAuthenticator",
    f"c.LocalGoogleOAuthenticator.oauth_callback_url = '{callback_url}'",
    f"c.LocalGoogleOAuthenticator.client_id = '{client_id}'",
    f"c.LocalGoogleOAuthenticator.client_secret = '{client_secret}'",
    "c.JupyterHub.authenticator_class = LocalGoogleOAuthenticator",
    f"c.LocalAuthenticator.create_system_users = True",
    f"c.LocalAuthenticator.add_user_cmd = ['adduser', '-q', '--gecos', '\"\"', '--disabled-password', '--force-badname']"
                                                               ]

auth0_config = lambda callback_url, client_id, client_secret: [
    f"from oauthenticator.auth0 import Auth0OAuthenticator",
    f"c.Auth0OAuthenticator.oauth_callback_url = '{callback_url}'",
    f"c.Auth0OAuthenticator.client_id = '{client_id}'",
    f"c.Auth0OAuthenticator.client_secret = '{client_secret}'",    
    f"c.Auth0OAuthenticator.scope = ['openid', 'email']",
    f"c.JupyterHub.authenticator_class = Auth0OAuthenticator",
    f"c.LocalAuthenticator.add_user_cmd = ['adduser', '-q', '--gecos', '\"\"', '--disabled-password', '--force-badname']",
    f"c.LocalAuthenticator.create_system_users = True"    
    ]

github_config = lambda callback_url, client_id, client_secret: [
    f"from oauthenticator.github import GitHubOAuthenticator",
    f"c.GitHubOAuthenticator.oauth_callback_url = '{callback_url}'",
    f"c.GitHubOAuthenticator.client_id = '{client_id}'",
    f"c.GitHubOAuthenticator.client_secret = '{client_secret}'",    
    f"c.JupyterHub.authenticator_class = GitHubOAuthenticator",
    f"c.LocalAuthenticator.add_user_cmd = ['adduser', '-q', '--gecos', '\"\"', '--disabled-password', '--force-badname']",
    f"c.LocalAuthenticator.create_system_users = True"
    
]

providers_config = {
    'google': google_config,
    'auth0': auth0_config,
    'github': github_config
}


import os
env_var = {k.lower():v for k, v in dict(os.environ).items() if v!=''}

if("jhub_oauth_provider" in env_var.keys()):
    assert env_var["jhub_oauth_provider"].lower() in providers_config.keys(), f"Provider {env_var['jhub_oauth_provider']} not supported {', '.join(providers_config.keys())} only"
    assert "jhub_callback_url" in env_var.keys(), "Missing 'JHUB_CALLBACK_URL' environment variable'"    
    assert "jhub_client_id" in env_var.keys(), "Missing 'JHUB_CLIENT_ID' environment variable'"
    assert "jhub_client_secret" in env_var.keys(), "Missing 'JHUB_CLIENT_SECRET' environment variable'"
    
    jhub_config = open("/git/jhub/jupyterhub_raw.py","r").read()
    
    callback_url, client_id, client_secret = env_var["jhub_callback_url"], env_var["jhub_client_id"], env_var["jhub_client_secret"]
    addl_config = providers_config[env_var["jhub_oauth_provider"].lower()](callback_url, client_id, client_secret)

    with open("/srv/jupyterhub/jupyterhub_config.py", "w") as fw:
        fw.write(jhub_config+"\n")
        for line in addl_config:
            fw.write(line+"\n")