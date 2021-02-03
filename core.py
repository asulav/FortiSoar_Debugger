from jinja2 import Template
import sys
import json

def load_data(path):
	try:
		with open(path, 'r') as file:
			json_vars = json.load(file)
		return json_vars
	except Exception as e:
		raise(e)

def load_syntax(path):
	try:
		with open(path, 'r') as file:
			syntax = file.read()
		return syntax
	except Exception as e:
		raise(e)

def core(json_vars, syntax):
	core_string = f"{syntax}"
	template = Template(core_string)
	ret =  template.render(json_vars)
	return ret

def main():
	if len(sys.argv) < 2:
		sys.argv.append('data.json')
		sys.argv.append('syntax')		
	elif len(sys.argv) < 3:
		sys.argv.append('syntax')

	data_path = sys.argv[1]
	syntax_path = sys.argv[2]

	data = load_data(data_path)
	syntax = load_syntax(syntax_path)

	ret = core(data,syntax)
	print(ret)

if __name__ == "__main__":
	main()