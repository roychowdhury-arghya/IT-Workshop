def safe_get_value(d, key, default=None):
    try:
        value = d[key]
    except KeyError:
        return default
    except TypeError:
        return "Invalid dictionary or key type"
    else:
        return value
    finally:
        pass


# -------- Auto Demo Output --------
data = {"a": 10, "b": 20}

print("Key exists:", safe_get_value(data, "a"))
print("Key not found:", safe_get_value(data, "c", 0))
print("Wrong dictionary type:", safe_get_value(5, "a"))
