# Using your favorite scripting language please code a nagios plugin.
# This nagios plugin must monitor for how many users are logged into a system
# and return the proper return code using the plugin api listed.
# https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/pluginapi.html
# 
# The script must take command line arguments for warning and critical thresholds but also have
# a default setting if no arguments are passed to the script.
#
# example command syntax 
# ./monitor_users -w 5 -c 10
#
# Bonus if you can add an argument to monitor for a specific user
# example command syntax 
# ./monitor_users -w 5 -c 10 -u root


This is a bash script to be used by NRPE for Nagios Checks
steps:
1) define command:
2) define service for the host
