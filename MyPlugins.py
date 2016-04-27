import sublime, sublime_plugin  
class valuesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print("START")
		self.documentFormatter(edit)
		print(self.insertQuotes(edit))
		print("FINISHED")
	def insertQuotes(self, edit):
		result = ""
		markers = []
		selections = self.view.find_all("^(.*)\n?", 0, "$1", markers)
		selections = zip(*[iter(selections)] * 19)
		markers = zip(*[iter(markers)] * 19)
		for x in range(0, len(selections)):
			selection_row = selections[x]
			result += "("
			marker_row = markers[x]
			for y in range(0, len(selection_row)):
				region = selection_row[y]
				marker = marker_row[y]
				if marker.strip(" "):
					replacement_text = marker
					if marker.strip(" ") != "null":
						replacement_text = "\"" + marker + "\""
					if (y+1) < len(selection_row):
						replacement_text = replacement_text + ", "
					result += replacement_text;
					#self.view.replace(edit, region, replacement_text)
			result += ")"
			if(x+1) < len(selections):
				result += ",\n "
		return result
	def documentFormatter(self, edit):
		selection = self.view.find_all("^\n")
		for region in reversed(selection):
			self.view.replace(edit, region, "")
class createCommand(sublime_plugin.TextCommand):			
	def run(self, edit):
		print("START")
		self.containerFormatter(edit)
		self.splitLines(edit)
		self.termsFormatter(edit)
		print("FINISHED")
	def containerFormatter(self, edit):
		markers = []
		selection = self.view.find_all("^create table (.*?) \(", 0, "create table `smc_portal`.`$1`\n(", markers)
		for x in reversed(range(0, len(selection))):
			region = selection[x]
			replacement_text = markers[x]
			self.view.replace(edit, region, replacement_text)
	def splitLines(self, edit):
		markers = []
		selection = self.view.find_all(",(\n)?", 0, ", \n", markers)
		for x in reversed(range(0, len(selection))):
			region = selection[x]
			replacement_text = markers[x]
			self.view.replace(edit, region, replacement_text)
	def termsFormatter(self, edit):
		selection = self.view.find_all("VARCHAR2")
		for region in reversed(selection):
			self.view.replace(edit, region, "VARCHAR")
