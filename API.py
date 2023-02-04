import Flask, request
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)
model = keras.models.load_model('./my_model.h5')

def predict_class(image, model):
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, [224, 224])
    image = np.expand_dims(image, axis = 0)
    prediction = model.predict(image)
    return prediction

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image'].read()
        test_image = Image.open(file)
        pred = predict_class(np.asarray(test_image), model)
        nomes_classes = ['benigno', 'maligno', 'normal']
        result = nomes_classes[np.argmax(pred)]
        output = 'Essa exame é  '  +  result
        return output

if __name__ == '__main__':
    app.run(debug=True)

#A API acima foi escrita usando o framework Streamlit e o Tensorflow. Para executar a API, siga os seguintes passos:

#Certifique-se de ter o Streamlit e o Tensorflow instalados em sua máquina.
#Salve o código acima em um arquivo com extensão .py
#Execute o código usando o comando streamlit run arquivo.py no terminal ou prompt de comando.
#Uma janela do navegador será aberta com a interface da API.
#Faça upload de uma imagem de mama clicando no botão "Upload an image of a Breast".
#A API processará a imagem e exibirá a classificação no final.
#Obs.: Tenha certeza de que você tem acesso à Internet e que o modelo já foi treinado e salvo como my_model.h5 na mesma pasta do código.