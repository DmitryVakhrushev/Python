Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> players = [29, 58, 66, 71, 87]
>>> players[2]
66

>>> players[2]=68
>>> players
[29, 58, 68, 71, 87]
>>> players + [90, 91, 98]
[29, 58, 68, 71, 87, 90, 91, 98]
>>> players
[29, 58, 68, 71, 87]

>>> players = players + [90, 91, 98]
>>> players
[29, 58, 68, 71, 87, 90, 91, 98]

>>> players.append(100)
>>> players
[29, 58, 68, 71, 87, 90, 91, 98, 100]

>>> players[:2]
[29, 58]
>>> players[:2] = [0, 0]
>>> players
[0, 0, 68, 71, 87, 90, 91, 98, 100]

>>> # Removing items from the list
>>> players[:2] = []
>>> players
[68, 71, 87, 90, 91, 98, 100]
>>> # Delete all items from the list
>>> players[:] = []
>>> players
[]
>>> 