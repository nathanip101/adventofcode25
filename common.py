def timed_execution(func, *args):
    import time
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    return result