#two tables: one with category names, one with items

import json
import os
import struct

class Database:
	def __init__(self):
		self.defaut_filename = "base.json"
		if os.path.exists(self.defaut_filename):
			with open(self.defaut_filename) as f:
				self.data = json.loads(f.read())
		else:
			self.data = {"categories" : [], "products" : []}
		self.cats = self.data["categories"]
		self.prods = self.data["products"]
	
	def get_cats(self):
		return self.cats.copy()
	
	def get_prods(self,cat):
		result = []
		for i in self.prods:
			if i["category"] == cat:
				result.append(i.copy())
		return result
	
	def add_cat(self,cat):
		if not (cat in self.cats):
			self.cats.append(cat)
		else:
			raise(ValueError, "Category already exists")
	
	def remove_cat(self,cat):
		if cat in self.cats:
			self.cats.remove(cat)
			for i in self.prods:
				if i["category"] == cat:
					self.prods.remove(i)
		else:
			raise(ValueError, "Category doesn't exist")
	
	def add_prod(self, cat, prod):
		prod[id] = self.get_new_id()
		self.prods[cat].append(prod)
	
	def remove_prod(self, id):
		for i in self.prods:
				if i["id"] == id:
					self.prods.remove(i)
	
	def get_new_id():
		success = False
		while not success:
			id = struct.unpack(">H",os.urandom(2))[0]
			success = True
			for i in prods:
				if i["id"] == id:
					success = False
		return id
	
	def commit(self):
		if os.path.exists(self.defaut_filename):
			os.path.remove(self.default_filename)
		with open(self.defaut_filename, "w") as f:
			f.write(json.dumps(self.data))