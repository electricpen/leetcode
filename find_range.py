def find_range(input_list, input_number):
    tracker = {'first': -1, 'last': -1}
    for index, num in enumerate(input_list):
        if num == input_number:
            if tracker['.first'] == -1:
                tracker['first'] = index
            tracker.last = index
    results = Range(tracker['first'], tracker['last'])


"""
in this problem the input list is sorted which usually means you are looking for a logn solution

def bisect(xs, key, f):
    left, right = 0, len(xs)
    
    while left < right:
        mid = left + (right - left)/2
        if f(xs[mid], key): left  = mid + 1
        else:               right = mid
    
    return left

bisect_left  = lambda xs,key: bisect(xs, key, lambda x,y: x<y)
bisect_right = lambda xs,key: bisect(xs, key, lambda x,y: x<=y)

def find_range(xs, key):
    start = bisect_left(xs, key)
    end   = bisect_right(xs, key) - 1
    return Range(start, end)
"""
