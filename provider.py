#Assignment of variable and list creating

#In eu-west-2 provision this ami - ami- 0d729d2846a86a9e7, 

#In eu-west-1 provision this ami ami-  ami-0c1bc246476a5572b

#In, us-east-1 provision this ami ami-0022f774911c1d690

#resource = aws

ami_list =  ["0d729d2846a86a9e7", "0c1bc246476a5572b", "0022f774911c1d690"]
print(ami_list)

#for loop
ami_list = ["ami-0d729d2846a86a9e7", "ami-0c1bc246476a5572b", "ami-0022f774911c1d690"]
for ami in ami_list:
    print("instances in ami id")
    print(ami)



# Assigning a variable and creating a Tuple
regions_tuple = ("ami-0d729d2846a86a9e7", "ami-0c1bc246476a5572b", "ami-0022f774911c1d690") #tuple

for region in regions_tuple: 
    print (region)
    if region == "ami-0022f774911c1d690":
        print("us-east-1")
        
        
#  Assigning a variable and creating a dictionary
region_ami_dict = {"eu_west-2" : "ami- 0d729d2846a86a9e7", "eu-west-1" : "ami-0c1bc246476a5572b", "us-east-1" : "ami-0022f774911c1d690"}

for k, v in region_ami_dict.items():
    print(v,k)
    
    
    
# importing aws library 
import boto3

# Specify region

region = "eu-west-2"

session = boto3.Session()

# get variable resource

available_resources = session.get_available_resources()

print(available_resources)