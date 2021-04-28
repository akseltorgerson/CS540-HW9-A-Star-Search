import heapq

def swap(state, start, dest):
  s = state[:]
  tmp = s[start]
  s[start] = s[dest]
  s[dest] = tmp
  return s

def succ(state):
  # state is a 1D representation
  # use some interesting arithmetic to check
  v = []
  s = state[:]
  i = s.index(0)
  if((i - 3) >= 0):
    v.append(swap(s, i, i - 3))
  if((i % 3) != 2):
    v.append(swap(s, i, i + 1))
  if((i + 3) <= 8):
    v.append(swap(s, i, i + 3))
  if((i % 3) != 0):
    v.append(swap(s, i, i - 1))
  return v

def manhattan_distance(p1, p2):
  dist = abs(p1 // 3 - p2 // 3) + abs(p1 % 3 - p2 % 3)
  return dist

def distance(state):
  tot = 0
  for i in range(1,9):
    tot += manhattan_distance(i - 1, state.index(i))
  return tot

def print_succ(state):
  states = sorted(succ(state))
  for state in states:
    print(str(state) + " h=" + str(distance(state)))

def print_path(pq, visited):
  path = []
  path.append(visited[-1])
  nxt = visited[-1][2][2]
  for i in range(len(visited)):
    if(visited[len(visited) - i - 1][2][3] == nxt):
      path.append(visited[len(visited) - i - 1])
      nxt = visited[len(visited) - i - 1][2][2]
  for i in range(len(path)):
    print(str(path[len(path)-i-1][1])+" h=" + str(path[len(path)-i-1][2][1]) + " moves: " + str(path[len(path)-i- 1][2][0]))

def solve(state):
  s = state[:]
  pq = []
  visited = []
  searched = []
  heapq.heappush(pq, (distance(s), s, (0, distance(s), -1, 0)))
  ct = 1
  while len(pq)>0:
    head = heapq.heappop(pq)
    visited.append(head)
    if(distance(head[1]) == 0):
      return print_path(pq, visited)
    successors = succ(head[1])
    for suc in successors:
      if(not(suc in searched)):
        heapq.heappush(pq,(distance(suc)+head[2][0]+1,suc,(head[2][0]+1,distance(suc),head[2][3],ct)))
        searched.append(suc)
        ct += 1
  return "FAILED"

def main():
  solve([4,3,8,5,1,6,7,2,0])
  print_succ([8,7,6,5,4,3,2,1,0])
  solve([1,2,3,4,5,6,7,0,8])
  solve([8,7,6,5,4,3,2,1,0])


if __name__ == "__main__":
  main()

