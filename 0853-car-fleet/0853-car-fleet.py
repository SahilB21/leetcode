class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed))
        times = []
        ans = 0
        for p, s in cars:
            time = float(target - p) / s
            times.append(time)
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]:
                ans += 1
            else:
                times[-1] = lead
        return ans + len(times)