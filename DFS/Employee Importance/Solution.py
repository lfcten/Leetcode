class Solution:
    def getImportance(self, employees, id):
        emap = {e.id: e for e in employees}

        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))

        return dfs(id)

