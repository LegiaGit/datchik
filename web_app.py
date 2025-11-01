import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load('datchik.joblib')

st.title('Прогнозирование цены доставки груза')
st.write('Введите параметры для рассчета:')

volume = st.number_input(label='Объем, м3', min_value=0.00, max_value=99999.00, value=0.00)
weight = st.number_input(label='Вес, кг', min_value=0, max_value=99999, value=0)
distance = st.number_input(label='Расстояние, км', min_value=0, max_value=99999, value=0)
pallets = st.number_input(label='Паллеты, шт', min_value=0, max_value=99999, value=0)
boxes= st.number_input(label='Коробки, шт', min_value=0, max_value=99999, value=0)

if st.button('Рассчитать стоимость'):
    # Подготовка данных
    input_data = pd.DataFrame({'volume': [volume],
                               'weight': [weight],
                               'distance': [distance],
                               'pallets': [pallets],
                               'boxes': [boxes]})
    
    # Предсказание
    prediction = model.predict(input_data)
    
    st.success(f'Предсказание: {prediction[0]:.2f} EUR')