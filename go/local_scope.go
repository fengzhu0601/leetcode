package main

var a = "G"

func main(){
    n()
    m()
    n()
}

func n(){
    print(a)
}

func m() {
    a := "O" // a局部创建新变量
    print(a)
}

// GOG