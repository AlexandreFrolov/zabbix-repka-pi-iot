#!/bin/bash
echo "8" > /sys/class/gpio/export                  
sleep 0.1
echo "out" > /sys/class/gpio/gpio8/direction
sleep 0.1
echo "1" > /sys/class/gpio/gpio8/value
sleep 5
echo "0" > /sys/class/gpio/gpio8/value 
sleep 0.1
echo "8" > /sys/class/gpio/unexport   
sleep 0.1
