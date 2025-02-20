from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder


class FormsLSTM:
	def __init__(max_len, embedding_dim, lstm_units, model_path):
		self.tokenizer = Tokenizer()
        self.label_encoder = LabelEncoder()
        self.max_len = max_len
        self.embedding_dim = embedding_dim
        self.lstm_units = lstm_units
        self.model_path = model_path

    # for processing data
    def process_form_data(self):
    	pass

    # for embeding model
    def embed_model(self):
    	pass

    def train(self):
    	pass

    def predict(self):
    	pass    