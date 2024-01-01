export default class Car {
    constructor(color, year) {
        this.color = color
        this.year = year
    }
}

export const getColor = function(carObj) {
    return carObj.color
}

export const getYear = function(carObj) {
    return carObj.color
}