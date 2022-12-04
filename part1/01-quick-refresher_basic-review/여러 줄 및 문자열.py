"""암묵적으로 동작"""
a = [1,  # item1
     2,  # item2
     3  # item3
     ]


def my_func(a,
            b,  # comment
            c):
    print(a, b, c)


my_func(10,  # comment
        20, 30)

"""명시적으로 동작"""
"""if 10
    and 20
    and 30:
    """
if 10 \
        and 20 \
        and 30:
    print("abc")

# docstring과 주석은 같은것이 아님
# docstring은 python이 코드를 컴파일하면 해당 문자열이 코드의 일부분이 됩니다. 그것들은 컴파일되고 컴파일된 바이트코드에 입력됩니다.
