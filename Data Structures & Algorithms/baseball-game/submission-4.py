class Solution:
    def calPoints(self, ops: List[str]) -> int:
        rec = []
        for i in range(len(ops)):
            if ops[i] == "C":
                rec.pop()
            elif ops[i] == "D":
                rec.append(2 * int(rec[-1]))
            elif ops[i] == "+":
                n = int(rec[-1]) + int(rec[-2])
                rec.append(n)
            else:
                rec.append(int(ops[i]))
        return sum(rec)