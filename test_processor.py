import pytest
from hypothesis import given, strategies as st
from processor import sanitize_string, parse_int_list, reverse_words

@given(st.text() | st.none())
def test_sanitize_string_no_crash(s):
    # To-Do:Using try and except complete this function.
    try:
        sanitize_string(s)
    except Exception as e:
        pytest.fail(f"sanitize_string crashed with input={s!r}: {e}")
    
@given(st.text() | st.none())
def test_parse_int_list_safe(s):
    # To-Do:Using try and except complete this function.
    try:
        parse_int_list(s)
    except Exception as e:
        pytest.fail(f"parse_int_list crashed with input={s!r}: {e}")


@given(st.text() | st.none())
def test_reverse_words_safe(s):
    # To-Do:Using try and except complete this function.
    try:
        reverse_words(s)
    except Exception as e:
        pytest.fail(f"reverse_words crashed with input={s!r}: {e}")