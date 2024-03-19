
class Livro:
   
    def __init__(self,nome,autor,avaliacao,ano_publicacao,categoria):
        """
        Inicializando a Classe Livro
        """
        self._nome = nome
        self._autor = autor
        self._avaliacao = avaliacao
        self._ano_publicacao = ano_publicacao
        self._categoria = categoria
        self._disponivel = True

   
    def __str__(self):
        """
        Representação do objeto Livro em String
        """
        return f'{self._nome.ljust(40)} | {self._autor.ljust(25)} | {self._avaliacao} | {self._ano_publicacao} | {self._categoria.ljust(20)} | {self.disponibilidade}'
    
    
    def alterar_disponibilidade(cls):
        """
        Altera a disponibilidade do Livro
        """
        if cls._disponivel: 
            cls._disponivel = False
        else:
            cls._disponivel = True
    
   
    @property
    def disponibilidade(self):
        """
        Retorna a disponibilidade do Livro
        """
        return 'Disponivel' if self._disponivel else 'Indisponivel'
    


