🔥 Logitech G29 steering wheel connects to CARLA
======

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md) ![example](https://img.shields.io/badge/Python-API-red.svg) ![example](https://img.shields.io/badge/Ubuntu-18.04-yellow.svg) ![example](https://img.shields.io/badge/Logitech-G29-yellow.svg) ![example](https://img.shields.io/badge/CARLA-0.9.10-yellow.svg)
 
## 🏷️ The overview of Human expert collects the datasets via the Logitech G29 steering wheel. This repo is part of [SGADS](https://github.com/Tangzj2020/SGADS) 
![images](G29.png)


## 1.Install CARLA
* Based on Ubuntu 18.04
* Download  [CARLA_0.9.10](https://github.com/carla-simulator/carla/releases)

    `$ export PYTHONPATH=$PYTHONPATH:$YourFolder$/CARLA_0.9.10/PythonAPI/carla/dist/carla-0.9.10-py3.7-linux-x86_64.egg`
    
    `$ cd ~/YourFolder/CARLA_0.9.10/PythonAPI/examples $` and `Add manual_control_steeringwheel_G29.py`
  
    `$ pip install pygame==1.9.6 $`


## 2.Launch the CARLA server
* Enter the CARLA root folder:
  
    `$ cd ~/YourFolder/CARLA_0.9.10`
  
    `$ ./CarlaUE4.sh -opengl -carla-port=2000`
## 3.Install jstest-gtk


* jstest-gtk is a simple joystick testing and configuration tool based on Gtk+. It provides you with an additional list of joysticks, a way to display pressed buttons and axes, a method for remapping axes and buttons, and a method for calibrating the joystick. 

* To install jstest-gtk, use the following command:

    `$ sudo apt-get update `

    `$ sudo apt-get install jstest-gtk `



   
## 4.Running PythonAPI via G29

* Add wheel_config.ini file to below path: 

    `$ cd ~/YourFolder/CARLA_0.9.10/PythonAPI/examples`
    
* you also reset axes and buttions:
  
    `$ gedit wheel_config.int`
  
* Runing demo with follow command：
  
    `$ python manual_control_steeringwheel_carla.py`
  
* A simple function can be checked in `Collect_expert_data-via-G29.py`


