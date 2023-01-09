package main

import "fmt"

func main() {
	fmt.Println("Hello World")

	fakeAwsConnect()
	fakeSlackWebhook()
	fakeAwsConnectDup()

	randomFakeSACredentials()
}

func fakeAwsConnect() {
	fmt.Println("New for this file")
	iidd := "AKIABYAYVYDDEKVOUJVD"
	kkeeyy := "zUcJ2Hpx7o3NTR/BbwAsZRgyp+xJc1l/vVGKxAm"

	fmt.Println(iidd, kkeeyy)
}

func fakeAwsConnectDup() {
	fmt.Println("Same as config/connection.json")
	iidd := "AKIARQAYVYDDEKVOUJVD"
	kkeeyy := "rUcJ2Hpx7o3NTR/BbwAsZRgyp+xJc1l/vVGKxAmH"

	fmt.Println(iidd, kkeeyy)
}

func fakeSlackWebhook() {
	fmt.Println("New for this file")
	url := "https://hooks.slack.com/services/T033HKTSA/DHNMYJFE2/UbUBjDqSfkM3831vnr1glOy"

	fmt.Println(url)
}

func randomFakeSACredentials() {
	sa_username := "aGVsbG8gd29ybGQgdGhp"
	connect(sa_username, "prRJYxwhLfN/UO1NSnRXYZ22")
}

func connect(uname string, pwd string) {
	fmt.Println(uname, pwd)
}
