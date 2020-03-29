players = [29, 58, 66, 71, 87]
print(players[2]) #66

players[2] = 68
print(players) #[29, 58, 68, 71, 87]

print(players + [90, 91, 98]) #[29, 58, 68, 71, 87, 90, 91, 98]

# the original list was not changed
print(players) #[29, 58, 68, 71, 87]

# Changing the original list
players = players + [90, 91, 98]
print(players) # [29, 58, 68, 71, 87, 90, 91, 98]

# Changing (appending) the list
players.append(100)
print(players) # [29, 58, 68, 71, 87, 90, 91, 98, 100]

print(players[:2]) # [29, 58]

# Changing multiple values in the list
players[:2] = [0, 0]
print(players) # [0, 0, 68, 71, 87, 90, 91, 98, 100]

# Removing items from the list
players[:2] = []
print(players) # [68, 71, 87, 90, 91, 98, 100]

# Delete all items from the list
players[:] = []
print(players) # []
