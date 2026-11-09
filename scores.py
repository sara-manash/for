scores = [78,92,65,88,100,54,91,73]
total = 0
for score in scores:
    total = total + score
    print(f"total: {total}")

average = total / len(scores)
print(f"(average): {average}")

count_90 = 0
for score in scores:
   if score >= 90:
      count_90 = count_90 + 1
print(f"count of scores >= 90: {count_90}")

# max score
for score in scores:
    if score == max(scores):
        print(f"max score: {score}")
        

