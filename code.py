 def maxPoints(self, points: List[List[int]]) -> int:
        if(len(points)<=2):
            return len(points)
        maxi=2
        for i in range(len(points)):          
            for j in range(i+1,len(points)):
                total=2
                for k in range(len(points)):
                    if(k!=i and k!=j):
                        if((points[j][1]-points[i][1])*(points[i][0]-points[k][0])== (points[i][1]-points[k][1])*(points[j][0]-points[i][0])):
                            total+=1
                maxi=max(total,maxi)
        return maxi
