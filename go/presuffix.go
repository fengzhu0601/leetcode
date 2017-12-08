package main

import (
	"fmt"
	"strings"
)

func main(){
	var str string = "This is an example of a string"
	fmt.Printf("T/F? Does this string \"%s\" has prefix %s? ", str, "Th")
	fmt.Printf("%t\n", strings.HasPrefix(str, "Th"))

	fmt.Printf("T/F? Does this string \"%s\" has suffix %s? ", str, "n")
	fmt.Printf("%t\n", strings.HasSuffix(str, "n"))

	fmt.Printf("T/F? Does this string \"%s\" contains %s? ", str, "example")
	fmt.Printf("%t\n", strings.Contains(str, "example"))
}

