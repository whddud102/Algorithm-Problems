"""
문제
0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3*3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 -> 1, 1 -> 0)

입력
첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.

예제 입력 1 
3 4
0000
0010
0000
1001
1011
1001
예제 출력 1 
2
"""

row, col = map(int, input().split())

a = []
b = []
count = 0

def flip(row, col) :
  for idx_row in range(row, row+3) :
    for idx_col in range(col, col+3) :
      a[idx_row][idx_col] = 1- a[idx_row][idx_col] 

def isSame(row, col) :
  for idx_row in range(row) :
    for idx_col in range(col) :
      if a[idx_row][idx_col] != b[idx_row][idx_col] :
        return False
  return True
      

for i in range(row) :
  input_row = list(map(int, list(input())))
  a.append(input_row)

for i in range(row) :
  input_row = list(map(int, list(input())))
  b.append(input_row)

for idx_row in range(row - 2) :
  for idx_col in range(col - 2) :
     if a[idx_row][idx_col] != b[idx_row][idx_col] :
       flip(idx_row, idx_col)
       count += 1
    

if isSame(row, col) :
  print(count)  
else :
  print(-1)       


"""
설명
- 너무 어렵게 접근한 나머지 결국 풀지 못하고 다른 블로그를 참조하여 해결하였다. (출처 : https://m.blog.naver.com/pjok1122/221652193756)
- 3 x 3 의 부분 배열에 속하는 원소를 뒤집어서 행렬 A를 행렬 B와 같게 만들 수 있는지 계산하는 문제이다.
- A, B의 (0,0)의 원소가 서로 다르다면, (0,0)을 바꾸기 위해서는 (0,0)을 부분배열의 좌측 상단에 위치시켜놓고 행렬을 뒤집는 방법 밖에 없다.
- (0,0)의 뒤집기가 수행된 후 3x3 부분배열의 좌상단 기준을 (0,1)로 옮긴다면 더 이상 (0,0)의 값은 변경할 방법이 없게 된다.
- 그 다음 (0,1)의 원소가 서로 다르다면 (0,1)을 부분배열의 좌측 상단에 위치시켜놓고 뒤집는 방법 밖에 없다.
- (0,1)의 뒤집기가 수행된 후 3x3 부분배열의 좌상단 기준을 (0,2)로 옮긴다면 더 이상 (0,1)의 값은 변경할 방법이 없게 된다.
- 이런식으로 좌측 상단부터 우측 하단까지 A의 원소를 B와 일치하는지 확인 후, 일치하지 않는다면 부분배열을 이용해 A의 원소를 뒤집어 나간다.
- 일치하지 않는 원소를 발견하면 부분배열을 이용해 3X3 영역을 뒤집고, 일치하는 원소를 발견하면 뒤집지 않고 다음 원소로 넘어간다.
- 모든 원소에 대해서 뒤집기를 수행 후, 최종 결과가 A,B 행렬이 일치하는 경우 뒤집기를 수행한 횟수를 반환한다.
- 최종 결과가 A,B 행렬이 일치하지 않는 경우, -1을 반환한다.
"""

