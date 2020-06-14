

def isvalid(s):

  opeaning_bracket= "([{"
  closing_bracket = ")]}"
  matching_bracket={ "}":"{","]":"[", ")":"("  }

  stack=[]

  for i in s:
    if i in opeaning_bracket:
      stack.append(i)
    elif i in closing_bracket:
      if len(stack)==0:
        return False
      elif stack[-1] == matching_bracket[i]:
        stack.pop()
      else:
        return False
  return len(stack)==0
