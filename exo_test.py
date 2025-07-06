from exo import est_pair, convert_to_hour, convert_list

def exo(n):
    return 0

def test_est_pair():
    assert est_pair(2) == True
    assert est_pair(3) == False
    assert est_pair(0) == True
    assert est_pair(-2) == True
    assert est_pair(-3) == False
    assert est_pair(1000000) == True

def test_convert_to_hour():
    assert convert_to_hour(120) == "2 hour(s) and 0 minute(s)"
    assert convert_to_hour(61) == "1 hour(s) and 1 minute(s)"
    assert convert_to_hour(59) == "0 hour(s) and 59 minute(s)"
    assert convert_to_hour(0) == "0 hour(s) and 0 minute(s)"
    assert convert_to_hour(-10) == "error"
    assert convert_to_hour("3600") == "error"

def test_convert_list():
    list, list2 = [120, 61, 59], [0, -10, "3600"]
    assert convert_list(list) == ["2 hour(s) and 0 minute(s)", "1 hour(s) and 1 minute(s)", "0 hour(s) and 59 minute(s)"]
    assert convert_list(list2) == ["0 hour(s) and 0 minute(s)", "error", "error"]

if __name__ == "__main__":
    exo()
    