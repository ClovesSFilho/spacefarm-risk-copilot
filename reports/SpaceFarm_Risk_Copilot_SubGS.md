# SpaceFarm Risk Copilot

**Aluno:** Cloves Silva Filho  
**RM:** 567250  
**Curso:** Inteligencia Artificial - FIAP  
**Atividade:** Substitutiva Global Solution 2026.1  

## 1. Introducao

A exploracao espacial deixou de ser apenas uma area cientifica distante. Satelites, sensores orbitais e infraestrutura de comunicacao ja apoiam previsao climatica, monitoramento ambiental, agricultura, prevencao de desastres e analise de grandes volumes de dados. A nova economia espacial cria oportunidades para transformar informacoes captadas acima da Terra em decisoes praticas para quem vive e produz nela.

Este projeto responde a seguinte pergunta: como a Inteligencia Artificial e as tecnologias digitais podem transformar a nova economia espacial e gerar impacto positivo na Terra?

## 2. Problema

O setor agricola depende diretamente de condicoes climaticas. Temperatura alta, baixa umidade do solo, ausencia de chuva, vento e radiacao solar intensa podem reduzir produtividade e aumentar desperdicios. O problema nao e apenas coletar dados: o desafio e transformar dados em decisao compreensivel e acionavel.

## 3. Proposta da solucao

O SpaceFarm Risk Copilot e uma prova de conceito de IA que transforma dados climaticos e espaciais em um indice de risco agricola. A solucao le dados de uma fazenda, calcula um score de risco, classifica esse risco com Machine Learning e recomenda uma acao operacional.

Na pratica, o sistema funciona como uma camada de decisao para agricultura inteligente.

## 4. Arquitetura

Fluxo principal:

1. Dados climaticos/espaciais entram no sistema.
2. Um pipeline Python organiza as variaveis.
3. O motor de risco calcula um indice de 0 a 100.
4. Um modelo de Machine Learning classifica o risco como baixo, medio ou alto.
5. Um dashboard apresenta graficos e recomendacoes.
6. Um servico de alerta simulado mostra como a solucao poderia acionar equipes em campo.

Evolucao em nuvem:

- APIs climaticas ou produtos de satelite como fonte de dados.
- AWS Lambda para processamento periodico.
- AWS S3 para armazenamento historico.
- AWS SNS para alertas por e-mail ou SMS.

## 5. Desenvolvimento

O projeto foi desenvolvido em Python com Streamlit, Pandas, Scikit-learn e Plotly.

### Motor de risco

O indice combina temperatura, umidade do solo, deficit de chuva, radiacao solar e vento. Cada variavel recebe um peso proporcional ao impacto esperado sobre a plantacao. A fase da cultura tambem altera a sensibilidade do risco.

```python
weighted_score = (
    heat * 0.26
    + drought * 0.28
    + rain_deficit * 0.18
    + radiation * 0.16
    + wind * 0.12
) * 100
```

### Modelo de Machine Learning

O classificador Random Forest usa as variaveis climaticas para aprender a classificacao de risco. Para uma POC academica, essa abordagem e suficiente porque e interpretavel, robusta e facil de demonstrar.

```python
model = RandomForestClassifier(n_estimators=120, random_state=42, max_depth=4)
model.fit(data[FEATURES], data["risk_level"])
```

### Recomendacao automatica

O sistema transforma o risco em uma decisao pratica. Exemplo: quando ha risco alto, solo seco e temperatura elevada, a recomendacao e acionar irrigacao prioritaria e enviar alerta tecnico.

```python
if risk_level == "Alto" and soil < 25 and temp >= 34:
    return "Acionar irrigacao prioritaria e enviar alerta tecnico."
```

## 6. Resultados esperados

A POC entrega:

- Dashboard com indicadores de risco.
- Grafico de evolucao do indice.
- Tabela de dados monitorados.
- Recomendacao operacional baseada no risco.
- Alerta simulado para equipe da fazenda.

Um exemplo de leitura gerada pelo sistema:

> Indice alto causado por temperatura elevada, solo seco e ausencia de chuva. Acao recomendada: irrigacao prioritaria e alerta tecnico.

## 7. Limitacoes

O projeto usa um dataset simplificado para manter a execucao viavel dentro do prazo academico. A solucao nao tem a pretensao de substituir uma plataforma agricola profissional. Seu objetivo e demonstrar, de forma funcional, como IA, dados climaticos, arquitetura em nuvem e automacao podem ser combinados para resolver um problema real.

## 8. Conclusao

O SpaceFarm Risk Copilot mostra como a nova economia espacial pode gerar impacto positivo na Terra. Dados que antes ficavam restritos a observacao e analise tecnica podem ser transformados em apoio direto a decisao agricola. Com IA, dashboard e alertas, a tecnologia espacial deixa de ser abstrata e se torna uma ferramenta pratica para sustentabilidade, produtividade e prevencao de perdas.

## 9. Links

- Repositorio GitHub: preencher
- Video demonstrativo: preencher
