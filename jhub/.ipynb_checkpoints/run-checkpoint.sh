# Install dependencies
apt-get update && apt-get install -y python build-essential python-dev python3-dev;
pip3 install oauthenticator jupyter jupyterlab;
curl -sL https://deb.nodesource.com/setup_14.x | bash -;
RUN apt-get install -yq nodejs;

# Create default user configuration
echo "SKEL=/etc/skel" >> /etc/default/useradd && mkdir /home/shared && ln -s /home/shared /etc/skel/shared;

# Update jupyter_config.py
python /git/jhub/update_config.py;