## step1

Linked List Cycle 1 と同じような形だったが、ループの開始時点を2つのポインターを使ってもとめる方法はわからなかった。

一方、hashsetをつかって初めて一致したnodeがループの開始時点であることはわかったので、それをつかって解法をだした。

## step2

Floyd's Cycle Detection Algorithm というものがあることを知った。ただそれは常識ではないらしい。
速いnodeが2倍で動いていることに気をつけると、動作が理解できた。

合流地点Aで、速いnodeと遅いnodeの移動した距離は2倍。2つのnodeを同じ速さで戻すと、遅かったnodeがスタート地点にいるとき、速かったnodeが合流地点にいる。<- ここがわからずずっと考えていたけど、スッキリ。

[この説明をよく咀嚼した](https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0)

## step3

一度ロジックがわかればコードはシンプルなので、変数名など気を付けて再度コーディングをした。
