from time import time

class c_random_number_generator(self):

    #initiates the timer to prep for random number generator
    self.v_app_start_time = time()

    def f_gen_random_number(self):
        v_app_request_ran = time()
        v_app_random_number = v_app_start_time-v_app_request_ran

