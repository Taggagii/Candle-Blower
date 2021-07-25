import tensorflow as tf

def inference(model, img):
	return model.predict(img)
