
class IsNotDefined(Exception):
         def __init__(a,l):
             super().__init__('"'+l+'" is not defined')
##kernel_________________________________________________
def kernel(i):
     f=type('empty',(),{})
     p=[0,False,f,f,f,'']
     o=[f,f,f,f]
     class kernel:
          def __init__(a):
              p[5]='<__main__.kernel object at '+hex(id(a))+'>'
          def __getattr__(a,b):
               return getattr(this,b)
          def __str__(a):
              return p[5]
          def __repr__(a):
              return p[5]
          
     k=kernel()
     class this:
      locals().update(i(k))
      this=0
      def mode(m):
           p[4]=m
      def open(f,l={}):
         o[0]=f.read
         o[1]=f.seek
         o[2]=f.tell
         o[3]=l
      def end():
           p[1]=False
      def setdef(m):
            this.this=m
   #   def call(d,*a,**b):
    #      g=p[0]
         # j=p[1]
     #     p[0]=id(d)
      #    b=d(*a,**b) 
       #   p[0]=g
         # p[1]=j
        #  return b
      def run(d,*a,**b):
          g=p[1]
          p[1]=True
          while p[1]:
           d(*a,**b)
          p[1]=g
      def get():
          return p[4](o[0])
      def seek(*a):
          return o[1](*a)
      def key():
          return p[0]
      def tell():
          return o[2]()
      def info(n):
          return o[3][n]
      
     return k

