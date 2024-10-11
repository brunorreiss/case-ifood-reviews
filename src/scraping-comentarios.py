from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
import pandas as pd

# Definir os dicionários de pesos
pesos_categorias = {
    "Aplicativos": 10.00,
    "Delivery Alimentação": 9.92,
    "Não encontrei meu pr...": 9.08,
    "Problemas com o Aten...": 8.50,
    "Redes de fast food": 7.65,
    "Problemas com o Site": 7.52,
    "Não categorizado": 7.37,
    "Meios de pagamentos ...": 6.98,
    "Restaurantes": 6.66,
    "Supermercados": 6.56,
    "Diversos": 6.37,
    "Financeiras": 6.32,
    "Logística e Entrega ...": 6.03,
    "Problemas na Loja": 5.46,
    "Hipermercados": 5.29,
    "Cartões de Crédito": 5.21,
    "Atendimento para Con...": 4.64,
    "Lanchonetes": 4.47,
    "Bancos": 4.41,
    "Anúncios e Classific...": 4.21,
    "Docerias e Cafeteria...": 3.90,
    "Farmácias": 3.68,
    "Sites e portais": 3.34,
    "Marketplace": 3.28,
    "Embalagens": 2.87,
    "Sorveterias": 2.71,
    "Cartões de benefício...": 2.65,
    "Bomboniere": 2.07,
    "Concessionárias de S...": 1.99,
    "Serviços para Empres...": 1.98,
    "Internet Banking": 1.83,
    "Laticínios e Lácteos": 1.83,
    "Contact Center": 1.72,
    "Bebidas": 1.56,
    "Pets Alimentos": 1.44,
    "Clubes de Compras e ...": 1.43,
    "Higiene e Limpeza Pe...": 1.34,
    "Softwares": 1.10,
    "Mercearia": 0.78,
    "Hortifruti e Ovos": 0.66,
    "Nutrição Infantil": 0.62,
    "Bebidas alcoólicas": 0.38,
    "Sorvetes": 0.38,
    "Pets Produtos e Aces...": 0.14,
    "Troca de Fraldas": 0.08,
    "Comparadores de Preç...": 0.02,
    "Suplementos Alimenta...": 0.00,
    "Postos de combustíve...": 0.00,
    "Utilidades doméstica...": 0.00
}

pesos_produtos_servicos = {
    "Problemas Gerais": 10.00,
    "Outro Tipo de produt...": 7.60,
    "Acesso ao Cadastro": 5.10,
    "Problemas com o esta...": 4.89,
    "Canais de Atendiment...": 4.82,
    "Serviço de Entrega": 4.31,
    "Equipe de Atendiment...": 4.23,
    "Pagamentos e Documen...": 4.07,
    "Propaganda Enganosa": 2.94,
    "Supermercados": 2.81,
    "Financeiras": 0.65,
    "Entrega": 0.47,
    "Salgados e aperitivo...": 0.45,
    "Comidas-Aperitivos": 0.44,
    "Hipermercados": 0.38,
    "Cartão de crédito": 0.37,
    "Pagamentos eletrônic...": 0.34,
    "Sites e portais": 0.31,
    "Atendimento na Loja": 0.20,
    "Lanches": 0.15,
    "Aparelhos": 0.09,
    "Atendimento": 0.09,
    "Conta": 0.07,
    "Múltiplo (Débito e c...": 0.06,
    "Bebidas": 0.05,
    "Sorvete": 0.04,
    "Navegabilidade": 0.03,
    "Cartões de benefício...": 0.02,
    "Medicamentos e Vitam...": 0.02,
    "Bolos e tortas": 0.00,
    "Farmácias": 0.00,
    "Chocolates e bombons": 0.00,
    "Bonecos e Bonecas": 0.00,
    "Cartão de débito": 0.00,
    "Ração": 0.00,
    "Cadastro e Assinatur...": 0.00,
    "Sorvete de massa": 0.00,
    "Fraldas": 0.00,
    "B2B": 0.00,
    "Leites e Fórmulas In...": 0.00,
    "Docinhos": 0.00,
    "Marmita": 0.00,
    "Ovos de Páscoa": 0.00,
    "Leite": 0.00,
    "Refrigerante": 0.00,
    "Pizzas": 0.00,
    "Panetone e colombas": 0.00,
    "Frutas": 0.00
}

