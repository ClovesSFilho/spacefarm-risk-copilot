# SpaceFarm Risk Copilot

**Aluno:** Cloves Silva Filho  
**RM:** 567250  
**Curso:** Inteligência Artificial - FIAP  
**Atividade:** Substitutiva Global Solution 2026.1  

## 1. Introdução

Este projeto apresenta uma POC de Inteligência Artificial aplicada à nova economia espacial. A ideia é mostrar como dados climáticos e espaciais podem apoiar decisões agrícolas na Terra.

## 2. Problema

A agricultura depende de fatores como temperatura, chuva, umidade do solo, vento e radiação solar. Quando esses dados não são transformados em decisão prática, o produtor pode demorar para agir diante de risco de seca, calor extremo ou baixa umidade.

## 3. Solução

O SpaceFarm Risk Copilot lê dados climáticos de uma fazenda, calcula um índice de risco agrícola, classifica o risco com Machine Learning e apresenta uma recomendação operacional em um dashboard.

Tecnologias usadas:

- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly

## 4. Arquitetura

Fluxo da solução:

1. Entrada de dados climáticos/espaciais.
2. Tratamento dos dados em Python.
3. Cálculo do índice de risco.
4. Classificação com modelo de Machine Learning.
5. Exibição em dashboard.
6. Geração de recomendação e alerta simulado.

Em uma versão futura, os dados poderiam vir de APIs climáticas, sensores IoT ou produtos de satélite, com alertas enviados por serviços de nuvem como AWS Lambda e SNS.

## 5. Desenvolvimento

O motor de risco combina temperatura, umidade do solo, chuva, radiação solar e vento. Cada variável contribui para um score final de 0 a 100.

Trecho principal do cálculo:

```python
weighted_score = (
    heat * 0.26
    + drought * 0.28
    + rain_deficit * 0.18
    + radiation * 0.16
    + wind * 0.12
) * 100
```

Para a classificação, foi usado um modelo Random Forest:

```python
model = RandomForestClassifier(n_estimators=120, random_state=42, max_depth=4)
model.fit(data[FEATURES], data["risk_level"])
```

Quando o risco é alto, o sistema gera uma recomendação simples:

```python
return "Acionar irrigação prioritária e enviar alerta técnico."
```

## 6. Resultados Esperados

A POC entrega:

- dashboard com indicadores de risco;
- gráfico de evolução do índice;
- tabela com dados monitorados;
- classificação do risco em baixo, médio ou alto;
- recomendação operacional;
- alerta simulado para equipe da fazenda.

## 7. Limitações

O projeto usa um dataset simplificado para ser viável no prazo da atividade. Ele não substitui uma solução agrícola profissional. O objetivo é demonstrar, de forma funcional, como IA, dados climáticos e dashboard podem apoiar uma decisão real.

## 8. Conclusão

O SpaceFarm Risk Copilot mostra como tecnologias digitais e dados ligados à economia espacial podem gerar impacto positivo na Terra. Mesmo em formato de POC, a solução demonstra uma aplicação prática de IA para agricultura, prevenção de perdas e tomada de decisão.

## 9. Link

Repositório GitHub: https://github.com/ClovesSFilho/spacefarm-risk-copilot
