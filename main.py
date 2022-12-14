#p.92 큰수의 법칙 #01

a = input().split()
N = int(a[0])  #배열의 크기
M = int(a[1])  #숫자가 더해지는 횟수
K = int(a[2])  #연속해서 더할수있는 횟수
print(N, M, K)
# k <= M

#배열 입력받기
b = input().split()
print(b)

#내림차순으로 정리
c = sorted(b, reverse=True)
print(c)

#전체 결과값 변수 설정
d = int()

if c[0] == c[1]: #같은 경우에는 곱해주면 
  print(int(c[0]) * M)
else:
  for i in range(M):
    if (i+1) % (K+1) != 0:
      d += int(c[0])
      i += 1
    else:
      d += int(c[1])
      i += 1
  print(d)  


# 문제 해설01. 단순하게 푸는 답안 예

# N,M,K를 공백으로 구분하여 입력받기
n,m,k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

result = 0

while True:
  for i in range(k): # 가장 큰 수를 k번 더하기
    if m == 0: # m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1
  if m == 0: # m이 0이라면 반복문 탈출
    break
  result += second # 두번째로 큰 수를 한 번 더하기
  m -= 1 # 더할 떄마다 1씩 빼기

print(result) # 최종 답안 출

# 문제 해설02. 
# N,M,K를 공백으로 구분하여 입력받기
n,m,k = map(int, input().slpit())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() #입력받은 수 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m-count) * second # 두 번째로 큰 수 더하기
print(result)

