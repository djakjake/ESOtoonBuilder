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

Installation
============
Instructions notes. Tested on:
1. Ubuntu VERSION="18.04.4 LTS (Bionic Beaver)
1. GNU bash, version 4.4.20(1)-release (x86_64-pc-linux-gnu)
1. Python 3.6.9 (virtual environment installation handled by setEnv.sh)
  - Numpy 1.18.4
  - Pandas 1.0.3

Installation instructions:
1. Navigate to the directory you desire ESOtoonBuilder to be. (bash)

    ```bash
    cd /path/to/directory
    ```
  
1. clone the repository (example using the SSH URL) (bash)

    ```bash
    git clone git@github.com:djakjake/ESOtoonBuilder.git
    ```
    
Using ESOtoonBuilder
====================
NOTE: It is assumed that the current working directory is the root directory path to ESOtoonBuilder
1. Before each session, download any repository and/or python updates (optional) (bash)

    ```bash
    ./update.sh
    ```

1. source the python environment (bash)

    ```bash
    source setEnv.sh
    ```

1. execute script (bash)

    ```bash
    ./ESOtoonBuilder.py <options>
    ```
    
    OR
    
    ```bash
    python ESOtoonBuilder.py <options>
    ```
    
# Using the User Configuration File
make any changes at your own risk (although any unintential screw-ups can be reverted using git)
basic Python syntax is helpful, but not necessarily required. refrain from moving variables around, just change the values associated with them (eg)
```python
class <Module>:
  <subModule> = {
    '<variable_1>': <value_1>,
    '<variable_2>': <value_2>,
  }
```

Feel free to adjust <value_x> input; but there are internal checks for some values, which may cause this to Error out with a helpful message. For instance, if you sum of all the attribute points you set is greater than the max allowed attributes, it will raise an assertion error and point out the fact that you alloted too many attribute points.

Build Plans
===========
1. build scripting environment with setEnv.sh --Done
1. track (and install) python requirements with requirements.txt --Done
1. set up directory --Done
1. set up sim configuration/input/options --Done
1. set up main module --In Progress 
  - build Character module --In Progress
    - Attributes --Done
    - BuffFood --Not Started
    - ChampionPoints --Not Started
    - Equipment --Not Started
    - Mundus --In Progress
    - Potions --Not Started
    - Race --Not Started
    - Skills -Not Started
  - build DOE module --Not Started
    - TBD
  - build Sim module --Not Started (not in current directory)
    - TBD
  - build optimization module --Not Started (not in current directory)
    - TBD
