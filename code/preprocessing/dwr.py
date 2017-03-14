import zipfile
from squad_preprocess import *


if __name__ == '__main__':
    glove_base_url = "http://nlp.stanford.edu/data/glove.840B.300d.zip"
    glove_filename = "glove.840B.300d.zip"
    prefix = os.path.join("download", "dwr")

    print("Storing datasets in {}".format(prefix))

    if not os.path.exists(prefix):
        os.makedirs(prefix)

    glove_zip = download(glove_base_url,os.path.join(prefix,glove_filename))
    os.rename(os.path.join(prefix, glove_filename),os.path.join(prefix,"glove.840B.zip"))
    glove_zip_ref = zipfile.ZipFile(os.path.join(prefix,"glove.840B.zip"), 'r')

    glove_zip_ref.extractall(prefix)
    glove_zip_ref.close()