class Sol:
    def find_max_consecutive_ones(self, nums):
        max=0
        sum=0
        for num in nums:
            if num==1:
                sum+=1
            else:
                if sum>max:
                    max=sum
                sum=0
        if sum>max:
            max=sum
        return max
