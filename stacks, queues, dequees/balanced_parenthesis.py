# Program for checking balanced parenthesis , useful for syntax compiler error checks
# IDEA: logic is to have a temporary stack since not only count of the parenthesis matters, but also order of the parenthesis
# temporary stack will be useful for keeping all the open parenthesis in it in order , and all other closing parenthesis
# will be useful in popping the element from stack if there is matching parenthesis otherwise return False
# Finally, if stack contains any element, then it means there is atleast some parenthesis which doesn't have closing parenthesis
# so, we can return False, otherwise if stack is empty, then we have found all matching parenthesis, return True at this point
# TIME : 0(N), SPACE : 0(N), N IS LENGTH OF STRING 

from collections import deque

# function for checking syntax for parenthesis
def isValid(s: str) -> bool:
    # NOTE : Empty string is also valid
    n = len(s)
    if not n:
        return True
    stack = deque()
    for i in range(len(s)):
        # if opening parenthesis, append it to stack
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        # if closing parenthesis
        else:
            # at this point, stack can't be empty
            if not stack:
                return False

            # pop the element , and then check
            top = stack.pop()

            if s[i] == ')':
                if top != '(':
                    return "false"
            elif s[i] == '}':
                if top != '{':
                    return "false"
            elif s[i] == ']':
                if top != '[':
                    return "false"

        return len(stack) == 0

# driver test function
if __name__ == '__main__':
    s = "(]"
    print(isValid(s))
