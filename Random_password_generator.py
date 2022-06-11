#import libs
import random
#asigning of chars that your password contain
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower=upper.lower()
number="1234567890"
special_char="!@#$%^&*()_+{}:>?<"
#add the four variables into an one if you want"
all=upper+lower+number+special_char
#mention pasword length based on your wish
length=8
#create password 
pw="".join(random.sample(all,length))
#print created random password
print(pw)