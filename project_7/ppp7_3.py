#연도(y)를 주면, 윤년인지(True) 아닌지를(False) 알려주는 is_leap_year(y) 함수를
#만드시오. 단 윤년의 조건은 주어진 조건으로 구현하시오. 4로 나누었을 때 나누어 떨
#어지면 윤년. 4로 나누어떨어지더라도, 100으로 나누어 떨어진다면, 윤년 아님
def is_leap_year(y):
    y= int(input("윤년의 값을 판단해드리겠습니다."))
    if y % 4==0:
        y='윤년이 맞습니다.'

    elif y % 100==0:
          y="윤년이 맞습니다."
    else:
        y='윤년이 아닙니다.'

    return y

def main():
    print(is_leap_year('y'))

if __name__=="__main__":
    main()