#Text Retrieval Python#
A collection of Python scripts with functions for Text Retrieval

##Evaluating Search Engine Results##
What makes for a good search engine? 
- Speed
- Size
- Quality

Optionally:
- Personalized
- Localized
- Social

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