package main

import (
	"log"
	"net/http"
)

func main() {
	fs := http.FileServer(http.Dir("./public"))
	http.Handle("/", fs)

	log.Println("Listening on http://localhost:1314")
	err := http.ListenAndServe(":1314", nil)
	if err != nil {
		log.Fatal(err)
	}
}
