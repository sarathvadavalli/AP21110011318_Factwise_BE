# If the numbers to are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

dp = [0 for i in range(1001)]
dp[1] = dp[2] = dp[6] = dp[10] = 3
dp[4] = dp[5] = dp[9] = 4
dp[3] = dp[7] = dp[8] = 5
dp[11] = dp[12] = dp[20] = 6
dp[15] = dp[16] = dp[19] = 7
dp[13] = dp[14] = dp[18] = 8
dp[17] = 9
dp[40] = dp[50] = dp[60] = dp[90] = 5
dp[30] = dp[80] = 6
dp[70] = 7

for i in range(21,100):
    if(i%10 != 0):
      qu = i//10
      dp[i] = dp[qu*10] + dp[i - qu*10]

for i in range(1, 10):
   dp[100*i] = dp[i] + 7

for i in range(101, 1000):
    if(i%100 != 0):
        qu = i//100
        num = i - qu*100
        dp[i] = dp[qu] + 10 + dp[num]

print("Sum of all numbers in words:",end = " ")
print(sum(dp))