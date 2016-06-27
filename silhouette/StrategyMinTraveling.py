def dist_sq(a,b):
  dx = a[0]-b[0]
  dy = a[1]-b[1]
  return dx*dx+dy*dy

def findnearestpath(paths, pos, entrycircular=False):
    #print ("findnearest " ,pos,paths)
    nearestindex=0
    nearestdist=float("inf")
    for index,path in enumerate(paths):
        distance = dist_sq(pos,path[0]) # original direction
        if (nearestdist > distance):
            nearestdist = distance
            nearestindex = index
            selected = path
        distance = dist_sq(pos,path[-1]) # reverse direction
        if (nearestdist > distance):
            nearestdist = distance
            nearestindex = index
            selected = path[::-1]
        if (entrycircular & (path[0] == path[-1])):  # break up circular path. Not sure, if this saves real much time
           for i,p in enumerate(path):   # test each point in closed path
                 distance = dist_sq(pos,p)
                 if (nearestdist > distance):
                     nearestdist = distance
                     nearestindex = index
                     selected = path[i:] + path[1:i+1]
    return nearestindex,selected

# sort paths to achieve minimal traveling times
def sort(paths):
    pos=(0,0)
    sortedpaths=[]
    while (len(paths) > 0):
        i,path = findnearestpath(paths,pos)
        paths.pop(i)             # delete found index
        pos = path[-1]           # endpoint is next start point for search
        sortedpaths.append(path) # append to output list
    return sortedpaths
