"""_나 a-z A-Z 로 변수를 시작할 수 있다. 예약어는 사용할 수 없다"""

# convention


_my_val = "what is mean? under score value"
"""
"내부 사용" 또는 "private" 개체를 나타내는 규칙입니다.


파이썬에서는 private의 개념이 없음으로 코드를 읽는사람으로 부터 이 변수는 내부에서만 사용되는 변수거나 private임을 알려주는 용도로 사용됩니다. 
이 방식으로 이름이 지정된 개체는 다음과 같은 문을 통해 가져오지 않습니다. (from module import *)
python 인터프리터는 이것을 보고 개인 객체라고 받아들입니다. (엑세스 할 수 없다는 뜻은 아닙니다.)
"""

__my_val = "what is mean? double unser score value"
"""
클래스 속성을 "망글링"하는 데 사용 - 상속 체인에서 유용함
동일한 변수를 사용하는데 어느것이 어느것인지 구분하기 위해서도 사용할 수 있음
"""

__my_val__ = "what is mean?"

"""
인터프리터에 특별한 의미가 있는 시스템 정의 이름에 사용됩니다.
그것들을 발명하지 말고 Python이 미리 정의한 것들을 고수하세요!

__init__
x < y   --->  x.__lt__(y)
"""

# PEP8 규칙
"""
Packages: short, all-lowercase names. Preferably no underscores.(짧은 이름, 모든 이름. 밑줄이 없는 것이 좋습니다.)
Modules: short, all-lowercase names. Can have underscores.(밑줄이 있을 수 있습니다.)
Classes: CapWords (upper camel case) convention(Upper Camel 케이스를 따릅니다.)
Functions: lowercase, words separated by underscores (snake_case)
Variables: lowercase, words separated by underscores (snake_case)
Constants: all-uppercase, words separated by underscores (전체 텍스트가 밑줄로 구분된 대문자로 작성합니다.)

This is a should-read!
https://www.python.org/dev/peps/pep-0008/
"""