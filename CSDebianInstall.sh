#!/bin/bash

# This script will install the dependencies needed for
# Cobalt Strike on an Ubuntu 14.04 x64 system

sudo apt-get update
sudo apt-get install build-essential
sudo apt-get install software-properties-common
sudo add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
sudo apt-get update
sudo apt-get install oracle-java8-installer