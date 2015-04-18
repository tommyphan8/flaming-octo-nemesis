
p = 19  #prime number
g = 3	#generator number

x = 9	#what alice chooses as her secret number
y = 8	#what bob chooses as his secret number

X1 = g**x % p 	#calculate X and sends to Bob
Y1 = g**y % p 	#calculate Y and sends to Alice

K1 = Y1**x % p 	#Alice computes the secret key as K1
K2 = X1**y % p 	#Bob computes teh secret key as K2
	
print ("Alice pics a random postive number x in Zp: "),  x
print ("Alice computes X and sends to Bob: "), X1

print ("Bob pics a random postive number y in Zp: "), y  
print ("Bob computes Y and sends to Alice: "), Y1

print ("K1: "), K1
print ("K2: "), K2

	
