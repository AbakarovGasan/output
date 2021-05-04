class tr:
    gh=''
    en=['\n']
    
def daemon(l):
    def x(*a,**b):
        __k.run(l,*a,**b)
    return x

isiden=str.isidentifier
isnum=str.isdigit
isspace=str.isspace
def isspec(a):
    if not isiden(a):
        if not isnum(a):
            if not isspace(a):
                return True
    return False

def word():
  global word
  @daemon
  def d():
    f=__k.get()
    if isiden(f):
        tr.gh+=f
    elif isnum(f):
        tr.gh+=f
    else:
        __k.end()
  @daemon
  def r():
      f=__k.get()
      if not isiden(f):
          pass
      else:
          tr.gh=f
          __k.end()
  def word():
      tr.gh=''
      r()
      d()
      return tr.gh
word()

def space():
    global space
    @daemon
    def g():
        
    
