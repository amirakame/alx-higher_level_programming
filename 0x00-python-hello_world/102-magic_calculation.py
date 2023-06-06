import dis

def magic_calculation(a, b):
result = 98
result += pow(a, b)
return result
print(dis.dis(magic_calculation))
