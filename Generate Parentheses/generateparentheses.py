def generateParentheses(n: int) -> List[str]:

    def treeGen(s, op, cl):

        l = []
        r = []

        if cl == 0:
            return [s]

        if op >= 1:
            l.extend(treeGen(s + "(", op-1, cl))

        if cl >= 1 and cl > op:
            r.extend(treeGen(s + ")", op, cl-1))

        return l+r

    return treeGen("(", n-1, n)
