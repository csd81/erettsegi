Here’s a summary of the provided text on **Searching with Boost String Algorithms**:

The Boost String Algorithms library (in `<boost/algorithm/string/find.hpp>`) provides convenient functions for searching within strings or ranges. These functions wrap around various **finder objects** that perform targeted searches in strings.

### Example: `find_head`
- The `find_head(s, n)` function returns a range containing the first **n** elements of the string `s`.
- In the provided example (Listing 15-35), calling `find_head(word, 5)` on the string `"blandishment"` yields a range covering `"bland"`.

### Table of Common Find Algorithms (Table 15-17)
| **Function**              | **Purpose**                                                   |
|---------------------------|---------------------------------------------------------------|
| `find_first(s1, s2)`      | Finds the first occurrence of `s2` in `s1`.                   |
| `ifind_first(s1, s2)`     | Case-insensitive version of `find_first`.                    |
| `find_last(s1, s2)`       | Finds the last occurrence of `s2` in `s1`.                   |
| `ifind_last(s1, s2)`      | Case-insensitive version of `find_last`.                     |
| `find_nth(s1, s2, n)`     | Finds the **n-th** occurrence of `s2` in `s1`.               |
| `ifind_nth(s1, s2, n)`    | Case-insensitive version of `find_nth`.                      |
| `find_head(s, n)`         | Returns the first **n** characters of `s`.                   |
| `find_tail(s, n)`         | Returns the last **n** characters of `s`.                    |
| `find_token(s, p)`        | Finds the first character in `s` matching the predicate `p`. |
| `find_regex(s, rgx)`      | Finds the first substring in `s` matching a regular expression.|
| `find(s, fnd)`            | Applies a custom finder function `fnd` to `s`.               |

In short, these tools make it easy to search strings with custom criteria or patterns, both case-sensitive and case-insensitive, as well as finding specific occurrences or using regular expressions.