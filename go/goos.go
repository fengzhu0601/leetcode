package main

import "fmt"
import "os"

func main() {
    var goos string = os.Getenv("GOOS")
    fmt.Printf("The operation system is:%s \n", goos)
    path := os.Getenv("PATH")
    fmt.Printf("Path is %s \n", path)
}
