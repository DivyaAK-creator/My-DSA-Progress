# Count Frequency of Elements
arr = [4, 1, 2, 2, 3, 1, 1, 2]
freq = {}
for num in arr:
    freq[num]=freq.get(num,0)+1

max_freq = max(freq.values())
answer = float("inf")# we use when we want min value

for key,value in freq.items():
    if value == max_freq:
        answer = min(answer,key)
print(answer)

# First Non-Repeating Character
s = "aabbccdexx"
freq = {}
non_reapeating=[]
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)
for ch in freq:
    if freq[ch]>1:
        print(ch)
    else:
        non_reapeating.append(ch)
print(non_reapeating)
# or(for finding first non repeated char)
# for ch in freq:
#     if freq[ch]==1:
#         print(ch)
#         break
# else:
#     print(-1)

# Group Elements by Frequency
s = "aaabbcdddd"
freq = {}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
group = {}
for key,value in freq.items():
    if value not in group:
        group[value]=[]

    group[value].append(key)
print(group)

# Merge Two Dictionaries
d1 = {"a":5, "b":2}
d2 = {"b":7, "c":1}

for key,value in d2.items():
    if key in d1:
        d1[key]= max(d1[key],value)
    else:
        d1[key]=value
print(d1)