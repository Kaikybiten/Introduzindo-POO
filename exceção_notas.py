class NotesError(Exception):
    ...

excecao = NotesError('Exemplo notas de error')
excecao.add_note('Essa é a primeira nota do erro')
excecao.add_note('Essa é a segunda nota do erro')

raise excecao