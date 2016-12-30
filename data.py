import json;

print('Retrieving data');

# Data retrieval function
data = [];
def retrieve_data(file):
	if file < 0: return;
	print('\tRetrieving chat' +str(file)+ '.json');

	with open('data/chat' +str(file)+ '.json', encoding='utf8') as f:
		data.extend(json.loads(f.read()));
	print('\tSuccessfully retrieved chat' +str(file)+ '.json');

	retrieve_data(file - 1);


# Start collecting data
with open('data/lastChatFile.txt') as f:
	retrieve_data(int(f.read()));


# Process each message
for i in range(len(data)):
	data[i] = '\n'.join([x for x in data[i]['body'].split('\n') if x.strip()]);

# End
print('Successfully retrieved data');

