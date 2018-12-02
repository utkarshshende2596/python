def fun(s):
    flag=0
    username,domain=s.split('@')
    domain_1,domain_2=domain.split('.')

    if '_'or'-'or'.' in username:
        flag=1
    




fun('utkarsh_shende@persi.com')