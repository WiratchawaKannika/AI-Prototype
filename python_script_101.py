import argparse #สำหรับ รับ input จากภายนอก

def parse_input():
    parser = argparse.ArgumentParser(description='test program to learn about argparse')
    parser.add_argument('m', type=int, help='value of M positional argument') ## Input Shot name ## Must to input first position   
    parser.add_argument('--x', type=int, required = True, help='value of x')
    parser.add_argument('--yval', type=int, default=3, help='value of y') ## Input long name

    args = parser.parse_args()
    return args

def print_other():
    print('something else')

def print_ones():
    print('1'*20) 

if __name__ == "__main__":
    x = parse_input()
    print_ones()
    print_other()
    
    print(f"value of M positional argument ==>: {x.m}")
    print(f"value of x ==>: {x.x}")
    print(f"value of y ==>: {x.yval}")






#import subprocess #สำหรับ รัน terminal command

#import flask #สำหรับ ทำ web app และ web service api





#if __name__ == "__main__":

    #args = parse_input()
    
   # x = args.x
    #y = args.yval
   # print(f'M = {args.m}')
    #print(f'calculate {x} x {y} = {x*y}')
