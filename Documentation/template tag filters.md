# Template tag filters 
| Filter         | Description                                                  | Example                                     |
|----------------|--------------------------------------------------------------|---------------------------------------------|
| `add`          | Adds a value to the argument                                 | `{{ value|add:2 }}`                        |
| `capfirst`     | Capitalizes the first character of the value                 | `{{ value|capfirst }}`                     |
| `cut`          | Removes all occurrences of a specified string from the value | `{{ value|cut:" " }}`                      |
| `date`         | Formats a date according to a given format                   | `{{ value|date:"Y-m-d" }}`                 |
| `default`      | Provides a default value if the value is not available       | `{{ value|default:"N/A" }}`                |
| `escape`       | Escapes HTML characters in the value                         | `{{ value|escape }}`                       |
| `first`        | Returns the first item in a list                             | `{{ value|first }}`                        |
| `floatformat`  | Formats a number as a float with a specified number of digits| `{{ value|floatformat:2 }}`                |
| `join`         | Joins a list with a specified separator                       | `{{ value|join:", " }}`                    |
| `last`         | Returns the last item in a list                               | `{{ value|last }}`                         |
| `length`       | Returns the length of a value                                 | `{{ value|length }}`                       |
| `lower`        | Converts the value to lowercase                               | `{{ value|lower }}`                        |
| `pluralize`    | Returns an "s" if the value is not 1, used for pluralization | `{{ value|pluralize }}`                    |
| `slugify`      | Converts the value to a URL-friendly format                   | `{{ value|slugify }}`                      |
| `striptags`    | Removes HTML tags from the value                              | `{{ value|striptags }}`                    |
| `time`         | Formats a time value according to a given format              | `{{ value|time:"H:i" }}`                   |
| `timesince`    | Returns the time since the specified date as a string         | `{{ value|timesince }}`                    |
| `truncatechars`| Truncates the value to a specified number of characters       | `{{ value|truncatechars:10 }}`             |
| `truncatewords`| Truncates the value to a specified number of words            | `{{ value|truncatewords:5 }}`              |
| `upper`        | Converts the value to uppercase                               | `{{ value|upper }}`                        |
