#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Simple FortiGate firewall configuration file parser
# It takes filename of FortiGate config file as an argument and it exports all "config firewall" sections with > 0 member count into separate .csv files
# © 2019 Martin Schimmer, created in free time, distriubted under GPL license, works with Python 2.7 and config files from FortiGate 5.2

from __future__ import print_function

import sys
import os
import csv

input_filename = sys.argv[1]
output_filename_base = os.path.splitext(input_filename)[0]

with open(input_filename) as input:
	while True:
		line = input.readline()
		if line == "":
			break
		s = line.strip().split(None,2)
		if len(s) == 3 and s[0].startswith("config") and s[1] == "firewall":
			section_name = s[2]
			item_param_names = []
			item_param_names_set = set()
			items = []
			while True:
				line = input.readline()
				s = line.strip().split(None,1)
				if s[0] == "edit":
					item_name = s[1]
					item_params = {}
					while True:
						line = input.readline()
						s = line.strip().split(None,2)
						if s[0] == "set" or s[0] == "unset":
							if s[0] == "set":
								if s[1] not in item_param_names_set:
									item_param_names_set.add(s[1])
									item_param_names.append(s[1])
								item_params[s[1]] = s[2]
						else:
							# s[0] should = "next" denoting end of edit section
							items.append((item_name,item_params))
							break
				else:
					# s[0] should = "end" denoting end of config section
					# here items contain list of tuples (item name, dict of item parameters)
					if len(items) == 0:
						break
					# export section
					fn = output_filename_base+"-"+section_name+".csv"
					print("Exporting "+fn+" -> ",end="")
					with open(fn, "wb") as output:
						c = csv.writer(output, delimiter=';')
						l = ["name"]+item_param_names
						c.writerow(l)
						for i in items:
							l = [i[0]]
							for p in item_param_names:
								try:
									l.append(i[1][p])
								except KeyError:
									l.append("")
							c.writerow(l)
					print("ok")	
					break
			
