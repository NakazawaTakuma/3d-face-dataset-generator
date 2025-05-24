import cupy as cp

def set_age_gender(lp,c_data):
     #gender
     c_data[lp][1] = cp.random.randint(0, 2)
     #age
     c_data[lp][2] = cp.random.randint(10, 91)

