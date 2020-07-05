import cx_Freeze

executables = [cx_Freeze.Executable("Falling.py")]

cx_Freeze.setup(
    name = "Falling",
    options = {"build_exe": {"packages": ["pygame", "random", "os", "csv", "inspect"], "include_files":["Falling.mp3", "gameparameters.csv"]}},
    executables = executables
    )
