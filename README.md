#Text Retrieval Python#
A collection of Python scripts with functions for Text Retrieval.

Search process:
- Users perform a *task* that has an *information need*, from which a *query* is formulated.
- A *search engine* processes textual queries and *retrieves* a *ranked* list of *documents*.
- Users obtain a *result* and may *reformulate* (refine) their query, based on *suggestions*.

##Ranking##
There are quite a few ways to match a query to a set of documents.

###Term Frequency - Inverted Document Frequency (TF-IDF)###
TF-IDF is the product of TF and IDF. A high TF-IDF means the term is related to a document.

TF or tf(t,d), can prevent bias to longer documents:
- Raw Frequency: Simply count the number of times the term/query appears in the document.
- Boolean Frequency: tf(t,d) = 1 if term in document, else tf(t,d) = 0
- Logarithmically Scaled Frequency: tf(t,d) = 1 + log f(t,d) if term in document, else tf(t,d) = 0
- Proportional Frequency: tf(t,d) = tf(t,d) / size of all terms in document
- Normalized Frequency: tf(t,d) = tf(t,d) / maximum raw frequency of any term in the document

IDF or idf(t, docs), prevents bias to common words and values unique words:
- idf(t, docs): count all documents / Boolean frequency of the term in all documents.

Example IDF. We have 20 documents. We have three words:
- a very common word, appears in all documents: IDF = 20 / 20 = 1
- a fairly common word, appears in half of the documents: IDF = 20 / 10 = 2
- a very rare word, appears in only 10% of documents: IDF = 20 / 2 = 10

####tfidf.py####
Functions:
- TF Raw
- TF Proportional
- IDF
- Very simple tokenizer

Sample output:

	Term: alice
	First 5 document tokens: ['alice', 'wunderland', '1009', 'tree', 'lane']
	Term count in document 1
	Token count in document: 6
	Number of documents: 3
	Number of documents with term: 2
	TF:         0.1666
	IDF:        1.5
	TFIDF:      0.25

##Evaluating Search Engine Results##
What makes for a good search engine? 

Mainly:
- Speed
- Size
- *Quality*

Optionally:
- Personalization
- Localization
- Customization
- Simplicity / UX
- Social
- Privacy

###Measuring Quality###
How de we assess the quality of a search engine result page (SERP)?
- Ask users and volunteers directly for feedback
- Hire SERP reviewers
- Measure user engagement (Number of clicks on result, Bounce ratio)
- A/B testing
- Multi-variate testing

Quality feedback can be binary (0 for not relevant, 1 for relevant) or non-binary (0-3 scale).

Example binary feedback for 15 results:

	[(1,1),(2,1),(3,1),(4,0),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,0),(12,1),(13,0),(14,1),(15,0)]

(Rank 1, 2, 3 are relevant, rank 4 is irrelevant, rank 5 to 10 are relevant etc.)

####rankedresultseval.py####
Functions for:
- Precision (P)
- Precision at K (PaK)
- Interpolated Precision (IP)
- Average Precision (AP)
- Recall (R)
- Cumulative Gain (CG)
- Discounted Cumulative Gain (DCG)
- Ideal Discounted Cumulative Gain (IDCG)
- Normalized Discounted Cumulative Gain (NDCG)

Sample output:

	INPUT:	[(1,1),(2,1),(3,1),(4,0),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,0),(12,1),(13,0),(14,1),(15,0)]

	P: 		[1.0, 1.0, 1.0, 0.75, 0.8, 0.83, 0.85, 0.87, 0.88, 0.9, 0.81, 0.83, 0.76, 0.78, 0.73]
	R: 		[0.09, 0.18, 0.27, 0.27, 0.36, 0.45, 0.54, 0.63, 0.72, 0.81, 0.81, 0.90, 0.90, 1.0, 1.0]
	IP: 	[1.0, 1.0, 1.0, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.83, 0.83, 0.78, 0.78, 0.73]
	AP: 	[1.0, 1.0, 1.0, 0.93, 0.90, 0.89, 0.89, 0.88, 0.88, 0.89, 0.88, 0.87, 0.87, 0.86, 0.85]
	PaK: 	0.8 // precision at 5
	CG: 	11
	DCG: 	6.69277
	IDCG: 	6.95740
	NDCG: 	0.96196

	RANK	RELEVANT?	PRECISION	RECALL		INTERPOLATED PRECISION
	1		1			1.00000		0.09091		1.00000
	2		1			1.00000		0.18182		1.00000
	3		1			1.00000		0.27273		1.00000
	4		0			0.75000		0.27273		0.90000
	5		1			0.80000		0.36364		0.90000
	6		1			0.83333		0.45455		0.90000
	7		1			0.85714		0.54545		0.90000
	8		1			0.87500		0.63636		0.90000
	9		1			0.88889		0.72727		0.90000
	10		1			0.90000		0.81818		0.90000
	11		0			0.81818		0.81818		0.83333
	12		1			0.83333		0.90909		0.83333
	13		0			0.76923		0.90909		0.78571
	14		1			0.78571		1.00000		0.78571
	15		0			0.73333		1.00000		0.73333