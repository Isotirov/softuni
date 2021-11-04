n = int(input())

matrix = []

[matrix.append([int(x) for x in input().split()]) for r in range(n)]

primary_diagonal = [matrix[r][r] for r in range(n)]
secondary_diagonal = [matrix[r][n-1-r] for r in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")