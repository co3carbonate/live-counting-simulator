import json;

import live;
import markov;
from send_update import send_update;

# Received request from WebSocket
def websocket_message(ws, message):
	"Executed when a request is received from the server"
	request = json.loads(message);

	# Only care about request_type 'update' (when an update is sent)
	if request['type'] != 'update': return;

	# Setup variables
	data = request['payload']['data']; # {body, stricken, author, created, etc.}
	body = data['body'];

	# Check for commands
	if data['author'] != 'livecount_simulator':
		# 'simulator'
		if 'simulator' in body:
			send_update(markov.generate());
			print('/u/' +data['author']+ ' used "simulator"');
