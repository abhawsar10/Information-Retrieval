from collections import defaultdict
import matplotlib.pyplot as plt

filePath = "se_comp.csv"


qdict ={}
qdict["Cannes"] = {"lucene" : [], "pagerank":[] }
qdict["Congress"] = {"lucene" : [], "pagerank":[] }
qdict["Democrats"] = {"lucene" : [], "pagerank":[] }
qdict["Patriot Movement"] = {"lucene" : [], "pagerank":[] }
qdict["Republicans"] = {"lucene" : [], "pagerank":[] }
qdict["Senate"] = {"lucene" : [], "pagerank":[] }
qdict["Olympics 2020"] = {"lucene" : [], "pagerank":[] }
qdict["Stock"] = {"lucene" : [], "pagerank":[] }
qdict["Virus"] = {"lucene" : [], "pagerank":[] }

with open(filePath, "r") as file:
    for line in file:
        record = line.split(',')
        query, lucene, pagerank = record[0], record[1], record[2] 
        # print(query,lucene,pagerank)

        if query == "ï»¿":
            continue

        qdict[query]["lucene"].append(lucene)
        qdict[query]["pagerank"].append(pagerank)


file.close()


# print(qdict)

overlap = {}

for q in qdict.keys():
    
    overlap[q]=0

    for i,llink in enumerate(qdict[q]["lucene"]):

        count = 0
        for j,prlink in enumerate(qdict[q]["pagerank"]):

            if llink.strip() == prlink.strip():
                count +=1
                print("overlap=",q,llink)
                print(i+1)
                print(j+1)

                overlap[q]+=1



print(overlap)

plt.bar(list(overlap.keys()), list(overlap.values()), align='center')
plt.xlabel("Query")
plt.ylabel("Number of Overlaps")

plt.show()



