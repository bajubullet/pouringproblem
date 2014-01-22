def get_states(X, Y, initial_state):
  x, y = initial_state
  # print X, Y, x, y
  result = {}
  # Fill X
  result[(X, y)] = 'Fill X'
  # Fill Y
  result[(x, Y)] = 'Fill Y'
  # Empty X
  result[(0, y)] = 'Empty X'
  # Empty Y
  result[(x, 0)] = 'Empty Y'
  # X -> Y
  new_state = transfer_water((X,x), (Y,y))
  if new_state not in result:
    result[new_state] = 'X -> Y'
  # Y -> X
  y, x = transfer_water((Y,y), (X,x))
  new_state = (x, y)
  if new_state not in result:
    result[new_state] = 'Y -> X'
  return result


def transfer_water(frm, to):
  X, x = frm
  Y, y = to
  space_left = Y - y
  if space_left > x:
    return (0, y+x)
  else:
    return (x-space_left, Y)


def solve(X, Y, goal, initial_state=(0, 0)):
  if goal in initial_state:
    return 'nothing to do'
  explored = set([initial_state])
  actions = {initial_state: 'start'}
  frontier = set([initial_state])
  while frontier:
    state = frontier.pop()
    explored.add(state)
    action = actions[state]
    for new_state, new_action in get_states(X, Y, state).items():
      if new_state not in explored and new_state not in frontier:
        new_action = action + ' >> ' + new_action
        if goal in new_state:
          return new_action
        frontier.add(new_state)
        actions[new_state] = new_action

print solve(9, 4, 3)
