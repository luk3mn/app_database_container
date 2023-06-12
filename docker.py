#!/usr/bin/env python
import subprocess

# Update package manager
update_cmd = ['sudo', 'apt-get', 'update']
subprocess.run(update_cmd, check=True)

# Install Docker
install_cmd = ['sudo', 'apt-get', 'install', 'docker.io', '-y']
subprocess.run(install_cmd, check=True)

# Install Docker compose
install_cmd = ['sudo', 'apt-get', 'install', 'docker-compose', '-y']
subprocess.run(install_cmd, check=True)

# Execute Docker compose
excute_cmd = ['sudo', 'docker-compose', 'up','-d']
subprocess.run(excute_cmd, check=True)

# List containers
list_cmd = ['sudo', 'docker', 'ps']
subprocess.run(list_cmd, check=True)
