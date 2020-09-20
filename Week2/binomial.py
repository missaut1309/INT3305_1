import math

def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n - 1)

def prob(n,p,N):
	result = (factorial(N)/(factorial(n) * factorial(N - n)))* (p ** n) * ((1 - p) ** (N - n))
	return float(result)

def inforMeasure(n,p,N):
	result = -math.log2(prob(n,p,N))
	return float(result)

def sumProb(N,p):
	"""
	P(n) = {N}C{n}* p^n * (1-p)^(N-n)
	Tổng của dãy các xác suất là: S = (p + 1 - p)^N = 1
	Vậy tổng xác suất của phân bố binomial = 1  
	"""
	result = 0
	i = 0	
	while(i <= N):
		result += prob(i,p,N)
		i += 1
	return float(result)

def approxEntropy(N,p):
	"""
	Xét dãy H_{N} = (-Pr(1) log Pr(1)) + (-Pr(2) log Pr(2)) + ...
    H_{N} là một dãy dương, tăng và có giới hạn là entropy của biến ngẫu nhiên binomial
    Do đó khi N càng lớn, hàm approxEntropy sẽ tiến đến entropy của biến ngẫu nhiên binomial và hàm này có thể dùng để tính xấp xỉ entropy
	"""
	result = 0
	i = 0
	while (i <= N):
		result += prob(i,p,N) * inforMeasure(i,p,N)
		i += 1
	return float(result)
print(approxEntropy(100,0.5))