# Love Calculator 💘

This fun script calculates a "love score" based on the names of two people.

## How It Works
- Combines both names and converts them to lowercase.
- Counts the total number of letters from the word **"TRUE"**.
- Counts the total number of letters from the word **"LOVE"**.
- Joins the two counts to form a final love score (e.g. 4 from "TRUE" and 6 from "LOVE" gives 46).

## Example
```python
calculate_love_score(name1="Miguel Gonzales", name2="Manny Pacquiao")
# Output: 66
