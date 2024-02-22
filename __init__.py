import check50

@check50.check()
def add():
  """15"""
  check.run("./a.out").stdout("15", regex=False).exit(0)
