import os
import re
import requests
from bs4 import BeautifulSoup
import json

# Função para baixar um recurso e salvá-lo localmente, removendo parâmetros de URL
def baixar_recurso(url, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Remover parâmetros de URL e manter apenas o nome do arquivo
    nome_arquivo = url.split('/')[-1].split('?')[0]
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
    
    try:
        resposta = requests.get(url)
        with open(caminho_completo, 'wb') as f:
            f.write(resposta.content)
        print(f"Baixado: {url}")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")
    
    return caminho_completo

# Função para processar o HTML e torná-lo independente
def processar_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Baixar e substituir CSS
    for link in soup.find_all('link', {'rel': 'stylesheet'}):
        href = link.get('href')
        if href.startswith('http'):
            caminho_local = baixar_recurso(href, 'css')
            link['href'] = caminho_local

    # Baixar e substituir JavaScript
    for script in soup.find_all('script', src=True):
        src = script.get('src')
        if src.startswith('http'):
            caminho_local = baixar_recurso(src, 'js')
            script['src'] = caminho_local

    # Baixar e substituir imagens
    for img in soup.find_all('img'):
        src = img.get('src')
        if src.startswith('http'):
            caminho_local = baixar_recurso(src, 'imagens')
            img['src'] = caminho_local

    # Inserir um script para carregar conteúdo dinâmico de um JSON
    conteudo_dinamico_script = '''
    <script>
    document.addEventListener("DOMContentLoaded", () => {
        fetch('js/dados.json')
            .then(response => response.json())
            .then(data => {
                const postsDiv = document.getElementById('posts');
                data.posts.forEach(post => {
                    const postElement = document.createElement('article');
                    postElement.innerHTML = `<h2>${post.titulo}</h2><p>${post.conteudo}</p>`;
                    postsDiv.appendChild(postElement);
                });
            })
            .catch(error => console.error("Erro ao carregar dados:", error));
    });
    </script>
    '''
    soup.body.append(BeautifulSoup(conteudo_dinamico_script, 'html.parser'))
    
    # Retornar o HTML modificado
    return soup.prettify()

# Função para salvar HTML e arquivos JSON dinâmicos
def salvar_site(html_processado):
    # Salvar o HTML processado
    with open("index.html", "w", encoding="utf-8", errors="ignore") as f:
        f.write(html_processado)
    print("Arquivo index.html salvo.")

    # Salvar conteúdo dinâmico como JSON
    conteudo_dinamico = {
        "posts": [
            {"titulo": "Post de Exemplo 1", "conteudo": "Este é o conteúdo do post 1, carregado de JSON."},
            {"titulo": "Post de Exemplo 2", "conteudo": "Este é o conteúdo do post 2, carregado de JSON."}
        ]
    }
    if not os.path.exists("js"):
        os.makedirs("js")
    with open("js/dados.json", "w", encoding="utf-8") as f:
        json.dump(conteudo_dinamico, f, ensure_ascii=False, indent=4)
    print("Conteúdo dinâmico salvo em js/dados.json.")

# Função principal para rodar o script
def main():
    # HTML que você copiou do `Ctrl + U`
    html_copiado = r'''
    <!-- Cole seu HTML aqui -->
    '''

    # Processar o HTML para torná-lo independente
    html_processado = processar_html(html_copiado)

    # Salvar os arquivos do site
    salvar_site(html_processado)

# Executar o script
if __name__ == "__main__":
    main()
