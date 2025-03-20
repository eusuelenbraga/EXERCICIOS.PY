#Oitavo Exercício: Verificador de Palíndromos

def verificar_palindromo(palavra):
    
    palavra = palavra.lower() 
    return palavra == palavra[::-1]  

print(verificar_palindromo("Suelen")) 
print(verificar_palindromo("kaka"))
print(verificar_palindromo("ovo"))
print(verificar_palindromo("sopapos"))
print(verificar_palindromo("VaiNaWeb"))
print(verificar_palindromo("Python"))
print(verificar_palindromo("SocorroDeus"))
print(verificar_palindromo("arara"))