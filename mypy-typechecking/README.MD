# Python Type Checking

If you are accustomed to type-safe languages, such as C, C++, Java or C#, then you might find using a language such as Python somewhat disconcerting.

> Writing Python can seem quick and easy, in part because it is intelligent enough to perform implicit type conversions for you automatically.

Of course, Python is interpreted and not compiled. In a type-safe compiled language, we often rely on the compile step to spot errors or issue warnings before the code is ever executed. Some languages such as Rust can even refuse to compile if you attempy an operation that is not considered memory-safe.

> In addition to greater performance, a goal of compilers is to pick up errors are build time as opposed to run-time.

You might argue that code should be **tested**. Well, for that to work, your tests need to have full coverage, which can be hard to achieve. There may be branches of code that only run *sporadically* (e.g. a handler for a rare type of error). Of course a diligent developer may try and test all branches through the code, but this requires discipline and can be missed or added as a regression. 

We are human, and prone to mistakes, so need all the help we can get. Build tools should help us as much as possible, especially for tasks that are repetetive and/or time consuming.

## Implicit Type Conversion

Central to this discussion is the convenient but also dangerous *implicit type conversion* feature of Python. Consider the following class member function:

```Python
    def set_name(self, new_name) :
        if self.name != new_name:
            self.name = new_name
            print("Name changed to: ", self.name)
        else:
            print("Name is already: ", self.name)
```

If you pass a `string` as a parameter, the Python interpreter will automatically change the underlying type to `str`.

```Python
obj.set_name("1234")
```

If you pass an `integer` as a parameter, the Python interpreter will automatically change the underlying type an `int`.

```Python
obj.set_name(1234)
```

This will seem to work however as all we ever do in this code is print the value. Now to someone accustomed with writing in type-safe languages, this may well ring alarm bells!

Now consider a different function:

```python
    def set_serial(self, new_serial):
        if self.serial != new_serial:
            self.serial = new_serial
            print("Serial changed to: ", self.serial)
        else:
            print("Serial is already: ", self.serial)

    def get_next_serial(self) -> int:
        return self.serial + 1
```

Note that `get_next_serial` performs arithmetic. This makes sense only if the serial number is a numeric type. The following code works without issue:

```python
    t1.set_serial(000)
    next_sn = t1.get_next_serial()
    print("Next serial number: ", next_sn)
```

But what if we accidentally pass a string representation of a number?

```python
    t1.set_serial("000")
    next_sn = t1.get_next_serial()
    print("Next serial number: ", next_sn)
```

The first line executes, and sets the member variable to a `string` type.

> Python variables can change type at run-time

However, the second function causes a run-time crash as it attempts to add an the integer `1` to the string `"000"`.

> A compiled type-safe language would at least warn the developer at build time, and more likely produce a compile error.

So we may like the convenience of Python, but might miss some of the safety features of type-safe languages. Let's look at ways of getting the tools to do more checking for us.

## Type Hints

In Python 3, we can add *type hints* to our Python code. So taking the example above, we add type-hints as follows:

```Python
    def set_serial(self, new_serial: int) -> None:
        if self.serial != new_serial:
            self.serial = new_serial
            print("Serial changed to: ", self.serial)
        else:
            print("Serial is already: ", self.serial)

    def get_next_serial(self) -> int:
        return self.serial + 1
```

Note how the parameters and return type of functions can now be expressed explicitly. This is great for helping others to use your APIs, but how might we get the computer to help us comply with these type rules?

For that, we need python package called [`mypy`](https://www.mypy-lang.org/). You can simply `pip install mypy` in your virtual environment and you're good to go.

You can now check your python code for type-conformance by running `mypy` from the command line:

```bash
mypy myfile.py

```

where `myfile.py` is your Python source file. This is only one of many coding aids for Python, so while we are here, let's get as much help as we can. Furthermore, wouldn't it be nice if these tools ran in the background and flagged errors with intellisense? This is where Visual Studio Code extensions can come in handy.

## Coding Aids

Python will never have the type-safety of C++ or Rust, but we can improve matters by adding the following:

* **linting** - whereby the tools check for common errors and poor coding style
* **layout** - clear and consistent indentation is critical to verify the correct flow through the code
* **type hints** - Yes, you can add "type hints" to your Python code. You then need an aditional tools to highlight where you peform an implicit type conversion.
* **unit testing** - I will cover this in another project, but writing code for testability is a big topic


The following are all extensions from Microsoft, so are safe to install. You may want to add others (as I have done in [this file](./.vscode/extensions.json) ).

```JSON
{
    "recommendations": [
        "ms-python.autopep8",
        "ms-python.debugpy",
        "ms-python.mypy-type-checker",
        "ms-python.pylint",
        "ms-python.python",
        "ms-python.vscode-pylance"    
    ]
  }
```

When the project is opened in VSCode, there will be a pop-up asking if you want to install the workspace extensions from `extensions.json`.
These extensions are also listed in the Extensions tab under Workspace Recommendations.

Once these are installed, you should see intellisense underline code that needs attention:

* `pylint` - linting suggestions
* `mypy-type-checker` - type checking
* `autopep8` - adds a right-click context menu to format your code correctly.

# Task - try it

Clone this repository, launch VS Code and open the folder with this example.

There are two type errors. Can you find and fix them using these tools?

