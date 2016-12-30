# Global variables
import praw;

# Reddit API (PRAW)
# User authentication
reddit = praw.Reddit(
	client_id = '',
	client_secret = '',
	username = '',
	password = '',
	user_agent = ''
);

# Live thread information
thread = 'y3cd0w6bhz8m';

# WebSocket
ws = None;
