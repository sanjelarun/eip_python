def check_valid_parenthesis(exp):
    s_cnt = m_cnt = l_cnt = 0
    for each_brac in exp:
        if s_cnt < 0 or m_cnt < 0 or l_cnt < 0:
            return False

        if each_brac == '(':
            s_cnt += 1
        elif each_brac == ")":
            s_cnt -= 1
        elif each_brac == "{":
            m_cnt += 1
        elif each_brac == "}":
            m_cnt -= 1
        elif each_brac == "[":
            l_cnt += 1
        else:
            l_cnt -= 1
    return True if s_cnt == m_cnt == l_cnt == 0 else False


print(check_valid_parenthesis("))(("))
