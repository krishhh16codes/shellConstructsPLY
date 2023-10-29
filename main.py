import lexFile
data='''one is the number'''
lexFile.lexer.input(data)
while True:
    tok=lexFile.lexer.token()
    if not tok:
        break
    print(tok)    

