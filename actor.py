from income import Income
from education import Education

class Actor:

    def __init__(self, index, area, env):
      self.env = env

      self.index = index
      self.area = area

      self.income = Income.income_60_120
      self.education = Education.get_education_level()

      self.destination = [0, 0]

      self.event = env.event()

      print('self.Education = %d' %(self.education))

    def get_event(self):
      return self.event

    def create_event(self):
      self.event = self.env.event()

    def process_event(self):
      # for i in range(10):
      while True:
        print 'Waiting for actor %d event..........' %self.index
        yield self.event
        print 'EVENT PROCESSED for actor %d' %self.index

    def check_move(self):
      self.env.timeout(3)
      if True:
        self.move_env.succeed()

    def move(self, new_area):
      self.area.population -= 1
      self.area = new_area
      self.area.population += 1

    def get_area(self):
      return self.area



    #calculate my housing burden: percent of my income spent toward house payment(rent or own)
    def burden(self, area_cell):
      return (area_cell.avg_housing_price / 30) / self.income

    # method returns true if actor should move based on rules
    def should_i_move(self, area_cell):
      i_move = False # I like status quo
      # if # of ppl in my area with the same level of education of higher (combined) is less than 50%, I move
      if(area_cell.get_similar_education_ratio(self.education) < 50):
        i_move = True

      # if burden in my area is > 30%, then I move
      if(self.burden(area_cell) > 30):
        i_move = True

      return i_move

    # returns an area cell where a person would like to move
    def where_i_move(self, area_cells):
      attractive_areas = []
      # get a sorted list of areas where a person can move
      for cell in area_cells:
        if cell.citizens.length - cell.max_capacity: # filter by enough capacity
          if cell.get_similar_education_ratio(self.education) >= 50: # filter if we have enough ppl with the similar education level
            attractive_areas.append(cell)

      return sorted(attractive_areas, key=lambda cell: self.score_area(cell))

    # calculate attractiveness score for the particular area
    def score_area(self, area_cell):
      return Actor.decision_weights['housing_price'] * area_cell.avg_housing_price
      + Actor.decision_weights['opportunity_distance'] * Area.distance(self.my_area, area_cell)


