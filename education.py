from enum import Enum

import random

class Education(Enum):
  none = 0
  high_school = 1
  college = 2
  graduate = 3
  education_length = 4

  @staticmethod

  def get_education_level():
    education_list = [Education.none] * 20 + [Education.high_school] * 30 + [Education.college] * 30 + [Education.graduate] * 20
    return random.choice(education_list)
