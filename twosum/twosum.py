 def two_sum(arr,s):
  arr = list(set(arr)) #remove duplicates
  hashtable = {}
  ans = {}
  for i in arr:
    k = s - i
    if k not in hashtable:
      hashtable[i] = k
    else:
      hashtable[i] = k
      ans.append([d[k],d[i]])
  
  return ans