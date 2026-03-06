#Question 4.6
import numpy as np

def mc_run():
    f = input("Enter function: ")
    a = float(input("Lower bound: "))
    b = float(input("Upper bound: "))
    
    x = np.random.uniform(a, b, 100000)
    
    # Vectorized evaluation and integration
    y = eval(f, {"np": np, "x": x})
    integral = (b - a) * np.mean(y)
    
    print(f"Result: {integral:.6f}")

mc_run()
