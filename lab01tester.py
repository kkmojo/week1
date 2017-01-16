from lab01 import RaceRegistry

if __name__ == '__main__':
	system = RaceRegistry()
	system.add_runner('Gerhard', 'Under 40 minutes')
	system.add_runner('Tom', 'Under 30 minutes')
	system.add_runner('Toni', 'Under 20 minutes')
	system.add_runner('Margot', 'Under 30 minutes')
	system.modify_runner('Gerhard', 'Under 30 minutes')

	print(system.look_up_runners_by_speed_category('Under 30 minutes'))