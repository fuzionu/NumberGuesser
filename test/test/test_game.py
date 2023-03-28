from test.fixture import run

def test_end_game():
    #given
    user_input = 'no'

    #when
    program_output = run(user_input)

    #then
    assert program_output == 'Hello! Do you want to play? YES/NO\n> Good bye!\n'