
from 洗虾工 import 洗虾工
from 大厨 import 大厨

class 吃货:
    _洗虾工 = 洗虾工()
    _大厨 = 大厨()

    def 请做虾(self):
        self._洗虾工.请做虾()
        self._大厨.请做虾()

    def 吃虾(self):
        print("吃货 正在吃虾")



