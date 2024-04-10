## End to End Machine Learning project ##
##python -m src.components.data_ingestion -use to run any  .py file sometime directly 
let’s understand why python src/Exception.py didn’t work.

When you run a script directly using python src/Exception.py, Python treats this script as the main module and it doesn’t consider it as part of a package, even if the script is inside a package directory (like src in this case). This is why it doesn’t recognize any parent package and you get the error ImportError: attempted relative import with no known parent package when you try to do a relative import.

On the other hand, when you use -m to run the script as a module like python -m src.Exception, Python recognizes src as a package and Exception as a module inside this package. This way, Python knows the parent package and can correctly handle relative imports.

This is a common behavior in Python and is related to how it handles imports and packages. I hope this explanation helps!
