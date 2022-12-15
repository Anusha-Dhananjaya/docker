import sys

def combine_arrays(a1, a2):
	a1_a2 = a1 + a2
	a1_a2.sort()
	
	return a1_a2

if __name__ == "__main__":

	a1 = eval(sys.argv[2])
	a2 = eval(sys.argv[3])

	combined_sorted_array = globals()[sys.argv[1]](a1, a2)

	print(f"array_1 = {a1}")
	print(f"array_2 = {a2}")
	print(f"combined_sorted_array = {combined_sorted_array}")
