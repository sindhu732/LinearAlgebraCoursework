import numpy as np

countries = np.loadtxt('UN_voting_data.txt',dtype=np.str, usecols=[0])
#print countries

un_voting_data = np.loadtxt('UN_voting_data.txt',dtype=np.str)
A = un_voting_data[:, 1:]
A = A.astype(np.int)

M = np.dot(A,A.transpose())
print "M = A'A \nM =", M

m = M.min(0)
minimums = np.sort(m)[0:10]
#print minimums
most_opposed = []
for h in range(0,len(minimums)):
    for i in range(0,len(countries)):
        for j in range(0,len(countries)):
            if M[i,j]==minimums[h]:
                #print M[i,j],i,j
                #print countries[i], countries[j]
                if h==0:
                    h = h+1
                    most_opposed.append([countries[i], countries[j]])
                elif (most_opposed[h-1][0] != countries[j] and most_opposed[h-1][1]!=countries[i]):
                        most_opposed.append([countries[i], countries[j]])
                
print "Most opposed countries are ", most_opposed[0][0], " and ", most_opposed[0][1]
print "The ten most opposed are :", most_opposed 

n = M.max(0)
maximums = np.sort(n)
#print maximums
most_agreeable = []
for h in range(0,10):
    for i in range(0,countries.size):
        for j in range(0,countries.size):
            if i != j:
                if M[i,j]==maximums[h]:
                    most_agreeable.append([countries[i], countries[j]])
                    
print "Most agreeable countries are ", most_agreeable[-1][0], " and ", most_agreeable[-1][1]
