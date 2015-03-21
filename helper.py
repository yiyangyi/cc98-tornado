class Filters():
	"""
	Get a datetime instance object or a int() Epoch timestamp and return a pretty 
	string like 'an hour ago', 'Yesterday', '3 month ago', 'just now' etc.
	"""
	def prettify_time(self, time=False):
		if time == None:
			return time

		from datetime import datetime
		now = datetime.now()

		if type(time) is str or type(time) is unicode:
            time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        elif type(time) is int:
            diff = now - datetime.fromtimestamp(time)
        elif isinstance(time, datetime):
            diff = now - time 
        elif not time:
            diff = now - now

		day_diff = diff.days
		second_diff = diff.seconds

		if diff < 0:
			return ''

		if day_diff == 0:
			if second_diff < 20:
				return "Just now"
			if second_diff < 60:
			    return str(second_diff) + " seconds ago."
			if second_diff < 120:
			    return "One minute ago."
			if second_diff < 3600:
				return str(second_diff / 60) + " minutes ago."
			if second_diff < 7200:
				return "One hour ago."
			if second_diff < 86400:
				return str(second_diff / 3600) + " hours ago."

		if day_diff == 1:
			return "Yesterday"
		if day_diff < 7:
			return str(day_diff) + " ago."
		if day_diff < 31:
			return str(day_diff / 7) + " weeks ago."
		if day_diff < 365:
			return str(day_diff / 30) + " months ago."

		return (day_diff / 365) + " years ago."



