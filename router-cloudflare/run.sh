python /git/router-cloudflare/update-nginx-config.py;
python /git/router-cloudflare/update-oauth-config.py;
python /git/router-cloudflare/update-robocert-config.py;
cp -rf /git/router-cloudflare/oauth2proxy/config.cfg /oauth2proxy/config.cfg;
cp -rf /git/router-cloudflare/robocert/config.yml /robocert/config.yml;
cp -rf /git/router-cloudflare/nginx/* /nginx/;