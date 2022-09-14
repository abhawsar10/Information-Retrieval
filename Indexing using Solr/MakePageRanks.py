import networkx as nx

G = nx.read_edgelist("edges.txt", create_using=nx.DiGraph())

print(G)

pagerank = nx.pagerank(G, alpha=0.85, personalization = None, max_iter=30, tol=1e-06, nstart=None, weight= 'weight', dangling=None)


# with open("external_pageRankFile.txt", "w") as f:
with open("external_pageRankFile_raghav.txt", "w") as f:
    for k,v in pagerank.items():
        f.write(f"/home/raghav/Downloads/solr-7.7.3/foxnews/{k}={v}\n");
        #f.write(f"/Users/gautampranjal/Desktop/solr-7.7.3/server/solr/NYTIMES/nytimes/{k}={v}\n");