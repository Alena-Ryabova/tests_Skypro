
def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    """
    if key.lower() in collection:
        return collection[key.lower()]
    else:
        return default

