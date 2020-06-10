"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    """
    # IDEA:
    - condition1: the number of '(' and ')' = n
    - condition2: #'(' > #')'

                            '('
                            /      \
                        '(('       '()'
                        /  \      /    \
                    '((('  '(()' '()('
                    /   \
                ...
    """
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        pars =[]
        if self.n ==0:
            return ['']

        def bfs( pars, par,l,r):
            if l==self.n or l==r:
                par +='('
                bfs(pars, par,l-1,r)
            elif l==0:
                for i in range(r):
                    par +=')'
                    i+=1
                pars.append(par)
            else:
                bfs(pars, par+')',l, r-1)
                bfs(pars, par+'(', l-1,r)

        bfs(pars, '', self.n,self.n)
        return pars
