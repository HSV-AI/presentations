from hsvai import Doc2VecRec    

rec = Doc2VecRec('data/bugzilla.doc2vec')

# rec.load('data/bugzilla.doc2vec')
rec.recommendClosest("The grammar rules have a problem with linking external files")