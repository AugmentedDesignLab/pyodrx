import pyodrx
import numpy as np

class ThreeWayIntersection:
    def __init__(self, angles):
        self.roads = []
        self.angles = angles

    def generate(self):
        for i in range(3):
            self.roads.append(pyodrx.create_straight_road(i))
                # use this instead to change the number of lanes in the crossing
                #roads.append(pyodrx.generators.create_straight_road(i, length=100, junction=-1, n_lanes=2, lane_offset=3))
            self.angles[i] = self.angles[i]*np.pi/180


        # use this for a T-crossing instead
        #angles = [0,np.pi/2, 3*np.pi/2]

        #print(roads)
        junc = pyodrx.create_junction_roads(self.roads,self.angles,8)

        odr = pyodrx.OpenDrive('myroad')
        junction = pyodrx.create_junction(junc,1,self.roads)

        odr.add_junction(junction)
        for r in self.roads:
            odr.add_road(r)
        for j in junc:
            odr.add_road(j)

        odr.adjust_roads_and_lanes()
        odr.write_xml('three-way-intersection.xodr', True)
