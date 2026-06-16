# SpaceFarm Risk Copilot

**Aluno:** Cloves Silva Filho  
**RM:** 567250  
**Curso:** Inteligência Artificial - FIAP  
**Atividade:** Substitutiva Global Solution 2026.1  

## 1. Introdução

Este projeto apresenta uma POC de Inteligência Artificial aplicada à nova economia espacial. A ideia é usar dados climáticos e espaciais para apoiar decisões agrícolas na Terra.

## 2. Problema

A agricultura depende de temperatura, chuva, umidade do solo, vento e radiação solar. O problema é transformar esses dados em decisão prática antes que o risco gere perda.

## 3. Solução

O SpaceFarm Risk Copilot lê dados climáticos, calcula um índice de risco agrícola, classifica o risco com Machine Learning e apresenta uma recomendação em um dashboard.

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

Em uma versão futura, os dados poderiam vir de APIs climáticas, sensores IoT ou produtos de satélite.

## 5. Desenvolvimento

O motor de risco combina temperatura, umidade do solo, chuva, radiação solar e vento em um score de 0 a 100.

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

O projeto usa um dataset simplificado para ser viável no prazo da atividade. Ele não substitui uma solução agrícola profissional; demonstra uma aplicação funcional de IA e dados climáticos.

## 8. Conclusão

O SpaceFarm Risk Copilot mostra como dados ligados à economia espacial podem gerar impacto positivo na Terra, especialmente na agricultura e na prevenção de perdas.

## 9. Link

Repositório GitHub: https://github.com/ClovesSFilho/spacefarm-risk-copilot
