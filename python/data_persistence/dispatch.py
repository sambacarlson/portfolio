import datas
import pickle


def savePs(filename, data):
	with open(filename, 'wb') as f:
		pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
		return True

def loadPs(filename):
	with open(filename, 'rb') as f:
		saved = pickle.load(f)
	return saved

# def loadDefaults(data):
# 	return

try: 
	prefs = loadPs()
except FileNotFoundError:
	savePs()
	prefs = loadPs()


# print("here are your default preferences: {}\n".format(datas.preferences))
# print("here are your saved preferences: {}\n".format(prefs))
# datas.preferences['name'] = input("enter your name: ")
# savePs()
# print("preferences are saved reload program and see changes maitained")