pesos_problemas = {
    "Estorno do valor pag...": 10.00,
    "Dificuldade de cadas...": 9.65,
    "Outro problema": 9.06,
    "Mau Atendimento": 8.76,
    "Login-Senha": 8.70,
    "Problemas na finaliz...": 8.53,
    "Qualidade do serviço": 8.51,
    "Cobrança indevida": 8.40,
    "Propaganda enganosa": 8.38,
    "Atraso na entrega": 7.58,
    "Não consigo cancelar": 7.37,
    "Mau atendimento no S...": 7.28,
    "Qualidade do produto": 6.28,
    "Produto com defeito": 5.78,
    "Cobrança duplicada": 5.46,
    "Fila para acessar o ...": 5.15,
    "Produto errado": 4.83,
    "Qualidade do serviço...": 4.53,
    "Site fora do ar-Lent...": 4.48,
    "Valor abusivo": 3.85,
    "Produto não recebido": 3.73,
    "Instalação-Reparo nã...": 3.72,
    "Problema com entrega...": 3.62,
    "Mau atendimento do p...": 3.60,
    "Sorteios-Concursos": 3.53,
    "Baixa Qualidade": 3.41,
    "Entrega faltando ite...": 2.98,
    "Divergência de valor...": 1.97,
    "Produtos estragados": 1.92,
    "Demora no atendiment...": 1.92,
    "Conteúdo menor que o...": 1.56,
    "Má qualidade": 1.54,
    "Funcionários desprep...": 1.50,
    "Forma de pagamento i...": 1.41,
    "Comportamento do pro...": 1.35,
    "Demora na execução": 1.27,
    "Promoções": 1.24,
    "Estorno do valor pag...": 1.23,
    "Não atende": 1.22,
    "Produto com defeito": 1.20,
    "Produto indisponível": 0.99,
    "Débito indevido": 0.83,
    "Consistência estranh...": 0.49,
    "Estorno do valor pag...": 0.45,
    "Loja desorganizada": 0.41,
    "Troca-Devolução de p...": 0.08,
    "Roubo-Furto": 0.00
}

# Configurar o Selenium
options = Options()
options.headless = True  # Modo headless
options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# URL inicial
url_inicial = "https://www.reclameaqui.com.br/empresa/ifood/lista-reclamacoes/"

# Lista para armazenar os comentários coletados
comentarios_coletados = []

