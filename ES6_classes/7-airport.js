class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Redéfinition de la méthode toString pour retourner le code de l'aéroport
  toString() {
    return `[object ${this._code}]`;
  }
}

export default Airport;
