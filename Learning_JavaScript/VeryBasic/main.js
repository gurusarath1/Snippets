console.log('NaN -----------')
console.log(NaN)
console.log(0/0)
console.log(Infinity - Infinity)

console.log('Empty values -----------')
// Assume both are the same thing
console.log(null)
console.log(undefined)

console.log('Strings -----------')
// Strings - Unicode - 16 bits per char
// Unicode contains more than 2^16 chars, therefore some characters take up two chars
console.log(`String 1+1 = ${1+1}`) // Template literal
console.log("String 2")
console.log('String 3')
console.log('Contatenate ' + 'test')

console.log('Typeof -----------')
// typeof
console.log(typeof 4) // number
console.log(typeof 4.2) // number
console.log(typeof 'Hi') // string

console.log('boolean -----------')
// Boolean - true and false
console.log(3 > 2)
console.log('a' < 'b') // true
console.log('az' < 'ba') // true
console.log('Z' > 'a') // false // Upper case is always less than lower case letters
console.log(NaN == NaN) // false //There is only one value in Js that is not equal to itself, and that is NaN

console.log('logical operators -----------')
console.log(true && false)
console.log(true || false)
console.log(!true)

console.log('ternary operator -----------')
console.log(true ? true:false)
console.log(false ? true:false)

// Type conversion
console.log('Type conv-----------')
console.log(8 *null) // 0
console.log('5' - 1) // 4
console.log('5' + 1) // 51 string concatenation
console.log('5' - (-1)) // 6
console.log('g' * 2) // NaN
console.log(false == 0) // true
console.log(false === 0) // false
console.log(false == "") // true
console.log(false === "") // false
console.log(null == 0) // false
console.log(null == undefined) // true
console.log(Number(null))

console.log('Bindings -----------')
let x = 10
let y = x
const pi = 3.14
console.log(pi)
console.log(x)
x = 11
console.log(y) //10

console.log('prompt binding -----------')
name_ = prompt('What is your name ?')
console.log('Hi ' + name_)

console.log('Function -----------')

const cube = function(x) {
    if(Number.isNaN(x)) return 0;

    return x*x*x;
}

const add = (x,y) => {
    return x+y;
}

const cube_2 = x => {
    if(Number.isNaN(x)) return 0;

    return x*x*x;
}

console.log(cube(3))
console.log(cube_2(3))

console.log('Function - Optional Arguments-----------')
console.log(cube(4,1,2)) // Optional arguments

const minus = function(x,y) {
    if(y === undefined) return -x;
    return x-y;
}
console.log(minus(4)) 
console.log(minus(4,1)) 

const add_2 = function(x,y=0) {
    return x+y;
}
console.log(add_2(300)) 

console.log('Function - Local bindings are created anew everytime-----------')

const val = function(n) {
    let local = n
    return () => local
}

let val1 = val(999)
let val2 = val(777)

console.log(val1()) // 999
console.log(val2()) // 777