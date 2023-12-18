#!/bin/bash

cd Downloads/
## Get and uninstall old chrome
old_chrome=$(rpm -qa | grep chrome)
sudo rpm -e $chrome
## Get and install new chrome
new_chrome=$(ls *.rpm | grep google)
sudo rpm -ivh $new_chrome
rm $new_chrome

echo "Done :)"