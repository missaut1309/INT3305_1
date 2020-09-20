import math

def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n - 1)

def prob(n,p,r):
	result = (factorial(n - 1)/(factorial(r - 1) * factorial(n - r))) * (p ** r) * ((1 - p) ** (n - r))
	return float(result)

def inforMesure(n,p,r):
	result = -math.log2(prob(n,p,r))
	return float(result)

def sumProb(N,p,r):
	"""
	P(n) = {n - 1}C{r - 1} * p^r * (1 - p)^(n - r)
	Tổng các xác suất là: S = p^r * (1 + p - 1)^(-r) = 1
	Vậy tổng xác suất của phân bố negbinomial = 1 
	"""
	result = 0
	i = r
	while(i <= N):
		result += prob(i,p,r)
		i += 1
	return float(result)

def approxEntropy(N,p,r):
	"""
	Xét dãy H_{N} = (-Pr(1) log Pr(1)) + (-Pr(2) log Pr(2)) + ...
    H_{N} là một dãy dương, tăng và có giới hạn là entropy của biến ngẫu nhiên negbinomial
    Do đó khi N càng lớn, hàm approxEntropy sẽ tiến đến entropy của biến ngẫu nhiên negbinomial và hàm này có thể dùng để tính xấp xỉ entropy
	"""
	result = 0
	i = r
	while (i <= N):
		result += prob(i,p,r) * inforMesure(i,p,r)
		i += 1
	return float(result)
print(approxEntropy(100,0.5,12))