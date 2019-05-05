#import reader
import tensorflow as tf
train_data ="./train_data.csv"
test_data="./test_data.csv"
#train_data = reader.ptb_raw_data(data_path)
COLUMNS = ['label', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n']
FIELD_DEFAULTS = [[0], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
def my_input_fn(file_path, perform_shuffle=False, repeat_count=1):
    
    def decode_csv(line):
        
        parse_line = tf.decode_csv(line, FIELD_DEFAULTS)
        print("hj")
        features = dict(zip(COLUMNS,parse_line))
        label = features.pop('label')
        return features, label

    dataset = (tf.data.TextLineDataset(file_path).skip(1).map(decode_csv))
    print("666")
    if perform_shuffle:
        dataset = dataset.shuffle(buffer_size=256)
    dataset= dataset.repeat(repeat_count)
    dataset = dataset.batch(325)
    iterator = dataset.make_one_shot_iterator()
    batch_features, batch_labels = iterator.get_next()
    return batch_features, batch_labels
    print("3333")
feature_columns = [tf.feature_column.numeric_column(name) for name in COLUMNS[1:]]
#feature_columns = [tf.feature_column.numeric_column("x", shape[14])]

classifier = tf.estimator.DNNClassifier(feature_columns = feature_columns, hidden_units=[12,12], n_classes=2)

classifier.train(input_fn=lambda: my_input_fn(train_data,True,1))

test_results = classifier.evaluate(input_fn=lambda: my_input_fn(test_data,False,1))
print("\nTest accuracy: %g %%" % (test_results["accuracy"]*100))

