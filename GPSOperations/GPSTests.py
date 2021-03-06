import GPSOperations.GPSLoc as loc
import GPSOperations.GPSOperations as op


class GPSTests:
    @staticmethod
    def distance_calc_test():
        new_york_lat = 40.7128
        new_york_long = -74.0060
        new_york_loc = loc.GPSLocation(new_york_lat, new_york_long)

        chicago_lat = 41.8781
        chicago_long = -87.6298
        chicago_loc = loc.GPSLocation(chicago_lat, chicago_long)

        #check distance between two known points is correct
        distance = int(op.calculate_average_distance(chicago_loc, [new_york_loc]))
        print(distance == 1144)
        assert distance == 1144
        
    @staticmethod
    def multiple_distances_test():
        new_york_lat = 40.7128
        new_york_long = -74.0060
        new_york_loc = loc.GPSLocation(new_york_lat, new_york_long)

        chicago_lat = 41.8781
        chicago_long = -87.6298
        chicago_loc = loc.GPSLocation(chicago_lat, chicago_long)  

        boston_lat = 42.3601
        boston_long = -71.0589     
        boston_loc = loc.GPSLocation(boston_lat, boston_long)

        washington_lat = 38.9072
        washington_long = -77.0369     
        washington_loc = loc.GPSLocation(washington_lat, washington_long)

        seattle_lat = 47.6062
        seattle_long = -122.3321     
        seattle_loc = loc.GPSLocation(seattle_lat, seattle_long)

        group_dist = int(op.calculate_average_distance(chicago_loc, [new_york_loc, boston_loc, washington_loc, seattle_loc]))
        print(group_dist == 1563)
        assert group_dist == 1563



def main():
    GPSTests.distance_calc_test();
    GPSTests.multiple_distances_test();

if __name__ == "__main__" : main()