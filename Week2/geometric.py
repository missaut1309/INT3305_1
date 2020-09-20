import math

def prob(n,p):
	result = p * ((1 - p) ** (n - 1 ))
	return float(result)


def inforMeasure(n,p):
	result = -math.log2(prob(n,p))
	return float(result)

def sumProb(N,p):
	"""
	P(n) = p * (1-p)^(n-1)
	Tổng của dãy các xác suất với n chạy từ 1 đến vô cùng là: S =  1 - (1 - p)^N
	Từ công thức của S, dễ thấy với N->vô cùng thì S->1 (do 0<p<1)
	Vậy tổng xác suất của phân bố geometry = 1 
	"""
	result = 0
	i = 1
	while (i <= N):
		result += prob(i,p)
		i += 1 
	return float(result)

def approxEntropy(N,p):
	"""
	Entropy của nguồn thông tin: H(N) = -P(1)*log(P(1)) - P(2)*log(P(2)) + ... - P(N)*log(P(N))
	H(N) là một dãy dương, tăng và có giới hạn là entropy của BNN hình học
	Hàm approxEntropy trả về giá trị trung bình lượng tin của tất cả các symbol từ 1 đến N 
	Do đó, khi N càng lớn, hàm approxEntropy sẽ tiến đến entropy của BNN hình học


	"""
	result = 0
	i = 1
	while (i <= N):
		result += prob(i,p) * inforMeasure(i,p)
		i += 1
	return float(result)
print(approxEntropy(1000,0.5))