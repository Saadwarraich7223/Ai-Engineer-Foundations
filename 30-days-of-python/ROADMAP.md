# 🗺️ 30-Day Python Mastery — Roadmap & Resources

> A day-by-day guide with curated learning resources, practice exercises, and mini-projects.

---

## Phase 1 — Python Fundamentals (Days 01–07)

---

### Day 01 — Variables, Scope & `__name__`

**Goal**: Understand how Python stores and manages data in memory.

- [ ] **Concepts**: Variables, naming rules (`snake_case`), dynamic typing, multiple assignment, `id()` and `type()`, variable re-binding vs mutation
- [ ] **Scope**: LEGB rule (Local → Enclosing → Global → Built-in), `global` keyword, `locals()` / `globals()`
- [ ] **Special**: `__name__` guard (`if __name__ == "__main__":`)

**Resources**:
- [Python Docs — Naming and binding](https://docs.python.org/3/reference/executionmodel.html#naming-and-binding)
- Real Python: [Variables in Python](https://realpython.com/python-variables/)
- Real Python: [Python Scope & the LEGB Rule](https://realpython.com/python-scope-legb-rule/)
- Corey Schafer: [Python `__name__` == `__main__`](https://www.youtube.com/watch?v=sugvnHA7ElY)
- W3Schools: [Python Variables](https://www.w3schools.com/python/python_variables.asp)

**Exercises**:
1. Swap two variables without a temp variable
2. Write a script that prints "Run directly" vs "Imported" using `__name__`
3. Demonstrate the LEGB rule with nested functions
4. Track memory addresses of mutable vs immutable objects

**File**: `01_Variables/main.py`

---

### Day 02 — Data Types & Type Conversion

**Goal**: Master Python's built-in types and seamless type casting.

- [ ] **Immutable**: `int`, `float`, `bool`, `str`, `tuple`, `frozenset`, `bytes`
- [ ] **Mutable**: `list`, `dict`, `set`, `bytearray`
- [ ] **Type Conversion**: `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, `dict()`, `bool()`
- [ ] **Edge Cases**: `0.1 + 0.2 != 0.3`, `None` type, truthy/falsy values, `isinstance()`, `type()`

**Resources**:
- [Python Docs — Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- Real Python: [Basic Data Types](https://realpython.com/python-data-types/)
- Fluent Python (Luciano Ramalho) — Chapter 2
- Corey Schafer: [Python Tutorial for Beginners](https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFZiLCpG1cY)

**Exercises**:
1. Create a truth table of all falsy values in Python
2. Safely convert a list of strings to integers (handle errors)
3. Check the type of every built-in literal (`1`, `1.0`, `"a"`, `[1]`, etc.)
4. Demonstrate the float precision problem with `Decimal`

**File**: `02_DataTypes/main.py`

---

### Day 03 — Strings & Formatting

**Goal**: Wield Python string manipulation like a pro.

- [ ] **Methods**: `.split()`, `.join()`, `.strip()`, `.replace()`, `.find()`, `.startswith()`, `.endswith()`, `.count()`, `.isalpha()`, `.isdigit()`
- [ ] **Slicing**: `s[start:stop:step]`, negative indices, reversing
- [ ] **Formatting**: f-strings (`f"{name=}"`), `.format()`, `%`-formatting
- [ ] **Advanced**: `str.maketrans()`, `textwrap`, `re` (regex intro)

**Resources**:
- [Python Docs — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- Real Python: [Python String Formatting Best Practices](https://realpython.com/python-string-formatting/)
- Real Python: [f-strings](https://realpython.com/python-f-strings/)
- PyCon Talk: [The Mighty Dictionary (string interning)](https://www.youtube.com/watch?v=C4Kc8xzcLF8)

**Exercises**:
1. Reverse a string using slicing
2. Parse `"name=John;age=30;city=NYC"` into a dictionary
3. Check if a string is a palindrome (ignore case & punctuation)
4. Use f-string debug syntax: `f"{variable=}"`
5. Count word frequency in a sentence

**File**: `03_Strings/main.py`

---

### Day 04 — Lists & List Operations

**Goal**: Write efficient, Pythonic list code.

- [ ] **Methods**: `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.index()`, `.count()`, `.sort()`, `.reverse()`, `.copy()`
- [ ] **Slicing**: `list[start:stop:step]`, shallow copy vs deep copy
- [ ] **Patterns**: `enumerate()`, `zip()`, `map()`, `filter()`, `sorted()`, `reversed()`
- [ ] **Advanced**: list as stack (`append`/`pop`), list as queue (`collections.deque`), nested lists, matrix transpose

**Resources**:
- [Python Docs — Data Structures (Lists)](https://docs.python.org/3/tutorial/datastructures.html)
- Real Python: [Lists and Tuples](https://realpython.com/python-lists-tuples/)
- GeeksforGeeks: [Python List Methods](https://www.geeksforgeeks.org/list-methods-in-python/)
- Ned Batchelder: [Loop Like a Native](https://nedbatchelder.com/text/iter.html)

**Exercises**:
1. Merge two sorted lists into one sorted list
2. Rotate a list by `k` positions
3. Transpose a 3×3 matrix manually and with `zip(*)`
4. Find all duplicates in a list (O(n) time)
5. Flatten a nested list `[[1,2],[3,[4,5]]]`

**File**: `04_Lists/main.py`

---

### Day 05 — Dictionaries & Sets

**Goal**: Leverage hash-based data structures for speed.

- [ ] **Dict Methods**: `.get()`, `.setdefault()`, `.update()`, `.pop()`, `.popitem()`, `.keys()`, `.values()`, `.items()`, `defaultdict`, `Counter`, `OrderedDict`
- [ ] **Set Operations**: `union`, `intersection`, `difference`, `symmetric_difference`, `issubset`, `issuperset`
- [ ] **Dict Patterns**: dict comprehension, merging (`|` operator in 3.9+), key-based lookup vs `get()`, hashable keys

**Resources**:
- [Python Docs — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Docs — Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- Real Python: [Dictionaries in Python](https://realpython.com/python-dicts/)
- Real Python: [Python `collections.Counter`](https://realpython.com/python-counter/)

**Exercises**:
1. Count character frequency in a string using `dict`, `defaultdict`, and `Counter`
2. Find common elements across 3 lists using sets
3. Invert a dictionary (keys ↔ values, handle duplicates)
4. Merge two dicts with the `|` operator (3.9+) and `.update()`
5. Group a list of words by their first letter

**File**: `05_Dictionaries/main.py`

---

### Day 06 — Functions & Lambdas

**Goal**: Write clean, reusable, and Pythonic functions.

- [ ] **Fundamentals**: `def`, `return`, docstrings (`"""`), type hints (`def f(x: int) -> str:`)
- [ ] **Arguments**: positional, keyword, default, `*args`, `**kwargs`, order rules
- [ ] **Lambdas**: `lambda x: x**2`, use with `map`/`filter`/`sorted`
- [ ] **Advanced**: closures, `functools.partial`, `functools.wraps`, recursion, `@lru_cache`

**Resources**:
- [Python Docs — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- Real Python: [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
- Real Python: [Python `*args` and `**kwargs`](https://realpython.com/python-kwargs-and-args/)
- Real Python: [Python Closures](https://realpython.com/python-closure/)

**Exercises**:
1. Write a function with all 4 argument types (positional, default, *args, **kwargs)
2. Create a closure-based counter
3. Use `functools.partial` to fix a function's parameter
4. Sort a list of dicts by a key using `sorted()` + `lambda`
5. Implement a recursive factorial with `@lru_cache`

**File**: `06_Functions/main.py`

---

### Day 07 — Mini Project 1

**Goal**: Solidify fundamentals by building a real CLI tool.

**Project**: **CLI Contact Book**
- **Features**:
  - Add, list, search, update, delete contacts
  - Store contacts in a dictionary (in-memory)
  - Search by name, email, or phone
  - Export contacts to JSON
  - Pretty-print the contact list
- **Concepts used**: variables, strings, lists, dicts, functions, user input (`input()`), JSON

**Resources**:
- Project inspiration: [Build a Contact Book](https://realpython.com/python-contact-book/)
- [Python Docs — `json` module](https://docs.python.org/3/library/json.html)

**Deliverable**: `07_MiniProject/contact_book.py` — a fully functional CLI app.

---

## Phase 2 — Intermediate Python (Days 08–14)

---

### Day 08 — OOP: Classes & Inheritance

**Goal**: Think in objects — encapsulation, inheritance, and polymorphism.

- [ ] **Fundamentals**: `class`, `__init__`, `self`, instance vs class vs static methods (`@staticmethod`, `@classmethod`)
- [ ] **Inheritance**: `class B(A):`, `super()`, MRO (`ClassName.__mro__`), multiple inheritance
- [ ] **Dunder Methods**: `__str__`, `__repr__`, `__eq__`, `__lt__`, `__len__`, `__getitem__`, `__call__`
- [ ] **Properties**: `@property`, `@<name>.setter`, `@<name>.deleter`
- [ ] **Data Classes**: `@dataclass`, `field()`, `frozen=True`

**Resources**:
- [Python Docs — Classes](https://docs.python.org/3/tutorial/classes.html)
- Real Python: [Object-Oriented Programming (OOP) in Python](https://realpython.com/python3-object-oriented-programming/)
- Real Python: [Python `@dataclass`](https://realpython.com/python-data-classes/)
- Raymond Hettinger: [PyCon — Python's Class Development Toolkit](https://www.youtube.com/watch?v=HTLu2DFOdTg)

**Exercises**:
1. Create a `BankAccount` class with deposit/withdraw/balance
2. Build an inheritance hierarchy: `Animal` → `Mammal` → `Dog`
3. Write a `__str__` and `__repr__` for a custom class
4. Use `@dataclass` to model a `Student` with name, age, grades
5. Create a property that validates a value on set

**File**: `08_OOP/main.py`

---

### Day 09 — Modules & Packages

**Goal**: Organize Python code across files and manage dependencies.

- [ ] **Modules**: `import`, `from ... import`, `importlib.reload()`, `__pycache__`
- [ ] **Packages**: `__init__.py`, subpackages, relative vs absolute imports
- [ ] **Standard Library**: `os`, `sys`, `math`, `random`, `datetime`, `pathlib`, `itertools`, `collections`
- [ ] **Virtual Envs**: `venv`, `requirements.txt`, `pip freeze`

**Resources**:
- [Python Docs — Modules](https://docs.python.org/3/tutorial/modules.html)
- Real Python: [Python Modules and Packages](https://realpython.com/python-modules-packages/)
- Real Python: [Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)
- [Python Docs — `itertools` recipes](https://docs.python.org/3/library/itertools.html#itertools-recipes)

**Exercises**:
1. Create a package with 3 submodules and import all of them
2. Use `pathlib` to list all `.py` files in a directory
3. Generate 10 random passwords using `random` + `string`
4. Use `itertools.product` to generate all combinations of `[A,B,C]` × `[1,2,3]`
5. Practice relative imports within a package

**File**: `09_Modules/main.py`

---

### Day 10 — Error Handling & Exceptions

**Goal**: Write robust code that fails gracefully.

- [ ] **Basics**: `try`/`except`/`else`/`finally`, built-in exceptions hierarchy (`BaseException` → `Exception` → ...)
- [ ] **Patterns**: specific exception handling, `raise`, `assert`, `raise ... from e` (chaining), custom exceptions
- [ ] **Context**: `with` statement, context managers (`__enter__`/`__exit__`), `contextlib.contextmanager`
- [ ] **Logging**: `import logging`, log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL), config

**Resources**:
- [Python Docs — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- Real Python: [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)
- Real Python: [Python Logging](https://realpython.com/python-logging/)
- [Python Docs — `contextlib`](https://docs.python.org/3/library/contextlib.html)

**Exercises**:
1. Write a division function that handles `ZeroDivisionError` and `TypeError`
2. Create a custom `InsufficientFundsError` exception for a bank account class
3. Build a context manager that times code execution (`__enter__`/`__exit__`)
4. Set up a logger that writes to both console and file
5. Use `contextlib.contextmanager` decorator for a file-open context

**File**: `10_ErrorHandling/main.py`

---

### Day 11 — File I/O & Context Managers

**Goal**: Read and write every file format Python can handle.

- [ ] **Text Files**: `open()`, `r`/`w`/`a`/`r+`, `with` statement, `.read()`, `.readline()`, `.readlines()`, `.write()`, `.writelines()`
- [ ] **Binary Files**: `rb`/`wb`, `struct`, `pickle`
- [ ] **Formats**: JSON (`json`), CSV (`csv`), YAML (`pyyaml`), Excel (`openpyxl`/`pandas`)
- [ ] **Advanced**: `tempfile`, `io.StringIO`/`BytesIO`, `pathlib.Path.read_text()`, file encoding

**Resources**:
- [Python Docs — Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- Real Python: [Reading and Writing Files in Python](https://realpython.com/read-write-files-python/)
- Real Python: [Python `csv` module](https://realpython.com/python-csv/)
- Real Python: [Python `json` module](https://realpython.com/python-json/)

**Exercises**:
1. Read a CSV file and print each row as a dictionary
2. Write a JSON file from a Python dictionary
3. Use `pathlib.Path` to glob all `.txt` files in a directory
4. Serialize/deserialize an object with `pickle`
5. Read a large file line by line (memory-efficient)

**File**: `11_FileHandling/main.py`

---

### Day 12 — Comprehensions

**Goal**: Write compact, readable, and Pythonic transformations.

- [ ] **Types**: list comprehensions `[x for x in ...]`, dict comprehensions `{k:v for ...}`, set comprehensions `{x for x in ...}`
- [ ] **Nested**: `[expr for a in A for b in B]`, flattening, matrix operations
- [ ] **Conditional**: `[x for x in items if cond]`, ternary inside `[x if cond else y for x in items]`
- [ ] **vs**: generator expressions `(x for x in ...)` — memory comparison

**Resources**:
- [Python Docs — List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- Real Python: [Python List Comprehensions](https://realpython.com/list-comprehension-python/)
- Real Python: [When to Use a List Comprehension](https://realpython.com/python-list-comprehension-vs-generator-expression/)
- Trey Hunner: [Overuse of list comprehensions](https://treyhunner.com/2019/03/why-you-might-not-want-to-use-a-list-comprehension-in-python/)

**Exercises**:
1. Matrix transpose with nested list comprehension
2. Extract all vowels from a string using set comprehension
3. Build a dict mapping word → length from a sentence
4. Flatten `[[1,2],[3,4,5],[6]]` into `[1,2,3,4,5,6]`
5. Compare memory of list comprehension vs generator expression for 10⁶ items

**File**: `12_Comprehensions/main.py`

---

### Day 13 — Generators & Iterators

**Goal**: Build memory-efficient, lazy sequences.

- [ ] **Iterators**: `__iter__`/`__next__`, `StopIteration`, `iter()`, `next()`
- [ ] **Generators**: `yield`, generator functions vs generator expressions, `yield from`, `send()`, `throw()`, `close()`
- [ ] **Lazy Evaluation**: `range`, `map`, `filter`, `zip` — all lazy, `itertools.islice`, `itertools.chain`, `itertools.cycle`, `itertools.count`
- [ ] **Advanced**: coroutines with `yield`, `Generator` type hint (`from typing import Generator`)

**Resources**:
- [Python Docs — Generators](https://docs.python.org/3/tutorial/classes.html#generators)
- Real Python: [Introduction to Python Generators](https://realpython.com/introduction-to-python-generators/)
- Real Python: [Python `itertools`](https://realpython.com/python-itertools/)
- David Beazley: [Generator Tricks for Systems Programmers](https://www.dabeaz.com/generators/)

**Exercises**:
1. Create a Fibonacci generator using `yield`
2. Build a generator that reads a large file line by line (lazy)
3. Use `itertools.cycle` to alternate between two colors infinitely
4. Write a generator pipeline: read → filter → transform → output
5. Implement a coroutine with `send()` to compute a running average

**File**: `13_Generators/main.py`

---

### Day 14 — Mini Project 2

**Goal**: Build an intermediate-level CLI tool using all concepts so far.

**Project**: **Task Manager CLI**
- **Features**:
  - CRUD operations: add, list, complete, delete tasks
  - Persist tasks to JSON file
  - Filter tasks by status (all/pending/done)
  - Search by title
  - Priority levels (high/medium/low)
  - Due dates with sorting
  - Color-coded output (use ANSI escape codes or `colorama`)
- **Concepts**: OOP (Task class, TaskManager class), file I/O, error handling, list comprehensions, generators (lazy loading)

**Resources**:
- [Python Docs — `argparse`](https://docs.python.org/3/library/argparse.html) for CLI arguments
- [colorama](https://pypi.org/project/colorama/) for colored terminal output
- [Real Python — CLI Apps with argparse](https://realpython.com/command-line-interfaces-python-argparse/)

**Deliverable**: `14_MiniProject/task_manager.py` — a fully functional CLI task manager.

---

## Phase 3 — Data Science Stack (Days 15–20)

---

### Day 15 — NumPy

**Goal**: Master the foundation of numerical computing in Python.

- [ ] **Arrays**: `np.array()`, `ndarray`, shape, dtype, `reshape()`, `flatten()`, broadcasting
- [ ] **Indexing**: integer indexing, slicing, boolean indexing, fancy indexing
- [ ] **Operations**: vectorized ops (much faster than loops), `np.sum`, `np.mean`, `np.std`, `np.min`, `np.max`, `np.argmin`, `np.argmax`
- [ ] **Linear Algebra**: `np.dot`, `@` (matrix multiplication), `np.linalg.inv`, `np.linalg.eig`, `np.linalg.svd`
- [ ] **Random**: `np.random.rand`, `randn`, `randint`, `seed`, `normal`, `uniform`

**Resources**:
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy Absolute Beginner Guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
- Real Python: [NumPy Tutorial](https://realpython.com/numpy-array-programming/)
- Sentdex: [NumPy Tutorial Playlist](https://www.youtube.com/playlist?list=PLQVvvaa0QuDf9pFe7gCmnK6PBEy2q2i9v)

**Exercises**:
1. Create a 5×5 identity matrix
2. Generate 1000 random numbers from a normal distribution, compute mean & std
3. Replace all negative values in an array with 0
4. Compute element-wise product of two 3×3 matrices (both `*` and `np.dot`)
5. Find the index of the maximum value in each row of a 2D array

**File**: `15_NumPy/main.py`

---

### Day 16 — Pandas

**Goal**: Load, inspect, and transform tabular data.

- [ ] **Series & DataFrame**: creation from dict, list, CSV, `.head()`, `.info()`, `.describe()`, `.shape`, `.dtypes`
- [ ] **Indexing**: `.loc[]`, `.iloc[]`, `.at[]`, `.iat[]`, boolean indexing, `query()`
- [ ] **Filtering, Sorting, Grouping**: `.sort_values()`, `.groupby()`, `.agg()`, `.pivot_table()`, `.crosstab()`
- [ ] **Columns**: `.rename()`, `.drop()`, adding/removing columns, `.apply()`, `.map()`, `.applymap()`
- [ ] **Dates**: `pd.to_datetime()`, `.dt.year`, resampling with `.resample()`

**Resources**:
- [Pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
- Real Python: [Pandas Tutorial](https://realpython.com/pandas-python-explore-dataset/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- Corey Schafer: [Pandas Tutorial Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS)

**Exercises**:
1. Load a CSV into a DataFrame and display summary stats
2. Filter rows where a column value > threshold
3. Group by a category column and compute mean of a numeric column
4. Create a new column based on a conditional (`apply` or `np.where`)
5. Parse a date column and extract month/year

**File**: `16_Pandas/main.py`

---

### Day 17 — Data Cleaning

**Goal**: Turn messy real-world data into analysis-ready form.

- [ ] **Missing Data**: `.isna()`, `.dropna()`, `.fillna()`, `interpolate()`, `ffill`/`bfill`
- [ ] **Duplicates**: `.duplicated()`, `.drop_duplicates()`
- [ ] **Outliers**: IQR method, Z-score method, visualization-based detection
- [ ] **Transformations**: `.replace()`, `.str` accessor, `.astype()`, `pd.cut()`, `pd.qcut()`, `normalize`/`standardize`

**Resources**:
- Real Python: [Pandas Data Cleaning](https://realpython.com/python-data-cleaning-numpy-pandas/)
- [Pandas — Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- Kaggle: [Data Cleaning Course](https://www.kaggle.com/learn/data-cleaning)

**Exercises**:
1. Load a dataset, identify missing values, and fill them appropriately
2. Detect and remove duplicate rows
3. Remove outliers using the IQR method
4. Normalize numeric columns to [0, 1] range
5. Clean a column with mixed data types (numbers stored as strings with symbols)

**File**: `17_DataCleaning/main.py`

---

### Day 18 — Data Visualization

**Goal**: Tell stories with data using plots and charts.

- [ ] **Matplotlib**: `plt.plot()`, `plt.scatter()`, `plt.bar()`, `plt.hist()`, `plt.boxplot()`, `plt.subplots()`, figure/axes API, customization (labels, titles, legends, grids, styling)
- [ ] **Seaborn**: `sns.barplot`, `sns.boxplot`, `sns.violinplot`, `sns.pairplot`, `sns.heatmap`, `sns.kdeplot`, themes
- [ ] **Plotly (bonus)**: interactive plots, `px.scatter`, `px.line`, `px.bar` — great for notebooks

**Resources**:
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- Real Python: [Python Plotting with Matplotlib](https://realpython.com/python-matplotlib-guide/)
- Real Python: [Seaborn in Python](https://realpython.com/seaborn-python/)
- [From Data to Viz](https://www.data-to-viz.com/) — helps pick the right chart

**Exercises**:
1. Plot a line chart of a time series
2. Create a 2×2 subplot grid with different chart types
3. Generate a correlation heatmap using Seaborn
4. Create a pairplot of the Iris dataset
5. Customize a chart with labels, title, grid, and a color palette

**File**: `18_Visualization/main.py`

---

### Day 19 — Exploratory Data Analysis (EDA)

**Goal**: Systematically explore and understand a dataset.

- [ ] **Process**: data overview → cleaning → univariate analysis → bivariate analysis → multivariate analysis → insights
- [ ] **Univariate**: `.hist()`, `.boxplot()`, `.describe()`, skewness, kurtosis
- [ ] **Bivariate**: scatter plots, correlation, cross-tabs, grouped bar charts
- [ ] **Multivariate**: pairplots, heatmaps, 3D scatter, dimensionality intuition
- [ ] **Tools**: `pandas_profiling` / `ydata-profiling`, Autoviz (automated EDA)

**Resources**:
- Real Python: [EDA with Python](https://realpython.com/python-data-analytics/)
- Kaggle: [EDA on Iris Dataset](https://www.kaggle.com/code/hemeswar/eda-iris-dataset)
- Medium: [EDA Guide with Examples](https://towardsdatascience.com/exploratory-data-analysis-eda-a-practical-guide-and-template-for-structured-data-abfbf3ee3bd9)

**Dataset**: Use the Titanic dataset from Seaborn (`sns.load_dataset('titanic')`) or Kaggle.

**Exercises**:
1. Load dataset and print shape, columns, dtypes, missing values
2. Compute summary statistics for all numeric columns
3. Visualize the distribution of the target variable
4. Find correlations between features and target
5. Write a 5-sentence summary of insights from the data

**File**: `19_EDA/eda_titanic.ipynb` or `19_EDA/eda_titanic.py`

---

### Day 20 — Data Project 1

**Goal**: End-to-end data analysis project.

**Project**: **Analyze a Real Dataset**
- **Steps**:
  1. Choose a dataset (Kaggle: [Titanic](https://www.kaggle.com/c/titanic), [Housing](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-data-set), or [COVID-19](https://www.kaggle.com/datasets/imdevskp/corona-virus-report))
  2. Load and inspect
  3. Clean missing values, fix data types
  4. EDA with statistics and visualizations
  5. Answer 3–5 analytical questions
  6. Write a summary of findings
- **Outcome**: A well-documented analysis (Jupyter notebook or Python script + markdown report)

**Deliverable**: `20_DataProject/analysis.py` + `20_DataProject/README.md` with findings.

---

## Phase 4 — Machine Learning (Days 21–26)

---

### Day 21 — ML Basics & Scikit-Learn

**Goal**: Understand ML fundamentals and the Scikit-Learn API.

- [ ] **Concepts**: supervised vs unsupervised, training vs testing, features vs labels, overfitting vs underfitting, bias-variance tradeoff
- [ ] **Scikit-Learn API**: `.fit()`, `.predict()`, `.score()`, `.transform()`, train/test split (`train_test_split`), preprocessing (`StandardScaler`, `LabelEncoder`)
- [ ] **Workflow**: load data → split → preprocess → train → evaluate → predict

**Resources**:
- [Scikit-Learn Getting Started](https://scikit-learn.org/stable/getting_started.html)
- [Scikit-Learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- Real Python: [ML with Scikit-Learn](https://realpython.com/python-scikit-learn-a-first-look/)
- StatQuest with Josh Starmer: [ML Fundamentals](https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Kay3JSM)

**Exercises**:
1. Load the Iris dataset from `sklearn.datasets`
2. Split into train/test (80/20)
3. Scale features with `StandardScaler`
4. Train a `KNeighborsClassifier`
5. Evaluate accuracy on test set

**File**: `21_ML_Basics/main.py`

---

### Day 22 — Regression

**Goal**: Predict continuous numerical values.

- [ ] **Linear Regression**: `LinearRegression`, assumptions (linearity, independence, homoscedasticity, normality), coefficients, intercept
- [ ] **Metrics**: MSE, RMSE, MAE, R², Adjusted R²
- [ ] **Regularization**: Ridge (`L2`), Lasso (`L1`), `ElasticNet` — when and why
- [ ] **Polynomial**: `PolynomialFeatures` for non-linear relationships

**Resources**:
- [Scikit-Learn — Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)
- StatQuest: [Linear Regression](https://www.youtube.com/watch?v=ZkjP5RJLQF4)
- StatQuest: [Ridge vs Lasso](https://www.youtube.com/watch?v=Xm2C_gVFhsY)
- Real Python: [Linear Regression in Python](https://realpython.com/linear-regression-in-python/)

**Exercises**:
1. Train a linear regression on the Boston/diabetes dataset (or California housing)
2. Compute MSE, RMSE, R² manually and with sklearn
3. Compare Linear, Ridge, and Lasso regression
4. Plot actual vs predicted values
5. Use PolynomialFeatures to fit a curve

**File**: `22_Regression/main.py`

---

### Day 23 — Classification

**Goal**: Predict categorical outcomes.

- [ ] **Algorithms**: LogisticRegression, KNN, DecisionTree, SVM, Naive Bayes
- [ ] **Metrics**: accuracy, precision, recall, F1-score, confusion matrix, ROC curve, AUC
- [ ] **Imbalanced Data**: class weights, SMOTE (`imblearn`), stratified split
- [ ] **Multi-class**: OvR (One-vs-Rest), OvO (One-vs-One)

**Resources**:
- [Scikit-Learn — Classification](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
- StatQuest: [Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8)
- StatQuest: [Decision Trees](https://www.youtube.com/watch?v=7VeUPuFGJHk)
- StatQuest: [SVM](https://www.youtube.com/watch?v=efR1C6CvhmE)

**Exercises**:
1. Train LogisticRegression, KNN, and DecisionTree on Iris
2. Print confusion matrix and classification report
3. Compare precision, recall, F1 across models
4. Plot ROC curves for all models on the same axes
5. Handle class imbalance by adjusting class_weight

**File**: `23_Classification/main.py`

---

### Day 24 — Model Evaluation

**Goal**: Avoid overfitting — validate models properly.

- [ ] **Cross-Validation**: `cross_val_score`, `KFold`, `StratifiedKFold`, `LeaveOneOut`
- [ ] **Hyperparameter Tuning**: `GridSearchCV`, `RandomizedSearchCV`, `learning curves`, `validation curves`
- [ ] **Overfitting**: train vs validation gap, regularization, early stopping
- [ ] **Feature Importance**: `coef_` (linear), `feature_importances_` (tree-based), permutation importance

**Resources**:
- [Scikit-Learn — Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Scikit-Learn — Tuning](https://scikit-learn.org/stable/modules/grid_search.html)
- Real Python: [K-Fold Cross-Validation](https://realpython.com/cross-validation-machine-learning/)
- StatQuest: [Cross-Validation](https://www.youtube.com/watch?v=fSytzGwwBVw)

**Exercises**:
1. Perform 5-fold cross-validation on a classifier
2. Use GridSearchCV to tune KNN hyperparameters (n_neighbors, weights)
3. Plot learning curves for training vs validation error
4. Interpret feature importance from a trained model
5. Compare tuned vs default model performance

**File**: `24_ModelEvaluation/main.py`

---

### Day 25 — Feature Engineering

**Goal**: Create better features = better models.

- [ ] **Numeric**: scaling, normalization, binning (`pd.cut`), polynomial features, log transform
- [ ] **Categorical**: one-hot encoding (`OneHotEncoder`), label encoding, ordinal encoding, target encoding
- [ ] **Text**: bag-of-words, TF-IDF, n-grams, basic text features (length, word count)
- [ ] **Dates**: day of week, month, quarter, is_weekend, days_since
- [ ] **Feature Selection**: variance threshold, correlation filtering, `SelectKBest`, `RFE`, `mutual_info_classif`

**Resources**:
- [Scikit-Learn — Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Feature Engineering Book](https://www.featureengineeringbook.com/) (Alice Zheng)
- Kaggle: [Feature Engineering Course](https://www.kaggle.com/learn/feature-engineering)
- Medium: [Feature Engineering Guide](https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114)

**Exercises**:
1. Apply one-hot encoding to a categorical column
2. Create polynomial features (degree=2) from 3 numeric features
3. Extract day-of-week, month, and is_weekend from a date column
4. Compute TF-IDF for a small text dataset
5. Use SelectKBest to pick top 5 features

**File**: `25_FeatureEngineering/main.py`

---

### Day 26 — Clustering

**Goal**: Find hidden groups in unlabeled data.

- [ ] **K-Means**: `KMeans`, elbow method, silhouette score, `inertia_`
- [ ] **Hierarchical**: `AgglomerativeClustering`, dendrograms (`scipy.cluster.hierarchy`)
- [ ] **DBSCAN**: density-based, eps, min_samples, handles outliers
- [ ] **Evaluation**: silhouette score, Davies-Bouldin index, Calinski-Harabasz index, visual inspection

**Resources**:
- [Scikit-Learn — Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- StatQuest: [K-means Clustering](https://www.youtube.com/watch?v=4b5d3muPQmA)
- StatQuest: [Hierarchical Clustering](https://www.youtube.com/watch?v=7xHsKQgyBu4)
- StatQuest: [DBSCAN](https://www.youtube.com/watch?v=RDZUdRSDOok)

**Exercises**:
1. Apply K-Means to the Iris dataset (drop labels) and evaluate with silhouette score
2. Plot the elbow curve to find optimal K
3. Compare K-Means, Agglomerative, and DBSCAN on the same data
4. Visualize clusters in 2D using PCA for dimensionality reduction
5. Interpret the cluster centers

**File**: `26_Clustering/main.py`

---

## Phase 5 — Capstone Projects (Days 27–30)

---

### Day 27 — Capstone Project 1

**Project**: **End-to-End Regression Pipeline**
- **Dataset**: [California Housing](https://inria.github.io/scikit-learn-mooc/python_scripts/datasets_california_housing.html) or [Kaggle House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
- **Tasks**:
  - EDA and data cleaning
  - Feature engineering (log transforms, polynomial features, interaction terms)
  - Train Linear, Ridge, Lasso, and a tree-based model
  - Hyperparameter tuning with GridSearchCV
  - Model evaluation with cross-validation
  - Feature importance analysis
  - Final model selection and prediction

**Deliverable**: `27_Project1/pipeline.py`

---

### Day 28 — Capstone Project 2

**Project**: **End-to-End Classification Pipeline**
- **Dataset**: [Titanic](https://www.kaggle.com/c/titanic) or [Heart Disease UCI](https://www.kaggle.com/datasets/amanajmera1/framingham-heart-study-dataset)
- **Tasks**:
  - EDA (including survival rate by gender/class/age)
  - Handle missing values and outliers
  - Feature engineering (family size, title extraction, age bands)
  - Train LogisticRegression, RandomForest, SVM, GradientBoosting
  - Handle class imbalance
  - Hyperparameter tuning
  - ROC curves, confusion matrix, classification report
  - SHAP or permutation feature importance

**Deliverable**: `28_Project2/pipeline.py`

---

### Day 29 — Capstone Project 3

**Project**: **Unsupervised Learning — Customer Segmentation**
- **Dataset**: [Mall Customers](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) or generate synthetic data
- **Tasks**:
  - EDA on customer features (age, income, spending score)
  - Feature scaling
  - K-Means with elbow method & silhouette analysis
  - PCA for 2D/3D visualization of clusters
  - Interpret each cluster (profile the customer segments)
  - Hierarchical clustering with dendrogram
  - Write business recommendations per segment

**Deliverable**: `29_Project3/pipeline.py`

---

### Day 30 — Final Summary & Portfolio

**Goal**: Consolidate everything into a personal portfolio.

- [ ] **Review**: Go through all 29 days of code, notes, and projects
- [ ] **Organize**: Ensure every folder has clean, well-commented code
- [ ] **README**: Update the root README with commit history filled in
- [ ] **Portfolio**: Create a summary notebook or document showcasing:
  - Day 20 Data Analysis Project
  - Day 27 Regression Pipeline
  - Day 28 Classification Pipeline
  - Day 29 Customer Segmentation
- [ ] **Next Steps**:
  - Deep Learning: [fast.ai](https://www.fast.ai/), [PyTorch Tutorials](https://pytorch.org/tutorials/)
  - Advanced ML: [MLOps](https://ml-ops.org/), [DVC](https://dvc.org/), deployment
  - Certifications: [TensorFlow Developer](https://www.tensorflow.org/certificate), [AWS ML Specialty](https://aws.amazon.com/certification/certified-machine-learning-specialty/)
  - Practice: [Kaggle Competitions](https://www.kaggle.com/competitions), [LeetCode](https://leetcode.com/)

**Deliverable**: `30_FinalSummary/portfolio_overview.md` — a personal portfolio README.

---

## 📖 Bonus Resources

### Books
| Title | Author | Focus |
|-------|--------|-------|
| Python Crash Course | Eric Matthes | Beginner Python |
| Fluent Python | Luciano Ramalho | Advanced Python |
| Python Data Science Handbook | Jake VanderPlas | Data Science |
| Hands-On ML | Géron | Machine Learning |
| Feature Engineering for ML | Alice Zheng | Feature Engineering |

### YouTube Channels
- [Corey Schafer](https://www.youtube.com/user/schafer5) — Python fundamentals
- [Sentdex](https://www.youtube.com/user/sentdex) — Python + ML
- [StatQuest with Josh Starmer](https://www.youtube.com/@statquest) — ML theory (goldmine)
- [3Blue1Brown](https://www.youtube.com/@3blue1brown) — Linear algebra & calculus intuition
- [Tech With Tim](https://www.youtube.com/@TechWithTim) — Python projects

### Practice Platforms
- [LeetCode (Python track)](https://leetcode.com/) — interview prep
- [HackerRank Python](https://www.hackerrank.com/domains/python) — fundamentals practice
- [Kaggle](https://www.kaggle.com/) — datasets + competitions
- [Exercism Python](https://exercism.org/tracks/python) — mentor-reviewed exercises
- [Codewars](https://www.codewars.com/) — kata challenges

### Cheat Sheets (Keep handy)
- [Python 3 Memento](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)
- [NumPy Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Matplotlib Cheat Sheet](https://datacamp-community-prod.s3.amazonaws.com/e1a8f39d-71ad-4d13-9a6e-0b5ed84c21e5)
- [Scikit-Learn Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Scikit_Learn_Cheat_Sheet_Python.pdf)

---

## ✅ Daily Routine

```
□ Read the day's concept (theory + docs)
□ Watch 1–2 recommended videos
□ Complete the exercises
□ Write clean, commented code
□ Update README commit log
□ git add . && git commit -m "Day XX: Topic"
□ Push to GitHub
```

> **Consistency > Intensity.** Show up every day. The compound effect of 30 days will surprise you.

---

*Happy Coding! 🐍✨*