try:
    # Acessar a página inicial
    driver.get(url_inicial)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'filter-diderot')))

    # Encontrar o container dos filtros
    filtros_container = driver.find_element(By.ID, 'filter-diderot')

    # Encontrar todos os grupos de filtros
    grupos_filtros = filtros_container.find_elements(By.CSS_SELECTOR, 'div.sc-1h9pg1g-5')

    # Dicionário para armazenar os filtros por categoria
    todos_os_filtros = {}

    for grupo in grupos_filtros:
        # Obter o título do grupo de filtros
        titulo_element = grupo.find_element(By.CSS_SELECTOR, 'h6.sc-1h9pg1g-6')
        titulo_grupo = titulo_element.text.strip()

        # Ignorar os filtros especiais
        if titulo_grupo.lower() == 'filtros especiais':
            continue

        # Expandir o filtro, se houver o botão "Ver mais"
        try:
            ver_mais_botao = grupo.find_element(By.XPATH, './/button[span[text()="Ver mais"]]')
            driver.execute_script("arguments[0].click();", ver_mais_botao)
            time.sleep(1)
        except:
            pass

        # Encontrar todas as opções dentro do grupo
        opcoes = grupo.find_elements(By.CSS_SELECTOR, 'div.sc-1h9pg1g-7')

        # Lista para armazenar as opções deste grupo
        opcoes_grupo = []

        for opcao in opcoes:
            # Obter o label da opção
            label_element = opcao.find_element(By.CSS_SELECTOR, 'label.sc-imwsjW')
            nome_opcao = label_element.text.strip()
            opcoes_grupo.append((label_element, nome_opcao))

        # Armazenar as opções no dicionário
        todos_os_filtros[titulo_grupo] = opcoes_grupo

    # Iterar sobre cada filtro e coletar os comentários
    for titulo_grupo, opcoes in todos_os_filtros.items():
        print(f"Processando grupo de filtros: {titulo_grupo}")

        for label_element, nome_opcao in opcoes:
            print(f" - Aplicando filtro: {nome_opcao}")

            # Recarregar a página inicial para limpar filtros anteriores
            driver.get(url_inicial)
            wait.until(EC.presence_of_element_located((By.ID, 'filter-diderot')))

            # Expandir o grupo atual novamente (se necessário)
            try:
                grupo_atual = driver.find_element(By.XPATH, f'//h6[text()="{titulo_grupo}"]/ancestor::div[contains(@class, "sc-1h9pg1g-5")]')
                ver_mais_botao = grupo_atual.find_element(By.XPATH, './/button[span[text()="Ver mais"]]')
                driver.execute_script("arguments[0].click();", ver_mais_botao)
                time.sleep(1)
            except:
                pass

            # Reencontrar o label da opção
            try:
                label_element = driver.find_element(By.XPATH, f'//label[text()="{nome_opcao}"]')
            except:
                print(f"   * Opção {nome_opcao} não encontrada. Pulando...")
                continue

            # Selecionar o checkbox associado
            try:
                checkbox = label_element.find_element(By.XPATH, '../input')
                driver.execute_script("arguments[0].click();", checkbox)
            except:
                print(f"   * Checkbox para {nome_opcao} não encontrado. Pulando...")
                continue

            # Confirmar os filtros selecionados
            try:
                botao_confirmar = driver.find_element(By.XPATH, '//button[span[text()="Confirmar"]]')
                driver.execute_script("arguments[0].click();", botao_confirmar)
            except:
                print("   * Botão 'Confirmar' não encontrado. Pulando...")
                continue

            # Aguardar o carregamento dos resultados
            try:
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-1pe7b5t-0')))
            except:
                print("   * Comentários não carregaram. Pulando...")
                continue

            # Coletar os comentários das primeiras 10 páginas
            for pagina in range(1, 11):
                print(f"   * Coletando comentários da página {pagina}")

                # Aguardar os comentários carregarem
                time.sleep(2)

                # Obter o código-fonte atualizado
                html_pagina = driver.page_source
                soup = BeautifulSoup(html_pagina, 'html.parser')

                # Encontrar todos os comentários
                comentarios = soup.find_all('div', class_='sc-1pe7b5t-0')

                # Filtrar os comentários com a flag "Não respondida"
                for comentario in comentarios:
                    status_element = comentario.find('span', class_='sc-1pe7b5t-4')
                    if status_element and 'Não respondida' in status_element.text:
                        titulo_comentario = comentario.find('h4').text.strip()
                        texto_comentario = comentario.find('p').text.strip()
                        
                        # Obter os pesos
                        peso_categoria = pesos_categorias.get(nome_opcao, 0.0)

                        # Adicionar ao JSON
                        comentarios_coletados.append({
                            'titulo': titulo_comentario,
                            'texto': texto_comentario,
                            'pontuacao_comentario': str(peso_categoria),  # Convertido para string conforme o exemplo
                            'categoria': nome_opcao
                        })

                # Verificar se há uma próxima página
                try:
                    botao_proxima_pagina = driver.find_element(By.XPATH, '//button[@data-testid="next-page-navigation-button"]')
                    if not botao_proxima_pagina.is_enabled():
                        break
                    driver.execute_script("arguments[0].click();", botao_proxima_pagina)
                except:
                    break  # Se não encontrar o botão, sai do loop

    # Salvar os comentários em um arquivo JSON
    with open('comentarios_coletados.json', 'w', encoding='utf-8') as f:
        json.dump(comentarios_coletados, f, ensure_ascii=False, indent=4)


    # Converter para DataFrame do pandas
    df = pd.DataFrame(comentarios_coletados)

    # Salvar em CSV
    df.to_csv('comentarios_coletados.csv', index=False, encoding='utf-8-sig')

    # Salvar em Excel
    df.to_excel('comentarios_coletados.xlsx', index=False, engine='openpyxl')

    print("Coleta concluída com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    driver.quit()