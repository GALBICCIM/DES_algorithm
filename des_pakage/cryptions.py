from des_pakage.round_funcs import *


# 암호화 및 복호화 클래스
class DES:
   def __init__(self, plain_text, key, num_round, parity_drop_1, parity_drop_2, shift_key, subkey_box, parity_box):
      self.__plaintext = plain_text
      self.__key = key
      self.num_round = num_round
      self.resulttext = ""
      self.__pc1 = parity_drop_1
      self.__pc2 = parity_drop_2
      self.__shift_key = shift_key
      self.__sbox = subkey_box
      self.__pbox = parity_box
      
   
   def encryption(self):
      L_text = self.__plaintext[:32]  # 왼쪽부터 32bit
      R_text = self.__plaintext[32:]  # 오른쪽부터 32bit
      
      for i in range(self.num_round):
         R_tmp = R_text
         
         f_object = round_func(R_text, self.__key, self.__pc1, self.__pc2, self.__shift_key, self.__sbox, self.__pbox, i)
         f_object.active_func()
         
         result_round = bin(int(L_text, 2) ^ int(f_object.result, 2))[2:].zfill(32)
         
         R_text = result_round
         L_text = R_tmp
         
      self.resulttext = R_text + L_text
         
         
   def decryption(self):
      R_text = self.__plaintext[:32]
      L_text = self.__plaintext[32:]
      
      for i in range(self.num_round - 1, -1, -1):
         L_tmp = L_text
         
         f_object = round_func(R_text, self.__key, self.__pc1, self.__pc2, self.__shift_key, self.__sbox, self.__pbox, i)
         f_object.active_func()
         
         result_round = bin(int(R_text, 2) ^ int(f_object.result, 2))[2:].zfill(32)
         
         L_text = result_round
         R_text = L_tmp
         
      self.resulttext = L_text + R_text
