def reward_function(params):
   
    # Read input parameters
    track_width = params['track_width']
    speed = params['speed']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    abs_steering = abs(params['steering_angle'])
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    all_wheels_on_track = True


    if abs_steering > 20 and all_wheels_on_track == True:
        if speed < 2: 
            reward = 4 + (speed)**2
        else:
            reward = 0.002
    
    elif abs_steering <= 20:
        if speed > 2:
            if speed == 3:
                reward = 10 + (speed)**2
            reward = 8 + (speed)**2
        
        else:
            reward = 0.002
    
    return reward
