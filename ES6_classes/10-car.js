class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    // Utilise la fonction Reflect.construct pour créer une nouvelle instance de la classe actuelle
    // sans passer les arguments du constructeur, ce qui laisse les attributs indéfinis.
    return Reflect.construct(this.constructor, []);
  }
}

export default Car;
