class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+/-*" : 
                return int(token)
            else:
                right = dfs()
                left = dfs()

                if token == "+":
                    return left + right
                elif token == "-":
                    return left - right
                elif token == "*":
                    return left * right
                elif token == "/":
                    return int(left/right)

        return dfs()