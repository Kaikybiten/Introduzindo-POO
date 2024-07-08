class Minha_string(str): # Lembrando que, string tambem é uma classe
    def upper(self):
        print('Super impede que uma função da classe seja sobreescrita por outra com mesmo nome')
        return super().upper()
    
palavra = Minha_string('exemplo')

print(palavra.upper())