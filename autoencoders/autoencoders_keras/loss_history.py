import keras

class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, 
                       logs={}):
       self.log = []
 
    def on_epoch_end(self, 
                     batch, 
                     logs={}):
       self.log.append(logs)