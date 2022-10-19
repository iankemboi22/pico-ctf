import string

msg = []

with open("message.txt") as f:
	nums = f.read().split()
	for num in nums:
		num = int(num)
		res = pow(num, -1, 41)
		if res in range(0,27):
			msg.append(string.ascii_uppercase[res-1])
		elif res in range(27,37):
			msg.append(string.digits[res-27])
		else:
			msg.append("_")

msg = "".join(msg)
print("picoCTF{%s}" %msg)
