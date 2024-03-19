from livros_util import Livro

class Payload:
    """
    Classe para representar um conjunto de livros
    """
    def __init__(self):
        """
        Inicializa o objeto Payload
        """
        self._livros = []
        self._carregar_livros()

   
    def _carregar_livros(self):
        """
        Método que pré-carrega os livros em uma lista
        """
        livro10 = Livro("A Metamorfose", "Franz Kafka", 4.4, 1915, "Ficção") 
        livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 4.8, 1943, "Infantil")
        livro6 = Livro("Dom Quixote", "Miguel de Cervantes", 4.9, 1605, "Ficção")
        livro10.alterar_disponibilidade()
        livro6.alterar_disponibilidade()
        livro3.alterar_disponibilidade()
        self._livros = [
            Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 4.7, 1997, "Fantasia"),
            Livro("1984", "George Orwell", 4.5, 1949, "Ficção Científica"),
            livro3,
            Livro("A Culpa é das Estrelas", "John Green", 4.2, 2012, "Romance"),
            Livro("O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 4.9, 1954, "Fantasia"),
            livro6,
            Livro("Orgulho e Preconceito", "Jane Austen", 4.5, 1813, "Romance"),
            Livro("Cem Anos de Solidão", "Gabriel García Márquez", 4.8, 1967, "Realismo Mágico"),
            Livro("Crime e Castigo", "Fiódor Dostoiévski", 4.6, 1866, "Ficção"),
            livro10
        ]
    def listar_livros(self):
        """
        Mostra os detalhes de todos os livros
        """
        for livro in self._livros:
            print(livro)
            
    def buscar_livro_por_nome(self, nome):
        """
        Busca um livro pelo nome

        Args:
            nome (str): O nome do livro a ser buscado.

        Returns:
            Livro: O livro encontrado com o nome fornecido, se existir; caso contrário, retorna None.
        """
        for livro in self._livros:
            if nome == livro._nome:
                return livro
        
    