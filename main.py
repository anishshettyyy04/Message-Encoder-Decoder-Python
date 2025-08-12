import random
import string
def get_random_string(length=3):
    return ''.join(random.choices(string.ascii_letters, k=length))
s=input("Enter the message ")
words=s.split(' ')
print("Enter the choice ")
print("1.Encoding the Message ")
print("2.Decoding the Message ")
choice=int(input())
match choice:
  case 1:
    coding=True
    if(coding):
      nwords=[]
      for word in words:
        if(len(word)>=3):
          random_word_1 = get_random_string()
          random_word_2 = get_random_string()
          new_string=random_word_1+word[1:]+word[0]+random_word_2
          nwords.append(new_string)
        else:
          nwords.append(word[::-1])#reverse the word
          print(" ".join(nwords))


  case 2:
      nwords=[]
      for word in words:
        if(len(word)>=3):
          new_string=word[3:-3]
          new_string=new_string[-1]+new_string[:-1]
          nwords.append(new_string)
        else:
          nwords.append(word[::-1])#reverse the word
          print(" ".join(nwords))
  case _:
    print("enter the correct choice")
