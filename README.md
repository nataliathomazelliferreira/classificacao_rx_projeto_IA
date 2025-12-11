Classificação de Radiografias: Bacia x Tórax

Este projeto demonstra como uma IA simples pode classificar radiografias usando apenas:

🟦 Pixels brancos (ossos)

⚫ Pixels pretos (ar)

➖ Uma reta aprendida automaticamente pelo computador


🎯 Objetivo

Separar automaticamente dois tipos de radiografias:

Bacia → mais osso (mais pixels brancos)

Tórax → mais ar (mais pixels pretos)

Cada RX vira um ponto no gráfico:

X = pixels brancos

Y = pixels pretos

A IA aprende uma reta de decisão para separar as classes.


⚠️ Usamos radiografias reais, mas não podemos divulgar as imagens. Apenas os gráficos e resultados são compartilhados.


🧠 Como funciona

Cada RX é convertida para escala de cinza

Contamos:

Pixels claros → osso → eixo X

Pixels escuros → ar → eixo Y

Cada imagem vira um ponto no plano cartesiano → classificação com uma reta.


⛰️ Aprendizado: Descida da Colina

Começa com uma reta aleatória

Testa pequenas mudanças

Mantém a reta que erra menos

Repete até encontrar a melhor solução

Simples, passo a passo, chamado Hill Climbing.

📊 Resultados

🔵 Azul → Bacia

🔴 Vermelho → Tórax

🟢 Verde → Reta de decisão aprendida

Pontos acima da reta → Tórax

Pontos abaixo da reta → Bacia

Também há uma demonstração animada mostrando a reta se movendo e ajustando a classificação.

*Todos os gráficos são gerados a partir da análise das radiografias reais, sem divulgar imagens originais.*


🗂️ Estrutura do Projeto
├── leitor_pixels.py                     # Extrai pixels das RX
├── classificador_bacia_torax_descida_colina.py  # IA que aprende a reta
├── colina_grafico.py                    # Gera gráfico final
├── reta_movendo.py                      # Demonstração da reta se movendo
└── imagens_rx/                          # Radiografias usadas (não incluídas)


▶️ Como executar

Instale Python 3

Instale Matplotlib:

pip install matplotlib


Execute os scripts na ordem:

leitor_pixels.py → extrai pixels

classificador_bacia_torax_descida_colina.py → treina a reta

colina_grafico.py → mostra gráfico final

reta_movendo.py → demonstra a reta animada


📚 Conclusão

É possível criar um classificador de radiografias real usando:

Matemática simples

Contagem de pixels

Uma reta

Uma técnica básica de otimização

💡 Uma forma didática e acessível de entender modelos lineares de IA na prática, sem redes neurais ou bibliotecas complexas.
