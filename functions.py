def find_spn(json):
    a = json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]['Envelope']['lowerCorner'].split()
    b = json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]['Envelope']['upperCorner'].split()
    return abs(float(a[0]) - float(b[0])), abs(float(a[1]) - float(b[1]))