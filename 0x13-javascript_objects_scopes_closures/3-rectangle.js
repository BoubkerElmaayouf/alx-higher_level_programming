#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str = str + 'X';
      }
      console.log(str);
    }
  }
}

module.exports = Rectangle;
