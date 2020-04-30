L = ["https://www.google.co.in/, https://www.yahoo.com/, https://www.linkedin.com/jafjmhfvbjHVWAFM, https://www.kuchbhi.con/kjfugajbfa\n"] 

# Writing to file 
file1 = open('URLlist.txt', 'w') 
file1.writelines(L) 
file1.close() 

# Opening file 
file1 = open('URLlist.txt', 'r') 
count = 0

# Using for loop 
print("Using for loop") 
for line in file1: 
	count += 1
	x=(line.split(', ')) 
print(x)
# Closing files 
file1.close() 

#taking url from x and getting the status code
import requests
for url in x:
    try:
        r = requests.head(url)
        print(r.url,r.status_code,r.reason)
    # prints the int of the status code.
    except requests.ConnectionError:
        print("failed to connect")    
