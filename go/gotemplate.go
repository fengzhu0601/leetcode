package main

import "fmt"

const c = "C"

var v int = 5

type T struct{}

func init(){
    fmt.Println("hello init")
    fmt.Println(c)
    fmt.Println(v)
}

func main() {
    var a int
    Func1()

    fmt.Println(a)
}

func (t T) Method1(){

}

func Func1(){

}
