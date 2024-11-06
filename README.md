# IndependenteHTML

IndependenteHTML é um projeto para baixar e processar HTML, transformando-o em um site independente, onde os recursos externos como CSS, JavaScript e imagens são baixados localmente e referenciados no HTML. Além disso, ele inclui uma funcionalidade para carregar conteúdo dinâmico a partir de um arquivo JSON.

## Estrutura do Projeto

```plaintext
IndependenteHTML/
├── css/
│   └── (arquivos CSS baixados)
├── js/
│   ├── dados.json
│   └── (arquivos JavaScript baixados)
├── imagens/
│   └── (imagens baixadas)
├── index.html
└── script.py
```

## Dependências

- Python 3.x
- Bibliotecas Python:
  - `os`
  - `re`
  - `requests`
  - `beautifulsoup4`
  - `json`

## Instalação

Antes de executar o script, certifique-se de instalar as bibliotecas necessárias:


pip install requests beautifulsoup4
Funcionalidades
1. Baixar Recursos
A função baixar_recurso(url, pasta_destino) baixa um recurso (CSS, JS, imagem) a partir de uma URL e salva-o em uma pasta especificada localmente. Ela remove parâmetros de URL e mantém apenas o nome do arquivo.

2. Processar HTML
A função processar_html(html) processa o HTML para torná-lo independente:

Baixa e substitui links de CSS.

Baixa e substitui links de JavaScript.

Baixa e substitui links de imagens.

Adiciona um script para carregar conteúdo dinâmico de um arquivo JSON.

3. Salvar Site
A função salvar_site(html_processado) salva o HTML processado em um arquivo index.html e o conteúdo dinâmico em um arquivo js/dados.json.

Uso
A função principal main() deve ser executada para processar e salvar o site.

python
if __name__ == "__main__":
    main()
Exemplo de Uso
Copie o HTML desejado no espaço indicado em html_copiado na função main().

Execute o script script.py.

Verifique a pasta do projeto para ver o HTML processado e os recursos baixados.
