# Problem:------>find all the position of a given pattern in a given string

inputString = """Wye with Hinxhill is a hillside civil parish in the borough of Ashford northeast of Ashford, Kent itself,
centred 3.7 miles (6.0 km) NNE of the town centre.
The North Downs range of hills has a high escarpment on the east and west borders of the village,
flanking a gap caused by the River Great Stour in the centre of the parish.
The combined village has a relatively low population and a large geographical area.
The civil parish council meets monthly to administer local government resources, funding, and planning community events and facilities.
It contains the main village of Wye and the much smaller Hinxhill and had a combined population of 2,300 in 2001.
By the time of the 2011 Census, the population had reduced to 2,282."""
inputString = inputString.lower()
pat = 'th'
result = []
for i in range(0,len(inputString)):
  if inputString[i] == pat[0]:
    match = True
    for j in range(0,len(pat)):
      if inputString[i+j] != pat[j]:
        match = False
        break
    if match == True:
      result.append([i,i+len(pat)])

print(result)
