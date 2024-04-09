def draw_line_string(msg1, msg2):
    nstr = len(msg1) if(len(msg1)>len(msg2)) else len(msg2)
    print("-"*nstr)
    print(msg1)
    print(msg2)
    print("-"*nstr)


msg = input('Input his/her name: ')
msg1 = 'Hello '+ msg + ','
msg2 = 'Welcome to Seoul.'

draw_line_string(msg1, msg2)

    
    
