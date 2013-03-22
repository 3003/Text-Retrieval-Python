from math import log

# EVALUATING RANKED RESULTS WITH BINARY RELEVANCE

#Example of a ranked result with binary relevance added
#Rank		Relevant?
#1			1
#2			0
#3			1
#4			0
#5			0
#6			0
#7			1
#8			1
#9			0
#10			0
#[(1,1),(2,0),(3,1),(4,0) ... ]

# Sample of sorted ranked result set with relevance feedback -- 15 documents, their ranks and their relevance score -- 
# as a list of tuples (rank, relevance)
# sample_serp = [(1,1),(2,1),(3,1),(4,0),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,0),(12,1),(13,0),(14,1),(15,0)]

# DEALING WITH NON-BINARY RELEVANCE

# Non-binary relevance:
# Presented with a list of documents in response to a search query, an experiment 
# participant is asked to judge the relevance of each document to the query. Each 
# document is to be judged on a scale of 0-3 with 0 meaning irrelevant, 3 meaning 
# completely relevant, and 1 and 2 meaning "somewhere in between".

# Principles:
# 1. Highly relevant documents are more useful when appearing earlier in a search engine 
# result list (have higher ranks).
# 2. Highly relevant documents are more useful than marginally relevant documents, which 
# are in turn more useful than irrelevant documents.


# Returns a list of precisions for a ranked result set with relevance feedback
# precision = number of relevant documents retrieved / number of retrieved documents
# precision = True positives                         / (True positives + False positives)
# use: print precision(sample_serp)
def precision(serp):
	l = []
	nr_docs_retrieved = 0
	nr_relevant_docs_retrieved = 0
	for rank in serp:
		nr_docs_retrieved += 1
		nr_relevant_docs_retrieved += rank[1]
		l.append(nr_relevant_docs_retrieved/float(nr_docs_retrieved))
	return l

# Returns a list of recalls for a ranked result set with relevance feedback
# recall = number of relevant documents retrieved /	number of relevant documents
# recall = True positives                         / (True positives + False negatives)
# False negative = Relevant, not yet retrieved 
# Use: print recall(sample_serp)
def recall(serp):
	l = []
	nr_relevant_docs_retrieved = 0
	nr_relevant_docs = sum([rank[1] for rank in serp])
	if nr_relevant_docs == 0: #dont divide by zero
		return None
	else:
		for rank in serp:
			nr_relevant_docs_retrieved += rank[1]
			l.append(nr_relevant_docs_retrieved/float(nr_relevant_docs))
		return l

# Returns a list of interpolated precisions
# Interpolated precision at recall level r = maximum precision at any recall level equal or greater than r
# Use: print interpolated_precision(sample_serp, precision(sample_serp))
def interpolated_precision(serp, precisions = []):
	l = []
	for r in xrange(0, len(serp)):
		l.append(max(precisions[r:]))
	return l

# Returns a list of Average of Precision (AP)
# AP = 
# After each relevant document is retrieved, 
# Take the avarage of the precisions, 
# Up to and including the current level.
# Use: print avg_precision(sample_serp, precision(sample_serp))
def avg_precision(serp, precisions = []):
	avg_precisions = []
	for r in xrange(1, len(serp)+1):
		avg_precisions.append(sum(precisions[:r])/float(r))
	return avg_precisions

# Returns a float with the precision after K documents have been retrieved
# Use: print precision_at_k(5, precision(sample_serp))
def precision_at_k(k, precisions):
	try:
		return precisions[k-1] 	# K starts at 1, list index starts at 0
	except:
		return None

# Returns the integer Cumulative Gain (CG) for a ranked result set with relevance feedback
# Cumulative gain is the sum of the graded relevance values of all results in a search result list
# Note: Doesn't take into account the order of relevant results
# Use: print cumulative_gain(sample_serp)
def cumulative_gain(serp):
	cg = 0
	for rank_rel in serp:
		cg += rank_rel[1]
	return cg

# Returns the float Discounted Cumulative Gain (DCG) for a ranked result set with relevance feedback
# Principles:
# 1. Highly relevant documents appearing lower in a search result list should be penalized.
# 2. The graded relevance value is reduced logarithmically proportional to the position of the result.
# Use: print discounted_cumulative_gain(sample_serp)
# Todo: Adapted Discounted Cumulative Gain from the Yahoo ranking challenge gives better results for non-binary relevance?
def discounted_cumulative_gain(serp):
	return sum([g/log(i+2) for (i,g) in enumerate([rank[1] for rank in serp])])

# Returns a float with the Ideal Discounted Cumulative Gain (IDCG) for a ranked result set with relevance feedback
# IDCG = DCG on monotonically decreasing sort of the relevance judgments
# Use: print ideal_discounted_cumulative_gain(sample_serp)
def ideal_discounted_cumulative_gain(serp):
	return sum([g/log(i+2) for (i,g) in enumerate(sorted([rank[1] for rank in serp], reverse=True))])

# Returns a float Normalized Discounted Cumulative Gain (NDCG) for a ranked result set with relevance feedback
# NDCG = DCG / IDCG
# Use: print normalized_discounted_cumulative_gain(sample_serp)
def normalized_discounted_cumulative_gain(serp):
	return discounted_cumulative_gain(serp) / float(ideal_discounted_cumulative_gain(serp))

# Prints a table with rank, relevance, precision, recall, and interpolated 
# precision for each ranked result in a particular serp
# Use: show_ranked_results_evaluation(sample_serp)
def show_ranked_results_evaluation(serp):
	precisions = precision(serp)
	recalls = recall(serp)
	interpolated_precisions = interpolated_precision(serp, precisions)
	print "RANK\tRELEVANT?\tPRECISION\tRECALL\t\tINTERPOLATED PRECISION"
	for s, p, r, i in zip(serp, precisions, recalls, interpolated_precisions):
		fs0 = str(s[0])
		fs1 = str(s[1])
		fp = str(round(p,5)).ljust(7, '0')
		fr = str(round(r,5)).ljust(7, '0')
		fi = str(round(i,5)).ljust(7, '0')
		print fs0 + "\t" + fs1 + "\t\t" + fp + "\t\t" + fr + "\t\t" + fi;

# TODO: R-precision
# FURTHER READING
# http://www.enseignement.polytechnique.fr/informatique/profs/Michalis.Vazirgiannis/course_slides/71_text.pdf
# http://research.microsoft.com/en-us/projects/mslr/feature.aspx