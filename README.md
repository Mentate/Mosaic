'''
  This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

# Mosaic

# Description
This is a fork of the Microbead detecting software written for CSC-450 at Missouri State University. Intended to stitch together images provided by user and count the total number of microbeads.

# Installation Instructions
* To download python packages ensure you have the latest version of python3 installed, and that you have it in your path. Then in the command prompt navigate to where you have mosaic installed, and run this command "python -m pip install -r requirements.txt". 

#Running the server
Use these commands for window's command prompt. Other OSs' may require different commands
* set FLASK_APP=Server
* set FLASK_ENV=development  
* py -m flask run OR python server.py

# Pull Request Instructions
* Open a pull request into master with a clear description of what was changed and why.
* The pull request will then be reviewed and approved by at least 4 of the 6 collaborators.
* Once approved the branch will be merged with master. 
* If the branch being merged with master was a feature branch, it will be deleted.

# Code Standards 
* All functions should have a docstring consisting of description, parameters, and return value in the format of javadocs.
* Private methods in classes should start with an underscore character.
* Functions and variable names will be in camel case format.
* Functions that don't fit on the screen should be split into multiple functions.
* Each javascript file will start with "use strict". 
* Let and const will be used over var for variable declarations.
