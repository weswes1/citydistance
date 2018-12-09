

# Kuala Limpur and Nairobi Kenya
import math, requests;



# 3.1390N, 101.6869E ---> (latitude, longitude) -----> (3.139,101.6869)
# 1.2921S, 36.8219E ---> (latitude, longitude) -----> (-1.2921,36.8219)

# West -
# East +
# North +
# South -

def distanceBetween():

	URL='https://maps.googleapis.com/maps/api/geocode/json?parameters'

	addresses=[0,0]
	addresses[0] = "Nairobi, Kenya"
	addresses[1] = "Algiers, Algeria"


	parameters1 = {
		'address': addresses[0],
		'key': 'NONE'
	}

	parameters2 = {
		'address': addresses[1],
		'key': 'NONE'
	}

	response1 = requests.get(URL, params = parameters1);
	response2 = requests.get(URL, params = parameters2);

	print(response1.status_code)
	print(response2.status_code)

	print(response1.content)
	print(response2.content)

def toRadians(coordinates):
	for i in range(0,2):
		coordinates[i]=math.radians(coordinates[i]);

def getDistance(coordinatesA,coordinatesB):
	toRadians(coordinatesA);
	toRadians(coordinatesB);
	deltaSigma = math.acos(math.sin(coordinatesA[0])*math.sin(coordinatesB[0])+math.cos(coordinatesA[0])*math.cos(coordinatesB[0])*math.cos(abs(coordinatesB[1]-coordinatesA[1])));
	return 6371*deltaSigma;


distanceBetween()

#print(getDistance([3.139,101.6869],[-1.2921,36.8219]));

