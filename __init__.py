import check50

@check50.check()
def add():
  """15"""
  check50.run("./a.out").stdout("15", regex=False).exit(0)
