# ESOtoonBuilder

The idea is to run a character building sim that allows user to test builds that control:
1. race (passives)
1. attribute points
1. champion points (and passives)
1. equipement (sets and passives)
1. abilities (active + passives)
1. mundus stone (passives)
1. buff food (passives)
1. potions (passives)

After the ability to build a character is complete, Design an experiment, perhaps using latin hypercubes, where the above listed are control variables and monte carlo variables can be taken fron the configuration file. some ideas for monte carlo variables are:
1. enemy density
1. enemy damage rate
1. enemy damage type
1. player light attack rate
1. player heavy attack rate
1. average down time between proc'ed abilities (active, passive, gear)

After running the toon building sim, perform analysis and optimazation for desired stats. ie:
1. weapon/spell damage
1. weapon/spell crit
1. physical/spell resistance
1. max stats
1. etc...
each desired stat would be given a weight than the optimization would run based on the desired outcome.

This is just my thinking. the problem may not be well-defined or too complex; but it seems like a fun problem. if it does work, then many people might enjoy it.

Build Plans
===========
1. build scripting environment with setEnv.sh --Done
1. track (and install) python requirements with requirements.txt --Done
1. set up directory --Done
1. set up sim configuration/input/options --Done
1. set up main module --Not Started
1. build submodules --Not Started
1. Design of Experiment --Not Started
1. run simulation --Not Started (not in current directory)
1. optimization --Not Started (not in current directory)
