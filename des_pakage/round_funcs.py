# 라운드 함수 클래스
class round_func:
   def __init__(self, R, key, parity_drop_1, parity_drop_2, shift_key, subkey_box, parity_box, count):
      self.__pc1 = parity_drop_1  # 키 압축 1
      self.__pc2 = parity_drop_2  # 키 압축 2
      self.__shift_key = shift_key  # 비트 옮김
      self.__sbox = subkey_box
      self.__pbox = parity_box
      self.__r = R  # 라운드(MAX: 16)
      self.__key = key
      self.current_n = count
      self.result = ""
   
   
   # 확장 = 32bit -> 48bit
   def expansion_R(self):
      list_byte = []
      e_byte = []
      
      n = 0
      m = 0
      
      for i in self.__r:
         list_byte.append(i)
      
         n += 1
         m += 1
      
         if n == 4:
            byte_t = "".join(list_byte)
      
            if m == 32:
               head_text = self.__r[m - 5]
               tail_text = self.__r[0]
      
            else:
               head_text = self.__r[m - 5]
               tail_text = self.__r[m + 1]
               e_byte.append(head_text + byte_t + tail_text)
               
               n = 0 
               list_byte = []
                
      return "".join(e_byte)
   
   
   def shift_left(self, n, d, length):
      result = ((n << d) & (2 ** length - 1)) | (n >> (length - d))
      
      return result
   
   
   # 서브 키 생성
   def subkey_generator(self):
      subkey_pc1 = [0] * len(self.__pc1)
      subkey_pc2 = [0] * len(self.__pc2)
      n = 0
      
      for i in self.__pc1:
         subkey_pc1[n] = self.__key[i]
         n += 1
      
      subkey_pc = "".join(subkey_pc1)
   
      c_subkey = subkey_pc[:int(len(subkey_pc1) / 2)]
      d_subkey = subkey_pc[int(len(subkey_pc1) / 2):]
      len_subkey = len(c_subkey)
        
      c_shift = bin(self.shift_left(int(c_subkey, 2), int(self.__shift_key[self.current_n]), len_subkey))[2:].zfill(len_subkey)
      d_shift = bin(self.shift_left(int(d_subkey, 2), int(self.__shift_key[self.current_n]), len_subkey))[2:].zfill(len_subkey)
      subkey_shift = c_shift + d_shift 
      n = 0
      
      for i in self.__pc2:
         subkey_pc2[n] = subkey_shift[i]
         n += 1
        
      return "".join(subkey_pc2)
   
   
   def subkey_box(self, subkey_pc2):
      bit_list = []
      s_box = []
      n = 0
      
      for i in subkey_pc2:
         bit_list.append(i)
         n += 1
         
         if (n % 6) == 0:
            s_val = bin(self.__sbox[(n // 6) - 1][int(bit_list[0] + bit_list[5], 2)][int(bit_list[1] + bit_list[2] + bit_list[3], 2)])[2:].zfill(6)
            s_box.append(s_val)
            bit_list = []

      return "".join(s_box)
   
        
   def parity_box(self, s_box):
      n = 0
      subkey = [0] * len(self.__pbox)
      
      for i in self.__pbox:
         subkey[n] = s_box[i]
         n += 1
         
      return "".join(subkey)    
   
        
   def active_func(self):
      e_r = self.expansion_R()
      s_g = self.subkey_generator()
      subkey_xor = bin(int(e_r, 2) ^ int(s_g, 2))[2:].zfill(48)
      subkey_sbox = self.subkey_box(subkey_xor)
      self.result = self.parity_box(subkey_sbox)
   