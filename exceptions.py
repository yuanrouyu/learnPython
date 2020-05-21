def getstats(class_list):
    new_stats=[]
    for elt in class_list:
        new_stats.append([elt[0],elt[1],avg(elt[1])])
    return new_stats

def avg(grades):
    try:
         return sum(grades)/len(grades)
    except ZeroDivisionError:
          print('warning:no grades data')

test_grades=[[['prter','packer'],[80.0,70.0,85.0]],[['bruce','wayne'],[100.0,80.0,74.0]],[['dead'],[]]]
print(getstats(test_grades))

def avg(grades):
    assert not len(grades)==0,'no grades data'
    return sum(grades)/len(grades)