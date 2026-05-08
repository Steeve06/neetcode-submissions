class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(OpenN,ClosedN):
            if n == OpenN == ClosedN:
                result.append("".join(stack))

            if OpenN < n:
                stack.append("(")
                backtrack(OpenN + 1, ClosedN)
                stack.pop()
            
            if ClosedN < OpenN:
                stack.append(")")
                backtrack(OpenN,ClosedN + 1)
                stack.pop()

        backtrack(0,0)
        return result


      