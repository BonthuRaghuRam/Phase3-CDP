# # # print binary sequences
def binary(size,res,n):
      if size==n:
          print(res)
          return
      binary(size+1,res+"1",n)
      binary(size+1,res+"0",n)
  n=4
  binary(0,"",n)
