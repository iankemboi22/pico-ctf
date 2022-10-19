import string

msg = []

with open("message.txt") as f:
	nums = f.read().split()
	for num in nums:
		num = int(num)
		mod = num%37
		if mod<26:
			msg.append(string.ascii_uppercase[mod])
		elif mod>25 and mod<36:
			msg.append(string.digits[mod-26])
		else:
			msg.append("_")

msg = "".join(msg)	
print("picoCTF{%s}" %msg)