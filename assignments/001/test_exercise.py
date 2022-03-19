# ---------------------------------------------------------------------------------------
#
# Title:       Assignment #1 Test Case
#
# Description: Program to accompany "exercise.py", which runs several unit tests to check
#              functionality of the "exercise.py" program.
#
# Usage:       python test-exercise.py
#
# ---------------------------------------------------------------------------------------

import exercise
import unittest

class TestExercise(unittest.TestCase):

  """
  Setup unit tests.
  """
  def setUp(self):
    """
    Currently nothing to set up.  We coould put some data access code here to
    retrieve seed value from an outside source, like a database.  However, for
    this exercise we'll keep it simple and inline the seed data.
    """
    pass

  """
  Clean-up for unit tests
  """
  def tearDown(self):
    """ Currently nothing to tear down. """
    pass

  """
  Tests for perms().

  TODO: Should probably add test for numbers within list and None value(s).
  """
  def test_perms_not_a_list(self):
    """ Test if input is not a list """
    self.assertEqual( exercise.perms("THISISASTRING"), 0 )

  def test_perms_empty_list(self):
    """ Test if input is empty list """
    self.assertEqual( exercise.perms([]), 0 )

  def test_perms_single_member(self):
    """ Test list with one member """
    self.assertEqual( exercise.perms([1]), 1 )

  def test_perms_multi_members_nodupes(self):
    """ Test list with multiple members but no duplicates """
    self.assertEqual( exercise.perms([ 3,1,2 ]), 6 )

  def test_perms_multi_members_dupes(self):
    """ Test list with multiple members with duplicates """
    self.assertEqual( exercise.perms([ 0,4,0,0,1,3,2,1 ]), 3360 )

  """
  Tests for calculate().

  TODO: Should probably add test for None value(s).
  """
  def test_calculate_not_a_string(self):
    """ Test if input is not a string """
    self.assertEqual( exercise.calculate([]), 0 )

  def test_calculate_empty_string(self):
    """ Test if input is empty string """
    self.assertEqual( exercise.calculate(""), 0 )

  def test_calculate_single_letter(self):
    """ Test string with one letter """
    self.assertEqual( exercise.calculate("A"), 1 )

  def test_calculate_not_valid_string(self):
    """ Test if input has invalid characters """
    self.assertEqual( exercise.calculate("Q456A"), 0 )

  def test_calculate_group_nodupes(self):
    """ Test multiple strings in same grouping with no duplicates """
    self.assertEqual( exercise.calculate("ABCD"), 1 )
    self.assertEqual( exercise.calculate("ABDC"), 2 )
    self.assertEqual( exercise.calculate("ACBD"), 3 )
    self.assertEqual( exercise.calculate("ACDB"), 4 )
    self.assertEqual( exercise.calculate("ADBC"), 5 )
    self.assertEqual( exercise.calculate("ADCB"), 6 )
    #
    self.assertEqual( exercise.calculate("BACD"), 7 )
    self.assertEqual( exercise.calculate("BADC"), 8 )
    self.assertEqual( exercise.calculate("BCAD"), 9 )
    self.assertEqual( exercise.calculate("BCDA"), 10 )
    self.assertEqual( exercise.calculate("BDAC"), 11 )
    self.assertEqual( exercise.calculate("BDCA"), 12 )
    #
    self.assertEqual( exercise.calculate("CABD"), 13 )
    self.assertEqual( exercise.calculate("CADB"), 14 )
    self.assertEqual( exercise.calculate("CBAD"), 15 )
    self.assertEqual( exercise.calculate("CBDA"), 16 )
    self.assertEqual( exercise.calculate("CDAB"), 17 )
    self.assertEqual( exercise.calculate("CDBA"), 18 )
    #
    self.assertEqual( exercise.calculate("DABC"), 19 )
    self.assertEqual( exercise.calculate("DACB"), 20 )
    self.assertEqual( exercise.calculate("DBAC"), 21 )
    self.assertEqual( exercise.calculate("DBCA"), 22 )
    self.assertEqual( exercise.calculate("DCAB"), 23 )
    self.assertEqual( exercise.calculate("DCBA"), 24 )

  def test_calculate_group_dupes(self):
    """ Test multiple strings in same grouping with duplicates """
    self.assertEqual( exercise.calculate("AABB"), 1 )
    self.assertEqual( exercise.calculate("ABAB"), 2 )
    self.assertEqual( exercise.calculate("ABBA"), 3 )
    self.assertEqual( exercise.calculate("BAAB"), 4 )
    self.assertEqual( exercise.calculate("BABA"), 5 )
    self.assertEqual( exercise.calculate("BBAA"), 6 )

  def test_calculate_extra(self):
    """ Test additional strings from exercise summary """
    self.assertEqual( exercise.calculate("QUESTION"), 24572 )
    self.assertEqual( exercise.calculate("BOOKKEEPER"), 10743 )
    self.assertEqual( exercise.calculate("BAAA"), 4 )

if __name__ == '__main__':
  unittest.main()

