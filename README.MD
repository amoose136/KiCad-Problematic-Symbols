## KiCAD symbols with problems

I found out that certain KiCAD symbols are doing things in a not so good manner. So I made a python script that will list any symbol that has pins with a name the same as one of the global power symbols. It is not a safe assumption that two of the same component on the same board will be operating with the same ground and VCC so they shouldn't be auto net tied together.
