import time

class DGIM:
    def __init__(self , window_size):
        self.window_size = window_size
        self.buckets = []
        self.current_time = 0
    
    def add_bit(self , bit):
        self.current_time += 1

        if(bit == '1'):
            self.buckets.insert(0 , (1 , self.current_time))
            self.merge_buckets()
        self.expire_old_buckets()

    def merge_buckets(self):
        i = 0
        while i < len(self.buckets):
            count = 0
            size = self.buckets[i][0]

            same_size_indexes = []
            for j in range(len(self.buckets)):
                if self.buckets[j][0] == size:
                    same_size_indexes.append(j)

            if len(same_size_indexes) > 2:
                idx1 = same_size_indexes[-1]
                idx2 = same_size_indexes[-2]

                new_size = size*2
                new_timestamp = self.buckets[idx2][1]

                del self.buckets[idx1]
                del self.buckets[idx2 - 1]

                self.buckets.append((new_size , new_timestamp))
                self.buckets.sort(key=lambda x: -x[1])

                i = 0
            else:
                i += 1
        
    def expire_old_buckets(self):
        min_time = self.current_time - self.window_size
        self.buckets = [
            bucket for bucket in self.buckets
            if bucket[1] > min_time
        ]

    def count_last_k(self, k):
        count = 0
        boundary = self.current_time - k
        for size, timestamp in self.buckets:
            if timestamp > boundary:
                count += size
            else:
                count += size // 2
                break
        return count
    


long_stream = (
    "1101011101110101011110001110101010111101010101110111010101011101110101"
    "1101011101110101011110001110101010111101010101110111010101011101110101"
)

window_size = 100
dgim = DGIM(window_size)

# Feed stream into DGIM
for bit in long_stream:
    dgim.add_bit(bit)

# Query: count number of 1's in last 50 bits
k = 50
print("Estimated number of 1's in last", k, "bits:",
      dgim.count_last_k(k))