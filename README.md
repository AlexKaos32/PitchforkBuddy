# PitchforkBuddy
This creates user and pass lists, inserting valid credentials every 3rd line.


This is a tool I wrote to help with the PortSwigger Web Academy authentication lab "Broken brute-force protection, IP block". The concept is: 3 consecutive bad logins result in an IP ban. However a valid login results in counter reset. So I needed lists to import to an Intruder Pitchfork attack that would log me in every 3rd request.
