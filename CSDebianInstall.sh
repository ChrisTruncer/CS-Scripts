#!/bin/bash

# This script will install the dependencies needed for
# Cobalt Strike on an Ubuntu 14.04 x64 system

apt-get update
apt-get install build-essential dirmngr
apt-get install software-properties-common
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886
add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
apt-get update
apt-get install oracle-java8-installe
