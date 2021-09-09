n, m = map(int, input().split())
s = []
def f(k):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n+1):
    if i < k:
      continue
    s.append(i)
    f(i)     # 재귀
    s.pop()

f(1)