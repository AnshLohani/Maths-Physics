import math 

#Defining Initial Conditions of Bodies a, b, c.
class initial_conditions:
    #Defining Initial Locations 
    def location_a(a):
        '''
        a --> list()
        a = [x1,y1,z1] --> 3D cordinates of body "a"
        
        returns a vector 'va' } nested list
        Format: va = [ [ax,i] [ay,j] [az,k] ]
        ''' 
        va = [[a[0],"i"],[a[1],"j"],[a[2],"k"]]
        return va
        

    def location_b(b):
        '''
        b --> list()
        b = [x2,y2,z2] --> 3D cordinates of body "b"
        returns a vector 'vb' } nested list
        Format: vb = [ [bx,i] [by,j] [bz,k] ]
        ''' 
        vb = [[b[0],"i"],[b[1],"j"],[b[2],"k"]]
        return vb

    def location_c(c):
        '''
        c --> list()
        c = [x3,y3,z3] --> 3D cordinates of body "c"
        returns a vector 'vc' } nested list
        Format: cb = [ [cx,i] [cy,j] [cz,k] ]
        ''' 
        vc = [[c[0],"i"],[c[1],"j"],[c[2],"k"]]
        return vc

