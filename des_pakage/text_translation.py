from random import getrandbits


# text -> 64bit
# ASKII -> 7bit -> "0" + ASCII -> 8bit

def key_generator(n):
   key = format(getrandbits(n), "b")

   return key


def str_to_byte(text):
   byte_array = bytearray(text.encode("ascii"))
   str_list = []
   
   for i in byte_array:
      str_list.append("0" + str(format(i, "b")))
      
   return "".join(str_list)


def byte_to_str(byte):
   byte_list = []
   str_list = []
   n = 0
   
   for i in byte:
      byte_list.append(i)
      n += 1
      
      if n == 8:
         bit_t = "".join(byte_list)
         str_b = "0b" + bit_t
      
         str_list.append(chr(int(str_b, 2)))
      
         n = 0
         byte_list = []
      
   return "".join(str_list)
