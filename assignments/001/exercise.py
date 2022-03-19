# ---------------------------------------------------------------------------------------
#
# Title:       Assignment #1
#
# Description: Program to calculate the permutation of a given string with some limited
#              requirements, such as the passed string must only contain the first 25
#              uppercase English letters.
# 
# Usage:       python exercise.py <string>
# 
# Examples:    python exercise.py AAAB
#              python exercise.py ABCDEFGH
#              python exercise.py QUESTION
# 
# ---------------------------------------------------------------------------------------

import sys


# Since the requirements include a max boundary, we can predefine all of the
# applicable factorials (via an indexed array) instead of spending valuable
# clock cycles recalculating each time.

factorial = [
    1,				#  0!
    1,				#  1!
    2,				#  2!
    6,				#  3!
    24,				#  4!
    120,			#  5!
    720,			#  6!
    5040,			#  7!
    40320,			#  8!
    362880,			#  9!
    3628800,			#  10!
    39916800,			#  11!
    479001600,			#  12!
    6227020800,			#  13!
    87178291200,		#  14!
    1307674368000,		#  15!
    20922789888000,		#  16!
    355687428096000,		#  17!
    6402373705728000,		#  18!
    121645100408832000,		#  19!
    2432902008176640000,	#  20!
    51090942171709440000,	#  21!
    1124000727777607680000,	#  22!
    25852016738884976640000,	#  23!
    620448401733239439360000,	#  24!
    15511210043330985984000000	#  25!
]


# Custom permutation generator written specifically for this exercise to
# take advantage of an indexed factorial array.  Note: Since this method
# is called at only one place in calculate(), we could inline it in that
# method and (possibly) save a couple more clock ticks.

def perms(nval):
  #import collections  (see note above)
  # check if a list
  if type(nval) is not list:
    return 0

  # return len if its 0/1
  nval_len = len(nval)
  if nval_len<2:
    return nval_len

  # get counts of all duplicate (i.e., count>1) items and put in a list
  r = [ nval.count(x) for x in list(set(nval)) if nval.count(x)>1 ]
  #r = [y for x, y in collections.Counter(nval).items() if y > 1]

  # calculate the divisor for the permutation with the list of counts
  bot = 1
  for i in range(len(r)):
    n = r[i]
    bot *= factorial[n]

  return factorial[nval_len]/bot


# Custom method to caclulate the permutation of a string (with constraints).

def calculate(s):
  # check if a string
  if type(s) is not str:
    return 0

  # check if valid range
  s_len = len(s)
  if s_len<1 or s_len>25:
    return 0

  # Check if string contains all uppercase letters.  Note: If there was not a
  # requirement for just upperclass letters, this code could be removed, which
  # would result in MORE flexibility.  (-:
  s_listset = list(set(s))
  if len([ u for u in s_listset if not u.isupper() ]) > 0:
    return 0

  # Get sorted list of unique letters and bail if it reduces to just one value.
  # This will capture scenarios where a string is passed with one letter or a
  # mult-letter string with the same letter repeated.
  s_unique = sorted(s_listset)
  if len(s_unique) == 1:
    return 1

  # Convert original string into list with sequential indexed integers.
  # For example:
  #   "FADED" ... converts to ... [ 3,0,1,2,1 ]
  # Since: A=0, D=1, E=2, F=3
  nval = [ s_unique.index(c) for c in list(s) ]

  total = 1

  while True:

    # loop to process all preceding permutations
    for j in range( nval[0] ):

      # flip applicable index
      t_idx = nval.index(j)
      nval[t_idx] = nval[0]

      # accumalate permutations
      total += perms(nval[1:])

      # restore index
      nval[t_idx] = j

    # stop if we'll only have one value remaining after the del in next step
    if len(nval)<=2:
      break

    # drop first value
    del nval[0]

    # reindex shortened list
    q = sorted(list(set(nval)))
    v = [ q.index(c) for c in nval ]
    nval = v

  return total


if __name__ == '__main__':
  if len(sys.argv)==2:
    count = calculate(sys.argv[1])
    if count>0:
      print(sys.argv[1],"=",count)

