// This file is required by the index.html file and will
// be executed in the renderer process for that window.

// Runs user interface of app (or webpage which is an instance of
// webContents
// All of the Node.js APIs are available in this process.

const zerorpc = require("zerorpc")
let client = new zerorpc.Client()
client.connect("tcp://127.0.0.1:4242")

let formula = document.querySelector('#formula')
let result = document.querySelector('#result')
formula.addEventListener('input', () => {
  client.invoke("shannon", formula.value, (error, res) => {
    if(error) {
      console.error(error)
    } else {
      result.textContent = res
    }
  })
})
formula.dispatchEvent(new Event('input'))