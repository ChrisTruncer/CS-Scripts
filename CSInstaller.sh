#!/bin/bash

# This script will install the dependencies needed for
# Cobalt Strike on an Ubuntu 14.04 x64 system

apt-get update
apt-get -y install build-essential software-properties-common dirmngr default-jre

