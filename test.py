# ######문제 1##############################
# def solution(grid):
#     answer = []
#     for i in range(1, 6):
#         if i % 2 == 1:
#             answer.append(max(grid[i-1]))
#         else:
#             answer.append(min(grid[i-1]))
#     return answer

# # 예시 그리드
# grid = [
#     [1, 20, 28, 29, 4],
#     [2, 26, 10, 48, 27],
#     [3, 25, 19, 38, 25],
#     [4, 35, 11, 36, 5],
#     [5, 12, 40, 24, 33]
# ]

# # 함수 호출 및 결과 출력
# ret = solution(grid)
# print("solution 함수의 반환 값은", ret, "입니다.")
# ######문제 2##############################
# def solution(temperatures):
#     total_sales = 0
#     for temp in temperatures:
#         min_temp, max_temp = temp
#         if min_temp <= -15 and max_temp <= -5:
#             total_sales += 2000
#         else:
#             total_sales += 500
#     return total_sales

# # 예시 사용
# temperatures = [[0, 5], [-15, -5], [-16, -3], [-20, -8], [-14, -6]]
# print(solution(temperatures))  # 출력: 5500
# ######문제 3##############################
# def func_a(arr):
#     return sum(arr)

# def func_b(arr):
#     total = 0
#     for value in arr:
#         if value < 0:
#             total += value
#     return total

# def func_c(arr):
#     total = 1
#     for value in arr:
#         if value > 0:
#             total *= value
#     return total

# def solution(arr2d):
#     row_sums = []
#     for row in arr2d:
#         row_sums.append(func_a(row))
    
#     positive_product = func_c(row_sums)
#     negative_sum = func_b(row_sums)
    
#     return positive_product + negative_sum

# # 예시 사용
# arr2d = [
#     [1, 2, 3, 4, 5],
#     [1, -2, 3, -4, 5],
#     [3, 3, 3, 3, -1],
#     [5, 5, 5, 5, -5]
# ]

# print(solution(arr2d))  # 출력: 38
# ######문제 4##############################
# def time_to_seconds(time_str):
#     h, m, s = map(int, time_str.split(':'))
#     return h * 3600 + m * 60 + s

# def solution(times):
#     min_time = float('inf')
#     min_index = -1

#     for i, (start, end) in enumerate(times):
#         start_sec = time_to_seconds(start)
#         end_sec = time_to_seconds(end)
#         duration = end_sec - start_sec
        
#         if duration < min_time:
#             min_time = duration
#             min_index = i
#         elif duration == min_time and i < min_index:
#             min_index = i

#     return min_index + 1

# # 예시 사용
# times = [["22:10:05", "22:10:08"], ["22:10:08", "22:10:30"], ["21:10:10", "23:10:12"]]
# print(solution(times))  # 출력: 2

# ###########
# def func_a(arr):
#     return min(arr)

# def func_c(times):
#     answer = []
#     for x in times:
#         hour = int(x[1][0:2]) - int(x[0][0:2])
#         minute = int(x[1][3:5]) - int(x[0][3:5])
#         second = int(x[1][6:8]) - int(x[0][6:8])
#         answer.append(hour * 3600 + minute * 60 + second)
#     return answer

# def func_b(arr):
#     min_num = min(arr)
#     for i, a in enumerate(arr):
#         if min_num == a:
#             return i + 1

# def solution(times):
#     records = func_c(times)
#     answer = func_b(records)
#     return answer

# # 예시 사용
# times = [["22:10:05", "22:10:08"], ["22:10:28", "22:10:30"], ["23:10:10", "23:10:12"]]
# ret = solution(times)
# print("solution 함수의 반환 값은", ret, "입니다.")  # 출력: 2

# ###############
# ######문제 5##############################
# def solution(limit, weights):
#     total_weight = 0
#     count = 0

#     for weight in weights:
#         if total_weight + weight <= limit:
#             total_weight += weight
#             count += 1
#         else:
#             break

#     return count

# # 예시 사용
# limit = 2000
# weights = [1000, 500, 600, 100]
# print(solution(limit, weights))  # 출력: 2
# ######문제 6##############################
# def solution(foods, days):
#     # 메모이제이션을 위한 딕셔너리
#     memo = {}

#     def count_ways(current_day, last_food):
#         # 마지막 날에 도달하면 하나의 방법을 찾은 것
#         if current_day == days:
#             return 1

#         # 이미 계산한 경우 메모이제이션 활용
#         if (current_day, last_food) in memo:
#             return memo[(current_day, last_food)]

#         # 가능한 모든 음식을 시도
#         total_ways = 0
#         for food in range(foods):
#             if food != last_food:
#                 total_ways += count_ways(current_day + 1, food)

#         # 메모이제이션에 결과 저장
#         memo[(current_day, last_food)] = total_ways
#         return total_ways

#     # 첫 날은 이전에 먹은 음식이 없으므로 -1로 시작
#     return count_ways(0, -1)

# # 예시
# print(solution(4, 5))  # 출력: 324
# ######문제 7##############################
# def solution(arr):
#     max_candies = max(arr)
#     return sum(max_candies - candy for candy in arr)

# # 예시 사용
# arr = [3, 5, 6, 2, 4]
# print(solution(arr))  # 출력: 10
# ######문제 8##############################
# def solution(t):
#     times = [60, 30, 10, 5, 1]
#     count = 0
    
#     for time in times:
#         count += t // time
#         t %= time
    
#     return count

# # 예시 사용
# t = 78
# print(solution(t))  # 출력: 6
# ######문제 9##############################
# def solution(scores):
#     scores.remove(min(scores))  # 가장 낮은 점수를 하나 제거합니다.
#     return sum(scores) // len(scores)  # 나머지 점수의 평균을 계산하고 소수점 이하를 버립니다.

# # 예시 사용
# scores = [100, 90, 80, 95, 70, 81]
# print(solution(scores))  # 출력: 89
# ######문제 10##############################
# from collections import Counter

# def solution(best):
#     count = Counter(best)
#     return min(count['a'], count['b'], count['c'], count['d'], count['e'])

# # 예시 사용
# best = ["e", "c", "b", "d", "b", "a", "d", "a"]
# print(solution(best))  # 출력: 1

# n = int(input())
# for i in range(n,0,-1):
#     if i % 2 == 0:
#         print(i)