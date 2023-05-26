"""
    O termo SOLID é o acrônimo para os cinco princípios da POO, a saber:
    S de Single Responsibility Principle (Princípio da Responsabilidade Única); 
    O de Open-Closed Principle (Princípio Aberto-Fechado); 
    L de Liskov Substitution Principle (Princípio da Substituição de Liskov);
    I de Interface Segregation Principle (Princípio da Segregação da Interface);
    D de Dependency Inversion Principle (Princípio da Inversão da Dependência);
"""

class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__capturar_error()

    # __ -> defini que este método é privado
    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False
        
    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print('Acessando o banco de dados...')
        print('Cadastrar o usuario {}, idade {}'.format(nome, idade))

    def __capturar_error(self) -> None:
        print('Dados inválidos...')