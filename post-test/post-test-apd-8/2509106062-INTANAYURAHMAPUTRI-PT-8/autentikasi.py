def login(akun_data, clearScreen, jeda, inquirer):
    clearScreen()
    print("=== MASUK KE AKUN ===\n")
    
    login_questions = [
        inquirer.Text('username',
            message="Username",
            validate=lambda _, x: len(x) > 0
        ),
        inquirer.Text('password',
            message="Password",
            validate=lambda _, x: len(x) > 0
        )
    ]
    
    login_answers = inquirer.prompt(login_questions)
    if not login_answers:
        return None, None
        
    usn = login_answers['username']
    pw = login_answers['password']
    
    if usn == akun_data['admin']['username'] and pw == akun_data['admin']['password']:
        return 'admin', usn
    
    for user in akun_data['pengguna']:
        if user['username'] == usn and user['password'] == pw:
            return 'pengguna', usn
            
    print("\nUsername atau password salah (｡•̀ ⤙ •́ ｡ꐦ) !!!")
    jeda()
    return None, None