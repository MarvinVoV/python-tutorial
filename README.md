# python-tutorial

Python Tutorial

## Data types

### Dict

#### What's the difference between dict.get('key') and dict['key] ？

The primary difference between `dict.get('keyname')` and `dict['keyname']` in Python lies in **how they handle missing
keys**:

1. `dict.get('keyname')`:
    - The `get` method is used to retrieve the value associated with a given key from a dictionary.
    - If the key exists in the dictionary, `dict.get('keyname')` returns the corresponding value.
    - If the key is not found in the dictionary, it returns `None` by default (or a specified default value if
      provided).

   Example:
   ```python
   my_dict = {'name': 'Alice', 'age': 30}
   value = my_dict.get('name')  # Returns 'Alice'
   value = my_dict.get('city')  # Returns None (key not found)
   value = my_dict.get('city', 'Unknown')  # Returns 'Unknown' (default value provided)
   ```

2. `dict['keyname']`:
    - Using square brackets with the key name directly (e.g., `dict['keyname']`) is another way to retrieve the value
      associated with a key in a dictionary.
    - If the key exists in the dictionary, it returns the corresponding value.
    - If the key is not found in the dictionary, it raises a `KeyError` exception.

   Example:
   ```python
   my_dict = {'name': 'Alice', 'age': 30}
   value = my_dict['name']  # Returns 'Alice'
   value = my_dict['city']  # Raises a KeyError (key not found)
   ```

In summary:

- Use `dict.get('keyname')` when you're not sure if the key exists in the dictionary and you want to avoid raising an
  exception. You can provide a default value to be returned if the key is not found.
- Use `dict['keyname']` when you are confident that the key exists in the dictionary and you want to access the value
  directly. Be cautious when using this method, as it can raise a `KeyError` if the key is missing.