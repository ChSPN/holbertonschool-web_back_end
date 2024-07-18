class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Méthode appelée lors de la conversion de l'objet en nombre
  valueOf() {
    return this._size;
  }

  // Méthode appelée lors de la conversion de l'objet en chaîne de caractères
  toString() {
    return this._location;
  }
}

export default HolbertonClass;
