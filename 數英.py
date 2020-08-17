A=float(input('請輸入數學成績'))

B=float(input('請輸入英文成績')) 
if (A >=0 and A <= 100) and (B>=0 and B<=100):
    
 if A > 90 and B > 90:
    print('會有獎品')
 elif A <60 and B < 60:
    print('會有處罰')
 elif A <60 or B <60:
    print('在加油')
else:
    print('你又手殘')

    
    
    
        