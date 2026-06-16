# SpaceFarm Risk Copilot

**Aluno:** Cloves Silva Filho  
**RM:** 567250  
**Curso:** Inteligência Artificial - FIAP  
**Atividade:** Substitutiva Global Solution 2026.1  

## 1. Introdução

A exploração espacial deixou de ser apenas uma área científica distante. Satélites, sensores orbitais e infraestrutura de comunicação já apoiam previsão climática, monitoramento ambiental, agricultura, prevenção de desastres e análise de grandes volumes de dados. A nova economia espacial cria oportunidades para transformar informações captadas acima da Terra em decisões práticas para quem vive e produz nela.

Este projeto responde à seguinte pergunta: como a Inteligência Artificial e as tecnologias digitais podem transformar a nova economia espacial e gerar impacto positivo na Terra?

## 2. Problema

O setor agrícola depende diretamente de condições climáticas. Temperatura alta, baixa umidade do solo, ausência de chuva, vento e radiação solar intensa podem reduzir produtividade e aumentar desperdícios. O problema não é apenas coletar dados: o desafio é transformar dados em decisão compreensível e acionável.

## 3. Proposta da solução

O SpaceFarm Risk Copilot é uma prova de conceito de IA que transforma dados climáticos e espaciais em um índice de risco agrícola. A solução lê dados de uma fazenda, calcula um score de risco, classifica esse risco com Machine Learning e recomenda uma ação operacional.

Na prática, o sistema funciona como uma camada de decisão para agricultura inteligente.

## 4. Arquitetura

Fluxo principal:

1. Dados climáticos/espaciais entram no sistema.
2. Um pipeline Python organiza as variáveis.
3. O motor de risco calcula um índice de 0 a 100.
4. Um modelo de Machine Learning classifica o risco como baixo, médio ou alto.
5. Um dashboard apresenta gráficos e recomendações.
6. Um serviço de alerta simulado mostra como a solução poderia acionar equipes em campo.

Evolução em nuvem:

- APIs climáticas ou produtos de satélite como fonte de dados.
- AWS Lambda para processamento periódico.
- AWS S3 para armazenamento histórico.
- AWS SNS para alertas por e-mail ou SMS.

## 5. Desenvolvimento

O projeto foi desenvolvido em Python com Streamlit, Pandas, Scikit-learn e Plotly.

### Motor de risco

O índice combina temperatura, umidade do solo, déficit de chuva, radiação solar e vento. Cada variável recebe um peso proporcional ao impacto esperado sobre a plantação. A fase da cultura também altera a sensibilidade do risco.

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

O classificador Random Forest usa as variáveis climáticas para aprender a classificação de risco. Para uma POC acadêmica, essa abordagem é suficiente porque é interpretável, robusta e fácil de demonstrar.

```python
model = RandomForestClassifier(n_estimators=120, random_state=42, max_depth=4)
model.fit(data[FEATURES], data["risk_level"])
```

### Recomendação automática

O sistema transforma o risco em uma decisão prática. Exemplo: quando há risco alto, solo seco e temperatura elevada, a recomendação é acionar irrigação prioritária e enviar alerta técnico.

```python
if risk_level == "Alto" and soil < 25 and temp >= 34:
    return "Acionar irrigação prioritária e enviar alerta técnico."
```

## 6. Resultados esperados

A POC entrega:

- Dashboard com indicadores de risco.
- Gráfico de evolução do índice.
- Tabela de dados monitorados.
- Recomendação operacional baseada no risco.
- Alerta simulado para equipe da fazenda.

Um exemplo de leitura gerada pelo sistema:

> Índice alto causado por temperatura elevada, solo seco e ausência de chuva. Ação recomendada: irrigação prioritária e alerta técnico.

## 7. Limitações

O projeto usa um dataset simplificado para manter a execução viável dentro do prazo acadêmico. A solução não tem a pretensão de substituir uma plataforma agrícola profissional. Seu objetivo é demonstrar, de forma funcional, como IA, dados climáticos, arquitetura em nuvem e automação podem ser combinados para resolver um problema real.

## 8. Conclusão

O SpaceFarm Risk Copilot mostra como a nova economia espacial pode gerar impacto positivo na Terra. Dados que antes ficavam restritos à observação e análise técnica podem ser transformados em apoio direto à decisão agrícola. Com IA, dashboard e alertas, a tecnologia espacial deixa de ser abstrata e se torna uma ferramenta prática para sustentabilidade, produtividade e prevenção de perdas.

## 9. Links

- Repositório GitHub: https://github.com/ClovesSFilho/spacefarm-risk-copilot
