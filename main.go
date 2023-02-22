package main

import (
    "fmt"
    "log"
	"time"
    "os/exec"

	"github.com/sevlyar/go-daemon"
)

func main() {
	cntxt := &daemon.Context{
		PidFileName: "/var/run/sample.pid",
		PidFilePerm: 0644,
		LogFileName: "/var/log/sample.log",
		LogFilePerm: 0640,
		WorkDir:     "/",
		Umask:       027,
		Args:        []string{"[go-daemon sample]"},
	}

	d, err := cntxt.Reborn()
	if err != nil {
		log.Fatal("Unable to run: ", err)
	}
	if d != nil {
		return
	}
	defer cntxt.Release()

	log.Print("- - - - - - - - - - - - - - -")
	log.Print("daemon started")

	testFunction()
}

func testFunction() {
	for {
		log.Print(getOutput())
		time.Sleep(10 * time.Second)
	}
}

func getOutput() string {
    out, err := exec.Command("xrandr").Output()
    if err != nil {
		log.Printf(err)
        log.Fatal(err)
    }
    outString := fmt.Sprintf("%s", out)

	return outString
}
