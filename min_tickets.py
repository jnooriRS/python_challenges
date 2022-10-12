from black import List


class solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        # backtracking function/ recursion
        def dfs(i):
            # tracking index in days array
            if i == len(days):
                return 0
            # base case is that if we travel 0 days we pay nothing
            if i in dp:
                return dp[i]

            dp[i] = float("inf")
            # initialize dp to operate on which will be the three known cost of tickets
            for d, c in zip([1, 7, 30], costs):
                # zip allows us to ireatre through 2 arrays simultanesouly
                # d = day pass which is first array  c= cost which is price per pass
                # i = the current day, 1,2,4,8- index position
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    # while in bounds and j is less than what day we can travel too with purchase pass
                    # days[i] + d is index plus pass so exampl index + 7 days pass
                    # will mean in [1,2,8] 8 will be out of bounds and therefore not a valid ticket pass
                    j += 1
                    # increment untill we get to index value 8
                dp[i] = min(dp[i], c + dfs(j))
                # cost of last increment- last day
            return dp[i]

        return dfs(0)
        # 0 is index of days

        # [1,2,8] example of what days in a year we travel
        # to get to any number we need to pass an index 2= 8 days
        # so we need code that will find corresponding day to index inputted
        # while loop start at day i and keep incrementing unitll we get out of bounds


# Input days = [1, 4, 6, 7, 8, 20] costs = [2,7,15]
# output 11
# day 1 you buy cost[0] = 2
# day 3 you buy cost[1] = 7
# day 20 you buy cost[0] = 2

# Explnation https://www.youtube.com/watch?v=4pY1bsBpIY4
