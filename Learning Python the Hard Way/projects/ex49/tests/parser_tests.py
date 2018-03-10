from nose.tools import *
from parser import ParserError
import sentence, lexicon

def test_sentence_without_noun():
	tuples = [('verb', 'run'), ('direction', 'north')]
	grammar = sentence.parse_sentence(tuples)
	assert_equal(grammar.subject, 'player')
	assert_equal(grammar.verb, 'run')
	assert_equal(grammar.object, 'north')

def test_sentence_with_stop():
	tuples = [('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')]
	grammar = sentence.parse_sentence(tuples)
	assert_equal(grammar.subject, 'bear')
	assert_equal(grammar.verb, 'eat')
	assert_equal(grammar.object, 'honey')

@raises(Exception)
def test_wrong_sentence():
	tuples = [('noun', 'bear'), ('stop', 'the'), ('stop', 'the'), ('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')]
	grammar = sentence.parse_sentence(tuples)
	assert_equal(grammar.subject, 'bear')
	assert_equal(grammar.verb, 'eat')
	assert_equal(grammar.object, 'honey')