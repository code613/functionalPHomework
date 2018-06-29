#
# Map Pattern
#
# Iterative (Non-Functional) implementation
#
def MapIter(Fnc, In):
    Out = []
    for item in In:
       Out.append(Fnc(item))
    return Out
#
# Recursive (Functional) implementation
#
def MapRec(Fnc, In):
   if In == []:
     return []
   else:
     return [Fnc(In[0])] + MapRec(Fnc, In[1:])
#
def MapTailRec(Fnc, In, Result = []):
   if In == []:
     return Result
   else:
     return MapTailRec(Fnc, In[1:], Result + [Fnc(In[0])])
#
# List Comprehension implementation
#
def MapLCompr(Fnc, In):
   return [Fnc(item)  for item in In]
#
#
# Filter Pattern
#
# Iterative (Non-Functional) implementation
#
def FilterIter(bF, In):
    Out = []
    for item in In:
       if bF(item):
         Out.append(item)
    return Out
#
# Recursive (Functional) implementation
#
def FilterRec(bF, In):
   if In == []:
     return []
   elif bF(In[0]):
     return [In[0]] + FilterRec(bF, In[1:])
   else:
     return FilterRec(bF, In[1:])
#
def FilterTailRec(bF, In, Result = []):
   if In == []:
     return Result
   elif bF(In[0]):
     return FilterTailRec(bF, In[1:], Result + [In[0]])
   else:
     return FilterTailRec(bF, In[1:], Result)
#
# List Comprehension (Functional) implementation
#
def FilterLCompr(bF, In):
   return [item  for item in In  if bF(item)]
#
#
# Map-Filter Pattern
#
# Iterative (Non-Functional) implementation
#
def mapFilterIter(bF, func, In):
    Out = []
    for item in In:
       if bF(item):
         Out.append(func(item))
    return Out
#
# Recursive (Functional) implementation
#
def mapFilterRec(bF, func, In):
   if In == []:
     return []
   elif bF(In[0]):
     return [func(In[0])] + mapFilterRec(bF, func, In[1:])
   else:
     return mapFilterRec(bF, func, In[1:])
#
def mapFilterTailRec(bF, func, In, Result = []):
   if In == []:
     return Result
   elif bF(In[0]):
     return mapFilterTailRec(bF, In[1:], Result + [func(In[0])])
   else:
     return mapFilterTailRec(bF, In[1:], Result)
#
# List Comprehension (Functional) implementation
#
def mapFilterLCompr(bF, func, In):
   return [func(item)  for item in In  if bF(item)]
#
# Reduce Pattern
#
# Iterative (Non-Functional) implementation
#
def reduceIter(Fnc, In):
   result = In[0]
   for item in In[1:]:
      result = Fnc(result, item)
   return result
#
# Recursive (Functional) implementation
#
def reduceRec(Fnc, In):
   if len(In) == 1:
     return In[0]
   else:
     return Fnc(In[0], reduceRec(Fnc, In[1:]))
#
def reduceTailRec(Fnc, In, Result = 0):
   if In == []:
     return Result
   else:
     return reduceTailRec(Fnc, In[1:], Fnc(Result, In[0]))
#