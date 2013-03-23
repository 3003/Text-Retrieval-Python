from math import log

# Returns list of word tokens for a string
# Simple tokenizer for illustration purposes only
# Check out NLTK.word_tokenize()
def simple_tokenizer(document):
	return document.lower().split(None)

# Returns integer Term Count for a document
# tc = count number of term occurence in document
def term_count(term, document_tokens):
	return document_tokens.count(term.lower())

# Returns integer with total number of tokens in a document
# toc = count number of tokens in a document
def token_count(document_tokens):
	return len(document_tokens)

# Returns float term frequency (TF), 
# normalized for document size
# tf = term count / token count 
def term_frequency(term, document_tokens):
	return term_count(term, document_tokens) / float(token_count(document_tokens))

# Returns the number of documents containing the term
# from a list of document tokens
def nr_docs_with_term(term, document_tokens_list):
	nr = 0
	for document_tokens in document_tokens_list:
		if term_count(term, document_tokens) > 0:
			nr += 1
	return nr
	
# Returns the float Inverse Document Frequency  (IDF)
# normalized to reduce non-unique/common words that appear in many documents
def inverse_document_frequency(term, document_tokens_list):
	return len(document_tokens_list) / float(nr_docs_with_term(term, document_tokens_list))

# Returns the float Term Frequency - Inverse Document Frequency or tf-idf
def tf_idf(term, document_tokens, document_tokens_list):
	return term_frequency(term, document_tokens) * inverse_document_frequency(term, document_tokens_list)

# prints a rapport of all related values
def tf_idf_rapport(term, document_tokens, document_tokens_list):
	print "Term:", term
	print "Number of documents:", len(document_tokens_list)
	print "First 5 document tokens:", document_tokens[:5]
	print "Term count in document", term_count(term, document_tokens)
	print "Token count in document:", token_count(document_tokens)
	print "Number of documents with term:", nr_docs_with_term(term, document_tokens_list)
	print "TF:\t\t", term_frequency(term, document_tokens)
	print "IDF:\t\t", inverse_document_frequency(term, document_tokens_list)
	print "TF--IDF:\t",tf_idf(term, document_tokens, document_tokens_list)

# Simple sample usage
term = "alice"	
document_tokens1 = simple_tokenizer("This is a test document about living next door to Jane.")
document_tokens2 = simple_tokenizer("This is another alice document that is larger and also talks about Alice.")
document_tokens3 = simple_tokenizer("Alice Wunderland 1009 Tree Lane Kansas.")
document_tokens_list = [document_tokens1, document_tokens2, document_tokens3]

tf_idf_rapport(term, document_tokens3, document_tokens_list)