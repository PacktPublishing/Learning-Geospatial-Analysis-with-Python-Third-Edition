# Locate your Python site-packages directory
import sys
# Try the last path in the list
print(sys.path[-1])
# Otherwise look at the whole list manually
print(sys.path)
