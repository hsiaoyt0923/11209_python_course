# 猜數字遊戲
import random
import pyinputplus as pyip
def playGame():
   min = 1
   max = 100
   count = 0
   target = random.randint(min, max)
   print(target)
   print("===============猜數字遊戲=================:")
   while(True):
      try:
         keyin = input(f"猜數字範圍{min}~{max}[按q終止遊戲]")
         if keyin == 'q':                          
            print('遊戲中止')     
            break                
         keyinInt = int(keyin)
      except:
         print('格式錯誤，請輸入整數')               
         continue               
      else:
         if (min <= keyinInt <= max): 
            count += 1                                
            print()                                   
            print(f'猜數字範圍{min}~{max}:',end='')    
            print(keyinInt)                           
            if (keyinInt == target):                    
               print(f'您猜中了,答案是{keyinInt}')     
               print(f'您總共猜了{count}次')            
               break                                  
            elif (keyinInt < target):                               
               min = keyinInt + 1                                    
               print('提示:再大一點')                        
               continue                                           
            elif (keyinInt > target):                                                                   
               max = keyinInt - 1                                                      
               print('提示:再小一點')                                                
            
            print(f'您已經猜了{count}次')
         else:
            print('請輸入提示範圍內的數字')

while(True):
   playGame()  
   answer = pyip.inputYesNo(prompt='您是否要繼續遊戲?(y,n)', yesVal='y', noVal='n')   
   print()
   if not answer == 'y':
      break
print('遊戲結束')