.. baseball documentation master file, created by
   sphinx-quickstart on Thu May  2 22:24:18 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Lab_7 baseball.py 문서화(수동)
====================================


is_digit(user_input_number) 함수

    Input:
      - user_input_number : 문자열 값
    Output:
      - user_input_number가 정수로 변환 가능할 경우는 True,
        그렇지 않을 경우는 False
    Examples:
      >>> import baseball_game as bg
      >>> bg.is_digit("551")
      True
      >>> bg.is_digit("103943")
      True
      >>> bg.is_digit("472")
      True
      >>> bg.is_digit("1032.203")
      False
      >>> bg.is_digit("abc")
      False

====================================

is_between_100_and_999(user_input_number) 함수

    Input:
      - user_input_number : 문자열 값
                            입력된 값은 숫자형태의 문자열 값임이 보장된다.
    Output:
      - user_input_number가 정수로 변환하여 100이상 1000미만일 경우 True,
        그렇지 않을 경우는 False
    Examples:
      >>> import baseball_game as bg
      >>> bg.is_between_100_and_999("551")
      True
      >>> bg.is_between_100_and_999("103943")
      False
      >>> bg.is_between_100_and_999("472")
      True
      >>> bg.is_between_100_and_999("0")
      False

====================================

is_duplicated_number(three_digit) 함수

    Input:
      - three_digit : 문자열로 된 세자리 양의 정수 값
                      문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    Output:
      - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
        그렇지 않을 경우는 False
      ex) 117 - True, 123 - False, 103 - False, 113 - True
    Examples:
      >>> import baseball_game as bg
      >>> bg.is_duplicated_number("551")
      True
      >>> bg.is_duplicated_number("402")
      False
      >>> bg.is_duplicated_number("472")
      False
      >>> bg.is_duplicated_number("100")
      True

* :ref:`search`
