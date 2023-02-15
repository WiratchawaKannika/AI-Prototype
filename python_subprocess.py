import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    ##'basic
    #subprocess.run(["ls", "-ltr"])
    #subprocess.run(["python", "python_script_101.py", "5", "--x", "6"])

    ## ues output of subprocss
    sum = 0
    count = 0
    for num in range(0, 101):
        if (num % 2) != 0:
            count += 1
            process1 = subprocess.Popen(["python", "python_script_101.py", "4","--x", f"{num}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process1.communicate()
            outputt = out.decode('utf-8')
            print(f"({count}.) Input x: {num}")
            print(outputt)
            #print(len(outputt.strip().split("\n")))
            #print(outputt.strip().split("\n"))
            out_xt = outputt.strip().split("\n")[1]
            #print(out_xt)
            out_xt_i = int(out_xt.split("=")[-1])
            #print(out_xt_i)
            #print(type(out_xt_i))
            sum += out_xt_i
    print('-'*100)
    print(f"Print Sum of Xt ==> {sum}")
    print('-'*100)
    # HW สั่งรัน python_scrip101.py 50 รอบ [1, 3, 5, 7, 9 ,...,99]
    #  #แล้วให้เอา output ของ xt มารวมกัน แล้ว print ออกมา
    