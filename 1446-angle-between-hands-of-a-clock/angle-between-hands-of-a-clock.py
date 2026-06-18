class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m_angle = minutes * 6
        h_angle = (hour % 12) * 30 + minutes * 0.5
        diff = abs(h_angle - m_angle)
        return min(diff, 360 - diff)