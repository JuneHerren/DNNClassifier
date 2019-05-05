import tensorflow as tf 
path = './adult.test'
newfile = './adult.test1'
F = open(newfile,'w')
data_lines = tf.gfile.GFile(path).readlines()
for line in data_lines:
    
    line=line.replace('.','')
    #F = open(newfile,'w')
    F.write(line)
F.close
