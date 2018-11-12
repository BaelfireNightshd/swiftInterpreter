# swiftInterpreter
A swift interpreter written in python allowing swift code to be ran on any platform that supports python.

# Running
Run the python swift interpreter with the following command
```
py swift.py [<*.swift file to be run>]
```
If no \*.swift file is given, swift's REPL will start.

# Project Organization
### swift.py
The main script that either runs a .swift file or if none is given, starts a REPL session.

### interpreter.py
Contains the class that parses swift code and runs code from `swiftLang` and `stdlib`

### swiftLang
Contains the modules to support the base swift language.

All module names begin with `lang_` 

Each module is named after the section it's found in in swift.org's [Summary of Grammar].

For example, everything defined under **GRAMMAR OF WHITESPACE** should be defined in the file `lang_whitespace.py`

### stdlib
Contains implementations in python of [Apple's own stdlib]

Internal folder structure matches Apple's. 

Eventually the ability to read directly from the .swift files defined in [Apple's own stdlib] should be added as to not have to reinvent the wheel in python. May not happen for libraries that interface with things like stdout (Print.swift).

All module names begin with the parent folder's name followed by an underscore. 

For example, the equivalent of `Print.swift` is named `core_print.py`



[Summary of Grammar]: https://docs.swift.org/swift-book/ReferenceManual/zzSummaryOfTheGrammar.html
[Apple's own stdlib]: https://github.com/apple/swift/tree/master/stdlib

# Project Progress

### swiftLang

<!---   use :x: emoji as no and :heavy_check_mark: as yes --->
#### Lexical Structure
|               Grammar               |       Complete     | Comment
| ----------------------------------- |:------------------:| -------
| Whitespace                          | :x:                | Only comment complete
| Identifier                          | :x:                | 
| Literal                             | :x:                | 
| Integer Literal                     | :x:                | 
| Floating Point Literal              | :x:                | 
| String Literal                      | :x:                | 
| Operators                           | :x:                | 

#### Types
|               Grammar               |       Complete     | Comment
| ----------------------------------- |:------------------:| -------
| Type                                | :x:                | 
| Type Annotation                     | :x:                | 
| Type Identifier                     | :x:                | 
| Tuple Type                          | :x:                | 
| Function Type                       | :x:                | 
| Array Type                          | :x:                | 
| Dictionary Type                     | :x:                | 
| Optional Type                       | :x:                | 
| Implicitly Unwrapped Optional Type  | :x:                | 
| Protocol Composition Type           | :x:                | 
| Metatype Type                       | :x:                | 
| Type Inheritance Clause             | :x:                | 

#### Expressions
|               Grammar               |       Complete     | Comment
| ----------------------------------- |:------------------:| -------

#### Statements
|               Grammar               |       Complete     | Comment
| ----------------------------------- |:------------------:| -------

#### Declarations
|               Grammar               |       Complete     | Comment
| ----------------------------------- |:------------------:| -------

#### Attributes
|               Grammar               |       Complete     | Comment
| ----------------------------------- |:------------------:| -------

#### Patterns
|               Grammar               |       Complete     | Comment
| ----------------------------------- |:------------------:| -------

#### Generic Parameters and Arguments
|               Grammar               |       Complete     | Comment
| ----------------------------------- |:------------------:| -------


### stdlib
TODO
