from test.fixture import run

def test_declined():
    #given
    user_input = 'no'

    #when
    program_output = run(user_input)

    #then
    assert program_output == 'Hello! Do you want to play? YES/NO\n> Good bye!\n'

def test_declined_separated_by_whitespace():
    #given
    user_input = 'y e s'

    #when
    program_output = run(user_input)

    #then
    assert program_output == 'Hello! Do you want to play? YES/NO\n> Good bye!\n'

def test_declined_substring():
    # given
    user_input = 'xyesx'
    # when
    program_output = run(user_input)
    # then
    assert program_output == 'Hello! Do you want to play? YES/NO\n> Good bye!\n'