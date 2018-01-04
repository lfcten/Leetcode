class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        route_len = len(gas)
        cur = 0
        total = 0
        start = 0
        for i in range(route_len):
            cur += gas(route_len) - cost(route_len)
            total += cur
            if cur < 0:
                start = i + 1
                cur = 0
        if total >= 0:
            return start
        else:
            return -1
