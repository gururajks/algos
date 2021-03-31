class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1

        memo = {}
        min_schedule = math.inf

        def helper(jobDifficulty, start_idx, rem_d, curr_sum):
            nonlocal min_schedule

            if rem_d == 0 and start_idx == len(jobDifficulty):
                min_schedule = min(min_schedule, curr_sum)
                return

            if rem_d < 0 or start_idx == len(jobDifficulty):
                return

            max_diff_day = 0
            for idx in range(start_idx, len(jobDifficulty)):
                max_diff_day = max(max_diff_day, jobDifficulty[idx])
                helper(jobDifficulty, idx + 1, rem_d - 1, curr_sum + max_diff_day)

        helper(jobDifficulty, 0, d, 0)

        return min_schedule
    