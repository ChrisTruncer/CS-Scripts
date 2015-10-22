#!/bin/bash

# This script will install the dependencies needed for
# Cobalt Strike on an Ubuntu 14.04 x64 system

sudo apt-get update
sudo apt-get install build-essential
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee -a /etc/apt/sources.list
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee -a /etc/apt/sources.list
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
apt-get update
# Java 7
apt-get install oracle-java7-installer