import requests
import concurrent.futures

class Fetcher:
	"""
	categories:cases_time_series, statewise, tested
	url:
	"""
	url = "https://api.covid19india.org/data.json"
	entry = None


	def retriever(self, categories):
		self.response = requests.get(self.url)
		self.Data = self.response.json()
		self.fetched = []
		for data in self.Data[categories]:
			self.fetched.append(data)
		return self.fetched
	def all_state(self):
		State = []		
		for data in self.retriever('statewise'):
			s =data['state']
			State.append(s)
		return State

	def confirmed(self):
		for data in self.retriever('statewise'):
			if data['state'] == self.entry:
				confirmed = data['confirmed']
				return confirmed

	def recovered(self):
		for data in self.retriever('statewise'):
			if data['state'] == self.entry:
				recovered = data['recovered']
				return recovered

	def deaths(self):
		for data in self.retriever('statewise'):
			if data['state'] == self.entry:
				death = data['deaths']
				return death

	def active(self):
		for data in self.retriever('statewise'):
			if data['state'] == self.entry:
				active = data['active']
				return active

	def lastupdate(self):
		for data in self.retriever('statewise'):
			if data['state'] == self.entry:
				lastupdate = data['lastupdatedtime']
				return lastupdate

	def state(self):
		for data in self.retriever('statewise'):
			if data['state'] == self.entry:
				state = data['state']
				return state

	def statecode(self):
		for data in self.retriever('statewise'):
			if data['state'] == self.entry:
				statecode = data['statecode']
				return statecode

	def triplet(self):

		with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
			confirmed_ = executor.submit(self.confirmed)
			recovered_ = executor.submit(self.recovered)
			deaths_ = executor.submit(self.deaths)

		

	def conclusion(self):
		with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
			first_con = executor.submit(self.confirmed) 
			second_reco = executor.submit(self.recovered) 
			third_deaths = executor.submit(self.deaths) 
			forth_active = executor.submit(self.active) 
			fifth_state = executor.submit(self.state) 
			sixth_scode = executor.submit(self.statecode) 
			seventh_lupdate = executor.submit(self.lastupdate)

			confirmed = first_con.result()
			recovered = second_reco.result()
			deaths = third_deaths.result()
			active = forth_active.result()
			state = fifth_state.result()
			statecode = sixth_scode.result()
			lastupdate = seventh_lupdate.result()

			final = f"Dated\n{lastupdate}\n{state} ({statecode})\nConfirmed: {confirmed}\nRecovered: {recovered}\nActive: {active}\nDeaths: {deaths}"
			return final

class complete:
	url = 'https://api.covid19india.org/data.json'
	f = Fetcher()
	# type is cases_time_series

	def __init__(self):
		self.type=type
		# self.date=date

	def getter(self):
		self.response = requests.get(self.url)
		self.resources = []

		for data in self.f.retriever('cases_time_series'):
			self.resources.append(data)
		return self.resources

	def date(self):
		self.Date =[]
		for dates in self.getter():
			self.Date.append(dates['date'])
		return self.Date

	def response(self, date):
		# 0-->daily confimed,...,2-->daily recovered
		# 3-->total confirmed,...,5-->total recovered

		# fomatted date
		# Date = f"{date} "

		# Retrieved Meta data
		self.cases = []
		for data in self.getter():
			if data['date'] == date:
				self.cases.append(data['dailyconfirmed'])
				self.cases.append(data['dailydeceased'])
				self.cases.append(data['dailyrecovered'])
				self.cases.append(data['totalconfirmed'])
				self.cases.append(data['totaldeceased'])
				self.cases.append(data['totalrecovered'])
		return self.cases

	# retrieving updated date for tested meta data
	def update_time(self):
		updated_at = []
		for data in self.f.retriever('tested'):
			updated_at.append(data['updatetimestamp'])
		return updated_at

	# retriving patient tested meta data
	def test(self, update_time):
		# 09/06/2020 09:00:00

		# 0-->individualstestedperconfirmedcase
		# 1-->positivecasesfromsamplesreported
		# 2-->samplereportedtoday
		# ....testpositivityrate,testsconductedbyprivatelabs,testsperconfirmedcase,testspermillion
		# 7-->totalindividualstested
		# 8-->totalpositivecases
		# 9-->totalsamplestested

		self.meta_data = []
		for data in self.f.retriever('tested'):
				if data['updatetimestamp'] == update_time:
				 self.meta_data.append(data['individualstestedperconfirmedcase'])
				 self.meta_data.append(data['positivecasesfromsamplesreported'])
				 self.meta_data.append(data['samplereportedtoday'])
				 self.meta_data.append(data['testpositivityrate'])
				 self.meta_data.append(data['testsconductedbyprivatelabs'] )
				 self.meta_data.append(data['testsperconfirmedcase'])
				 self.meta_data.append(data['testspermillion'])
				 self.meta_data.append(data['totalindividualstested'])
				 self.meta_data.append(data['totalpositivecases'])
				 self.meta_data.append(data['totalsamplestested'])

		result = f'''Dated:{update_time.split(' ')[0]}
		\nindividuals tested : {self.meta_data[0]}
		\npositive cases : {self.meta_data[1]}
		\nSample reported today:{self.meta_data[2]}
		\ntest positivity rate : {self.meta_data[3]}
		\ntests by private labs : {self.meta_data[4]}
		\ntests on confirmed cases : {self.meta_data[5]}
		\ntests per million : {self.meta_data[6]}
		\ntotal individuals tested : {self.meta_data[7]}
		\ntotal positive cases : {self.meta_data[8]}
		\ntotal samples tested : {self.meta_data[9]}'''
		return result	

class district_info:

	url = 'https://api.covid19india.org/districts_daily.json'

	def State(self):
		self.data = requests.get(self.url)
		self.response_json = self.data.json()

		# content all data about covid cases in district
		self.complete_data = []
		for content in self.response_json['districtsDaily']:
			self.complete_data.append(content)
		data_info = [self.complete_data, self.response_json]
		return data_info

    # getting name of all districts in a particulat state
	def districts(self, state):
		# creating list of all ther district in a particulat state
		self.Districts = []
		for contents in self.State()[1]['districtsDaily'][state]:
			self.Districts.append(contents)
		return self.Districts

    # for retrieving dates
	def date(self, state, districts):
		# for retriving district data
		info = []
		for content in self.State()[1]['districtsDaily'][state][districts]:
			info.append(content['date'])
		return info
    
    # for retriving data 
    # --> 'Uttar Pradesh', 'Jhansi', '2020-04-27'
	def Data(self, state, district, date):
		# retriving data for specific location and time
		for contents in self.State()[1]['districtsDaily'][state][district]:
			if contents['date'] == date:
				# custom format date
				date = date.split('-')
				new_date = '\\'.join(list(reversed(date)))

				result = f"""Dated: {new_date}
				\nActive: {contents['active']}
				\nRecovered: {contents['recovered']}
				\nConfirmed: {contents['confirmed']}
				\nDeaths: {contents['deceased']}"""
				return result
				break



if __name__ == '__main__':
	data = district_info()
	print(data.districts('Uttar Pradesh'))
	print(data.Data('Uttar Pradesh', 'Jhansi', '2020-07-01'))