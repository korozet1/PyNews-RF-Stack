class Config(object):
    def __init__(self):
        #原始数据路径
        self.train_datapath=r".\data\train.txt"
        self.test_datapath=r".\data\test.txt"
        self.dev_datapath=r".\data\dev.txt"
        self.class_datapath=r".\data\class.txt"

        #处理后的数据路径
        self.process_train_datapath = r".\data\process_train.csv"
        self.proces_test_datapath = r".\data\process_test.csv"
        self.proces_dev_datapath = r".\data\process_dev.csv"

         #停用词路径
        self.stop_words_path=r".\data\stopwords.txt"

        #保存模型路径
        self.rf_model_save_path=r"save_model"
        self.model_predict_result=r"result"
        #self.WERKZEUG_RUN_MAIN=True


if __name__ == '__main__':
    conf=Config()
    print(conf.train_datapath)
    print(conf.dev_datapath)