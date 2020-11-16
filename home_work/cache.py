def do_cache(maxsize):
    def decorator(func):
        def wrapper(*args):
            cache = list()
            cache.append(args)
            a = args[0]
            b = args[1]
            cache.append(a**b)
            print(cache)
            if len(cache) > maxsize:
                cache.pop()
            # if args in cache2:
            #     return cache2[2]
            return func(*args)
        return wrapper
    return decorator

@do_cache(maxsize=2)
def get_value(a, b):
    return a ** b

print(get_value(2,2))