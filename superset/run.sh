python /git/superset/update_config.py;
touch /app/docker && rm -rf /app/docker/*;
cp -rf /git/superset/docker-setup/* /app/docker && chmod +x /app/docker/*.sh;