#!/usr/bin/env python3

with open('fileprocessor.input', 'r') as file:
    lines = file.readlines()


user_data = []
skipped_items = []

for line in lines:
	# skip
	if line.startswith('#'):
		skipped_items.append(line.strip())
		continue
	# split
	user_info = line.strip().split(':')
	# append
	user_data.append(user_info)

print("Printing out User Data:\n")
for user_info in user_data:
	username, password, userid, groupid = user_info
	print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

for skipped_item in skipped_items:
	username = skipped_item.split(':')[0][1:]
	print(f"{username} is skipped because it starts with a hashtag (is commented out)")

print("\nEnd of User Data")
