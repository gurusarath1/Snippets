console.log('Array -------------')
let ary = [1,2,3]
console.log(ary)
console.log(ary.length)
ary.push(4)
ary.push(5)
console.log(ary)
ary.pop()
console.log(ary)

if(ary.includes(10)) {
    console.log('10 is present')
}

if(ary.includes(2)) {
    console.log('2 is present')
}

console.log('Array Loop -------------')
for(let i=0; i<ary.length; i++) {
    console.log(ary[i])
}
// or
for(let x of ary) {
    console.log(x)
}

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

console.log('Function - Optional Arguments -----------')
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

console.log('Functions - Rest Parameters -------------')

const max_func = function(...vals) {
    let max_val = -Infinity
    for(let val of vals) {
        max_val = max_val < val ? val : max_val;
    }

    return max_val;
}

console.log(max_func(2,5,3,8))
console.log(max_func(...ary)) // ... also spreads out the array value when used in a function call

console.log('Functions - Access array members -------------')

const func_example = function([a,b,c]) {
    return a + b - c;
}
console.log(func_example([5,4,1]))

console.log('Object -------------')

let square = {
    side: 10,
    color: 'red',
    location_x_y_z: [21,45,25],
    'not valid binding name': 999,
}

let circle = {
    radius: 10,
    color: 'blue',
}

console.log(square)
console.log(square.color)
console.log(square['not valid binding name'])
console.log(square.testing) // Undefined
console.log('color' in square) // true
console.log('testing' in square) // false
delete square.color
console.log('color' in square) // false
console.log(Object.keys(square)) // array containing the name of all the properties
Object.assign(circle, square)
console.log(circle)

// Immutable - numbers, strings and Booleans

console.log('Constant Object -------------')
// Const object
const obj1 = {test:0, test2:1}
obj1.test = 10 // Allowed
//obj1 = {test:1, test2:6}  // Not Allowed

console.log('Prototype Object -------------')
// Object.prototype is the protype of all js objects

let obj_prt = {a:1, b:2, c:3}

console.log(Object.getPrototypeOf(obj_prt))
console.log(Object.getPrototypeOf(obj_prt) == Object.prototype) // true
console.log(Object.getPrototypeOf(Object.prototype)) // null

console.log('Classes - Creating objects with specific prototype -------------')


let box = {
    l : 0,
    b : 0,
    h : 0,
    vol() {
        return this.l*this.b*this.h;
    }
}

let new_box = Object.create(box)
console.log(new_box)
new_box.l = 3
new_box.b = 2
new_box.h = 1
console.log(new_box.vol())

// Constructors
// All functions automatically have a property called prototype, which hold a plain, empty object
function Rabbit(type, color='white') {
    this.type = type
    this.color = color
}

rabbitX = new Rabbit('wild') // Creates a object
console.log(rabbitX)

// Class Notation
// Only functions are allowed in class notation of Js
class Car {
    constructor(brand, color, max_speed) {
        this.brand = brand
        this.color = color
        this.max_speed = max_speed
        this.speed = 0
    }

    inc_speed() {
        this.speed++

        if(this.speed > this.max_speed) {
            this.speed = this.max_speed
        }
    }
}

car1 = new Car('bmw', 'black', 100)
car1.inc_speed()
console.log(car1)

console.log('JSON -------------')

let json_string = JSON.stringify(obj1)
console.log(json_string)






