#!/bin/bash
sleep 30  # Wait for system to initialize

# Log current directory
pwd > /home/ec2-user/install-logs.txt

# Install Git
sudo yum install git -y

# Clone repository
cd /home/ec2-user
git clone https://github.com/Mlcruz9/devops_assignments.git

# Navigate to app directory
cd /devops_assignments/week3/ej1_AgsAlb/app

# Make script executable and run
chmod u+x run.sh
./run.sh