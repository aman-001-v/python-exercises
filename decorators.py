from functools import wraps
def timer(original_func):
    @wraps(original_func)
    def wrapper(*args , **kwargs):
        import time
        t = time.time()
        # time.sleep(1)
        result = original_func(*args , **kwargs)
        t1 = time.time()
        print("{} executed in {} seconds".format(original_func.__name__ , t1 - t))
        return result
    return wrapper

def logger(original_func):
    @wraps(original_func)
    def wrapper(*args , **kwargs):
        print("Calling {}\nargs={}\nkwargs={}".format(original_func.__name__ , args , kwargs))
        return original_func(*args , **kwargs)
    return wrapper
    
def repeat(n):
    def decorator(original_func):
        @wraps(original_func)
        def wrapper(*args , **kwargs):
            result = []
            for i in range(0,n):
                result.append(original_func(*args , **kwargs))
            return result
        return wrapper

    return decorator

def require_login(original_func):
    @wraps(original_func)
    def wrapper(*args , **kwargs):
        if logged_in == False:
            print("Access Denied")
            return None
        else:
            return original_func(*args , **kwargs)
    return wrapper
        

@logger
@timer
@repeat(2)
@require_login
def deploy_server(name):
    print(f"Deploying {name}")

logged_in = False
deploy_server("web-01")

print("----------------")

logged_in = True
deploy_server("web-01")