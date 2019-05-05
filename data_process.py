import tensorflow as tf
import numpy as np

train_data_path='./adult.data'
test_data_path='./adult.test1'
train_filepath = './train_data.csv'
test_filepath = './test_data.csv'
def load(data_path,filepath):

    
    # 预先检测地址是否存在
    if not tf.gfile.Exists(data_path):
        tf.logging.fatal('File does not exist %s', data_path)
        return
    data_lines = tf.gfile.GFile(data_path).readlines()
    #print(len(data_lines))

    #X = np.zeros(shape=(14,1))
    

    f = open(filepath, 'w')     
    for line in data_lines:

        line = line.strip('\n')
        #line = line.replace('.','')
        #F.write(line)
        #line = line.replace(' ','')
        parse_items = line.split(',')
        print(len(parse_items))
        #print(parse_items)
        if len(parse_items)< 15:
            break
        data = [0 for n in range(15)]
        if parse_items[14] ==' <=50K':
           data[0] = 0
        elif parse_items[14] ==' >50K':
           data[0] = 1

        data[1] = int(parse_items[0])

        if parse_items[1] ==' Private':
           data[2] = 0
        elif parse_items[1] == ' Self-emp-not-inc':
           data[2] = 1
        elif parse_items[1] == ' Self-emp-inc':
            data[2] = 2
        elif parse_items[1] == ' Federal-gov':
            data[2] = 3
        elif parse_items[1] == ' Local-gov':
            data[2] = 4
        elif parse_items[1] == ' State-gov':
            data[2] = 5
        elif parse_items[1] == ' Without-pay':
            data[2] = 6
        elif parse_items[1] == ' Nerver-worked':
            data[2] = 7
        elif parse_items[1] == ' ?':
            data[2] = 8


        data[3] = int(parse_items[2])
    
        if parse_items[3] == ' Bachelors':
            data[4] = 0
        elif parse_items[3] == ' Some-college':
            data[4] = 1
        elif parse_items[3] == ' 11th':
            data[4] = 2
        elif parse_items[3] == ' HS-grade':
            data[4] = 3
        elif parse_items[3] == ' Prof-school':
            data[4] = 1
        elif parse_items[3] == ' Assoc-acdm':
            data[4] = 2
        elif parse_items[3] == ' Assoc-voc':
            data[4] = 3
        elif parse_items[3] == ' 9-th':
            data[4] = 4
        elif parse_items[3] == ' 7th-8th':
            data[4] = 5
        elif parse_items[3] == ' 12th':
            data[4] = 6
        elif parse_items[3] == ' Masters':
            data[4] = 7
        elif parse_items[3] == ' 1st-4th':
            data[4] = 8
        elif parse_items[3] == ' 10th':
            data[4] = 9
        elif parse_items[3] == ' Doctorate':
            data[4] = 10
        elif parse_items[3] == ' 5th-6th':
            data[4] = 11
        elif parse_items[3] == ' Preschool':
            data[4] = 12
        elif parse_items[3] == ' ?':
            data[4] = 13


        data[5] = int(parse_items[4])


        if parse_items[5] == ' Married-civ-spouse':
            data[6] = 0
        elif parse_items[5] == ' Divorced':
            data[6] = 1
        elif parse_items[5] == ' Nerver-married':
            data[6] = 2
        elif parse_items[5] == ' Separated':
            data[6] = 3
        elif parse_items[5] == ' Widowed':
            data[6] = 4
        elif parse_items[5] == ' Married-spouse-absent':
            data[6] = 5
        elif parse_items[5] == ' Married-AF-spouse':
            data[6] = 6
        elif parse_items[5] == ' ?':
            data[6] = 7


        if parse_items[6] == ' Tech-support':
            data[7] = 0
        elif parse_items[6] == ' Craft-repair':
            data[7] = 1
        elif parse_items[6] == ' Other-service':
            data[7] = 2
        elif parse_items[6] == ' Sales':
            data[7] = 3
        elif parse_items[6] == ' Exec-managerical':
            data[7] = 4
        elif parse_items[6] == ' Prof-specialty':
            data[7] = 5
        elif parse_items[6] == ' Handlers-cleaners':
            data[7] = 6
        elif parse_items[6] == ' Machine-op-inspct':
            data[7] = 7
        elif parse_items[6] == ' Adm-clerical':
            data[7] = 8
        elif parse_items[6] == ' Farming-fishing':
            data[7] = 9
        elif parse_items[6] == ' Transport-moving':
            data[7] = 10
        elif parse_items[6] == ' Priv-house-serv':
            data[7] = 11
        elif parse_items[6] == ' Protective-serv':
            data[7] = 12
        elif parse_items[6] == ' Armed-Forces':
            data[7] = 13
        elif parse_items[6] == ' ?':
            data[7] = 14


        if parse_items[7] == ' Wife':
            data[8] = 0
        elif parse_items[7] == ' Own-child':
            data[8] = 1
        elif parse_items[7] == ' Husband':
            data[8] = 2
        elif parse_items[7] == ' Not-in-family':
            data[8] = 3
        elif parse_items[7] == ' Other-relative':
            data[8] = 4
        elif parse_items[7] == ' Unmarried':
            data[8] = 5
        elif parse_items[7] == ' ?':
            data[8] = 6


        if parse_items[8] == ' White':
            data[9] = 0
        elif parse_items[8] == ' Asian-Pac-Islander':
            data[9] = 1
        elif parse_items[8] == ' Amer-Indian-Eskimo':
            data[9] = 2
        elif parse_items[8] == ' Other':
            data[9] = 3
        elif parse_items[8] == ' Black':
            data[9] = 4
        elif parse_items[8] == ' ?':
            data[9] = 5


        if parse_items[9] == ' Female':
            data[10] = 0
        elif parse_items[9] == ' Male':
            data[10] = 1
        elif parse_items[9] == ' ?':
            data[10] = 2

        data[11] = int(parse_items[10])

        data[12] = int(parse_items[11])

        data[13] = int(parse_items[12])


        if parse_items[13] == ' United-States':
            data[14] = 0
        elif parse_items [13] == ' Cambodia':
            data[14] = 1
        elif parse_items [13] == ' England':
            data[14] = 2
        elif parse_items [13] == ' Puerto-Rico':
            data[14] = 3
        elif parse_items [13] == ' Canada':
            data[14] = 4
        elif parse_items [13] == ' Germany':
            data[14] = 5
        elif parse_items [13] == ' Outlying-US(Guam-USVI-etc)':
            data[14] = 6
        elif parse_items [13] == ' India':
            data[14] = 7
        elif parse_items [13] == ' Japan':
            data[14] = 8
        elif parse_items [13] == ' Greece':
            data[14] = 9
        elif parse_items [13] == ' South':
            data[14] = 10
        elif parse_items [13] == ' China':
            data[14] = 11
        elif parse_items [13] == ' Cuba':
            data[14] = 12
        elif parse_items [13] == ' Iran':
            data[14] = 13
        elif parse_items [13] == ' Honduras':
            data[14] = 14
        elif parse_items [13] == ' Philippines':
            data[14] = 15
        elif parse_items [13] == ' Italy':
            data[14] = 16
        elif parse_items [13] == ' Poland':
            data[14] = 17
        elif parse_items [13] == ' Jamaica':
            data[14] = 18
        elif parse_items [13] == ' Vietnam':
            data[14] = 19
        elif parse_items [13] == ' Mexico':
            data[14] = 20
        elif parse_items [13] == ' Portugal':
            data[14] = 21
        elif parse_items [13] == ' Ireland':
            data[14] = 22
        elif parse_items [13] == ' France':
            data[14] = 23
        elif parse_items [13] == ' Dominican-Republic':
            data[14] = 24
        elif parse_items [13] == ' Laos':
            data[14] = 25
        elif parse_items [13] == ' Ecuador':
            data[14] = 26
        elif parse_items [13] == ' Taiwan':
            data[14] = 27
        elif parse_items [13] == ' Haiti':
            data[14] = 28
        elif parse_items [13] == ' Columbia':
            data[14] = 29
        elif parse_items [13] == ' Hungary':
            data[14] = 30
        elif parse_items [13] == ' Guatemala':
            data[14] = 31
        elif parse_items [13] == ' Nicaragua':
            data[14] = 32
        elif parse_items [13] == ' Scotland':
            data[14] = 33
        elif parse_items [13] == ' Thailand':
            data[14] = 34
        elif parse_items [13] == ' Yugoslavia':
            data[14] = 35
        elif parse_items [13] == ' El-Savador':
            data[14] = 36
        elif parse_items [13] == ' Trinadad&Tobago':
            data[14] = 37
        elif parse_items [13] == ' Peru':
            data[14] = 38
        elif parse_items [13] == ' Hong':
            data[14] = 39
        elif parse_items [13] == ' Holand-Netherlands':
            data[14] = 40
        elif parse_items [13] == ' ?':
            data[14] = 41
        
        #np.savez(filepath,data)
     
        #a = np.load(filepath)
        #print(a)
        
        a = str(data)
        
        f.write(a)
        f.write('\n')
    
        #print(liine)
        #print(data)
        #print(a.shape)
    f.close
    #F.close
    
"""
        item = parse_items[14]
        if item == ' >50K':
            data[14] = 1
            print("a person makes over 50K a year")
            continue
        if item == ' <=50K':
            data[14] = 0
            print("a person makes under 50k a year")
            continue

"""

def my_input_fn(data_path,filepath):
    load(data_path,filepath)

    data_lines = tf.gfile.GFile(filepath).readlines()
    f = open(filepath, 'w')
    x = np.array([[0 for i in range(54)] for j in range(32562)])
    for line in data_lines: 
      line = line.strip('[')
      line=line.replace(' ','')
      line=line.replace(']','')
      #line=line.replace(',', ' ')
      #for i in range(32562):
        #x[i] = [j for j in line[0:-2 ] ]
        #x[i][k] = [j for j in line[0:-1]]
      f.write(line)
      f.close
      #print(line)




#load(train_data_path,train_filepath)
my_input_fn(test_data_path, test_filepath)
my_input_fn(train_data_path,train_filepath)
            

