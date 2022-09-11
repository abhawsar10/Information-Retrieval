import json
import csv

# Opening JSON file
f1 = open('Google_Result2.json')
f2 = open('my_res.json')

google_res = json.load(f1)
my_res = json.load(f2)
 
f1.close()
f2.close()
 
q_results_dict={}

for q in my_res.keys():

	print("q=",q)

	matches=0
	d_sq_sum=0

	for my_link in my_res[q]: 

	
		for g_link in google_res[q]:

			# my_l=my_link
			# g_l = g_link

			my_l = my_link.split('//')[1]	
			if my_l[-1]=='/':
				my_l = my_l[:-1]
			if "www." in my_l:
				my_l = my_l.split('ww.')[1]


			g_l = g_link.split('//')[1]
			if g_l[-1]=='/':
				g_l = g_l[:-1]
			if "www." in g_l:
				g_l = g_l.split('ww.')[1]

			if g_l == my_l:
				matches+=1
				r1 = google_res[q].index(g_link) 
				r2 = my_res[q].index(my_link)
				d = r1 - r2
				print("matched: ",r1,r2)
				d_sq_sum += d**2

	if matches == 0:
		rho = 0
	elif matches == 1:
		if r1 == r2:
			rho = 1
		else:
			rho = 0
	else:
		rho = 1 - (6*d_sq_sum)/(matches**3 - matches)
	
	print("matches= ",matches)
	print("rho= ",rho)
	print("-------------------------------")
	q_results_dict[q] = [matches, matches*100/len(google_res[q]), rho]


f3 = open('hw1.csv', 'w',newline='')

writer = csv.writer(f3)
writer.writerow(["Queries","Number of Overlapping Results","Percent Overlap","Spearman Coefficient"])	

i=1
sum1=0
sum2=0
sum3=0
for q in q_results_dict.keys():

	writer.writerow(["Query "+str(i), q_results_dict[q][0], q_results_dict[q][1], q_results_dict[q][2] ])
	sum1 += q_results_dict[q][0]
	sum2 += q_results_dict[q][1]
	sum3 += q_results_dict[q][2]
	i+=1

i-=1
writer.writerow(["Averages", sum1/i, sum2/i, sum3/i])
f3.close()



# print(q_results_dict)

