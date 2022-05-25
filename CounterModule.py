#as a data scientist you often need to count items
#frequency analytics
#counter module is a go to library since the behind concept is based on dictionary
#so, easy to count as key,value
from collections import Counter
ls_dict=['stationname', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park']
name_count=Counter(ls_dict)
print(name_count)
#use most common function to extract top 1 items
print(name_count.most_common(1))
