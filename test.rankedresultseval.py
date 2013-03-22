from rankedresultseval import *
sample_serp = [(1,1),(2,1),(3,1),(4,0),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,0),(12,1),(13,0),(14,1),(15,0)]
print "P: \n", precision(sample_serp)
print "R: \n", recall(sample_serp)
print "IP: \n", interpolated_precision(sample_serp, precision(sample_serp))
print "AP: \n", avg_precision(sample_serp, precision(sample_serp))
print "PaK: \n", precision_at_k(5, precision(sample_serp))
print "CG: \n", cumulative_gain(sample_serp)
print "DCG: \n", discounted_cumulative_gain(sample_serp)
print "IDCG: \n", ideal_discounted_cumulative_gain(sample_serp)
print "NDCG: \n", normalized_discounted_cumulative_gain(sample_serp)
show_ranked_results_evaluation(sample_serp)