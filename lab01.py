class RaceRegistry:
	"""A  system for organizing a 5k running race

	=== Attributes ===
	@type runner_speed_cate: dict of {str:str}
		the key of dict is runner and the key is runner's related speed category
	"""

	def __init__(self, runner, speed):
		"""Initialize all the attributes

		@type self: RaceRegistry
		@type runner: str
			the runner's info
		@type speed: str
			the runner's speed category
		@rtype: None

		>>> system = RaceRegistry()
		>>> system.add_runner('eason' , '<30')
		>>> system.runner_speed_cate
		{'eason':'<30'} 
		"""
		self.runner_speed_cate = {}

	def __eq__(self, other):
		"""to check whether the two object are the same

		@type self: RaceRegistry
		@type other: RaceRegistry | other
			the other object we would like to compare
		@rtype: None

		>>> system1 = RaceRegistry()
		>>> system2 = RaceRegistry()
		>>> system1.add_runner('eason', '<30')
		>>> system1 == system2
		False
		"""
		if type(self) != type(other):
			return False
		else:
			for runner in self.runner_speed_cate:
				if (runner not in other.runner_speed_cate) or (
					self.runner_speed_cate[runner] != other.runner_speed_cate[runner]):
					return False

		return True 


	def __str__(self):
		"""Return a user friendly string representing the race registry system

		@type self: RaceRegistry
		@rtype: str

		>>> system = RaceRegistry()
		>>> system.add_runner('eason' , '<30')
		>>> print(system)
		eason:<30
		"""
		result += ''
		for runner in self.runner_speed_cate:
			result += '{}:{}'.format(runner, self.runner_speed_cate)
		return result

	def add_runner(self, runner, speed):
		"""Add a new runner to the system

		@type self: RaceRegistry
		@type runner: str
			the runner's info we will add to the system
		@type speed: str
			the runner's related speed
		@rtype: None

		>>> system = RaceRegistry()
		>>> system.add_runner('eason' , '<30')
		>>> system.runner_speed_cate
		{'eason':'<30'} 
		"""
		if runner not in self.runner_speed_cate:
			self.runner_speed_cate[runner] = speed

	def modify_runner(self, runner, speed):
		"""modify the exiting runner's speed category

		@type self: RaceRegistry
		@type runner: str
			the runner's info we will modify in the system
		@type speed: str
			the runner's related speed
		@rtype: None

		>>> system = RaceRegistry()
		>>> system.add_runner('eason' , '<30')
		>>> system.modify_runner('eason', '<20')
		>>> system.runner_speed_cate
		{'eason':'<20'} 
		"""
		if runner in self.runner_speed_cate:
			self.runner_speed_cate[runner] = speed

	def look_up_speed_by_runner(self, runner):
		"""Return the runner's related speed category

		@type self: RaceRegistry
		@type runner: str
			the runner we want to find its speed category
		@rtype: str

		>>> system = RaceRegistry()
		>>> system.add_runner('eason' , '<30')
		>>> system.look_up_speed_by_runner('eason')
		'<30'
		"""
		return self.runner_speed_cate[runner]

	def look_up_runners_by_speed_category(self, speed):
		"""Return the list of runners of the given speed category

		@type self: RaceRegistry
		@type email: str
			the speed category we want to find its related runners
		@rtype: [str]

		>>> system = RaceRegistry()
		>>> system.add_runner('eason' , '<30')
		>>> system.look_up_runners_by_speed_category('<30')
		['eason']
		"""
		result = []
		for runner in self.runner_speed_cate:
			if self.runner_speed_cate[runner] == speed:
				result.append(runner)
		return result