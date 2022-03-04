#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy


from sensor_msgs.msg import LaserScan


class ObstacleAvoidance():

    def __init__(self):
        
        rospy.init_node('obstacle')
        
        rospy.Subscriber('scan', LaserScan, self.scan)

        
        self.PositionEnd = [-4, 46.020]
        self.error = 1
        self.stopped = False
        
        rospy.spin()


    def scan(self, laser):
        

        state_area = ''
    
        area = {
            'right':  min(min(laser.ranges[0:268]), 10),
            'front':  min(min(laser.ranges[269:450]), 10),
            'left':   min(min(laser.ranges[451:719]), 10), #laser lidar a une range de 720
        } #A MODIFIER !!!!
        
        if not self.stopped:
        
            if area['front'] > 0.2 and area['left'] > 0.2 and area['right'] > 0.2:
                state_area = 'case 1 - no obstacle'
                
            elif area['front'] < 0.2 and area['left'] < 0.2 and area['right'] > 0.2:
                state_area = 'case 2 - obstacle in front/left'
                
            elif area['front'] < 0.2 and area['left'] > 0.2 and area['right'] < 0.2:
                state_area = 'case 3 - obstacle in front/right'
                
            elif area['front'] > 0.2 and area['left'] > 0.2 and area['right'] < 0.2:
                state_area = 'case 4 - obstacle in right'
                
            elif area['front'] > 0.2 and area['left'] < 0.2 and area['right'] > 0.2:
                state_area = 'case 5 - obstacle in left'
                
            elif area['front'] < 0.2 and area['left'] < 0.2 and area['right'] < 0.2:
                state_area = 'case 6 - obstacle in front and left and right'
                
                 
            else:
                state_area = 'unknown case'
                
                rospy.loginfo(area)

            rospy.loginfo(state_area)
            
                 
        else:
            state_area = 'case 7 - It is finihed !'
            
            rospy.loginfo(state_area)
            
                       

    
            
            
            
if __name__ == '__main__':
    OA = ObstacleAvoidance()
