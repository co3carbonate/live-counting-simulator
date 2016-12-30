import markovify;

from data import data;

print('Loading Markov chains');

# Variables
text = '\n'.join(data);
model = markovify.NewlineText(text);

# Generate
def generate():
	return model.make_sentence(tries=100);


print('Successfully loaded Markov chains');
