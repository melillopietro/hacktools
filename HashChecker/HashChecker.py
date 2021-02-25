def hash_checker():
    import hashlib
    
    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                   HackTool                    |")
    print("|                                               |")
    print("+-----------------------------------------------+")
    print("|                 HASH CHECKER                  |")
    print("+-----------------------------------------------+")
    
    while True:
        
        # Dizionario con password non hashate
        passwords_file = input('\nPassword dict name [ex. common_password.txt]:\n > ')

        try:    
            with open(passwords_file, 'r') as f:
                common_passwords = f.read().splitlines()
                break
        except FileNotFoundError:
            print('\nFile not found')
        
    while True:
        
        # File contenente le password hashate     
        encrypted_password_file = input('\nFilename with encypted passwords [ex. password.txt]:\n > ')
        
        try:
            with open(encrypted_password_file, 'r') as f:
                encrypted_password_list = f.read().splitlines()
                break
        except FileNotFoundError:
            print('\nFile not found')
    
    # Scelta dell'opzione
            
    print('\nSelect hash type:\n1) MD5\n2) SHA-1\n3) SHA-224\n4) SHA-256\n5) SHA-384\n6) SHA-512\n7) ALL (not recommended)')
        
    while True:
        x = input("\n > ")
        try:
            x = int(x)
        except ValueError:
            print("\nEnter a number")
        if 1 <= x <= 7:
            break
        else:
            print("\nSelect a valid option")
    
    # Verifica presenza di password con hash MD5
    
    if x == 1:
    
        for password in common_passwords:
            hashed_md5_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            for hash in encrypted_password_list:
                if hashed_md5_password == hash:
                    print(f'\nMD5 HASH FOUND\nPassword: {password}')
    
    # Verifica presenza di password con hash SHA-1
                
    if x == 2:
        for password in common_passwords:        
            hashed_sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
            for hash in encrypted_password_list:
                if hashed_sha1_password == hash:
                    print(f'\nSHA-1 HASH FOUND\nPassword: {password}')
    
    # Verifica presenza di password con hash SHA-224
            
    if x == 3:
        for password in common_passwords:        
            hashed_sha224_password = hashlib.sha224(password.encode('utf-8')).hexdigest()
            for hash in encrypted_password_list:
                if hashed_sha224_password == hash:
                    print(f'\nSHA-224 HASH FOUND\nPassword: {password}')
    
    # Verifica presenza di password con hash SHA-256
            
    if x == 4:
        for password in common_passwords:        
            hashed_sha256_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            for hash in encrypted_password_list:
                if hashed_sha256_password == hash:
                    print(f'\nSHA-256 HASH FOUND\nPassword: {password}')

    # Verifica presenza di password con hash SHA-384

    if x == 5:
        for password in common_passwords:        
            hashed_sha384_password = hashlib.sha384(password.encode('utf-8')).hexdigest()
            for hash in encrypted_password_list:
                if hashed_sha384_password == hash:
                    print(f'\nSHA-384 HASH FOUND\nPassword: {password}')

    # Verifica presenza di password con hash SHA-512    

    if x == 6:
        for password in common_passwords:        
            hashed_sha512_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
            for hash in encrypted_password_list:
                if hashed_sha512_password == hash:
                    print(f'\nSHA-512 HASH FOUND\nPassword: {password}')

    # Verifica presenza di password con gli hash disponibili
    # Non consigliato in quanto è un procedimento pesante

    if x == 7:        
        for password in common_passwords:            
            hashed_md5_password = hashlib.md5(password.encode('utf-8')).hexdigest()    
            hashed_sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest()    
            hashed_sha224_password = hashlib.sha224(password.encode('utf-8')).hexdigest()
            hashed_sha256_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            hashed_sha384_password = hashlib.sha384(password.encode('utf-8')).hexdigest()
            hashed_sha512_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
            for hash in encrypted_password_list:
                if hashed_md5_password == hash:
                    print(f'\nMD5 HASH FOUND\nPassword: {password}')
                elif hashed_sha1_password == hash:
                    print(f'\nSHA-1 HASH FOUND\nPassword: {password}')
                elif hashed_sha224_password == hash:
                    print(f'\nSHA-224 HASH FOUND\nPassword: {password}')
                elif hashed_sha256_password == hash:
                    print(f'\nSHA-256 HASH FOUND\nPassword: {password}')
                elif hashed_sha384_password == hash:
                    print(f'\nSHA-384 HASH FOUND\nPassword: {password}')
                elif hashed_sha512_password == hash:
                    print(f'\nSHA-512 HASH FOUND\nPassword: {password}')

hash_checker()                
