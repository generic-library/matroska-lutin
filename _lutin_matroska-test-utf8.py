#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_type():
	return "BINARY"

def get_sub_type():
	return "TEST"

def get_desc():
	return "matroska test software"

def get_licence():
	return "LGPL-2.1"

def get_maintainer():
	return ["Moritz Bunkus <moritz@bunkus.org>"]


def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'matroska/test/utf8/test5.cpp'
	    ])
	my_module.compile_version("c++", 2003)
	my_module.add_module_depend('matroska')
	return my_module
