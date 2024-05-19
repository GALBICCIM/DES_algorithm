from init_tables import *
from text_translation import *
from cryptions import DES


# TEST
key = key_generator(64).zfill(64)

if __name__ == "__main__":
   plain_text = input("암호화할 문자를 영어로 쓰세요... : ")
   name = str_to_byte(plain_text)
   object = DES(name, key, 16, parity_drop_1, parity_drop_2, shift_key, subkey_box, parity_box)
   
   print("입력하신 문자의 이진수 값 (ASCII) :: ", name)
   print("\n<<암호화 시작>>")
   
   object.encryption()
   print("암호화된 이진수 값 :: ", object.resulttext)
   print("이진수 암호문을 문자로 변환 :: ", byte_to_str(object.resulttext))
   
   # TODO: 복호화 고치기
   object_2 = DES(object.resulttext, key, 16, parity_drop_1, parity_drop_2, shift_key, subkey_box, parity_box)
   print("\n<<복호화 시작>>")
   
   object_2.decryption()
   print("복호화된 이진수 값 :: ", object_2.resulttext)
   print("이진수 평문을 문자로 변환 :: ", byte_to_str(object_2.resulttext))
