import Building from './5-building';

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // Appel du constructeur de la classe parente
    this._floors = floors; // Initialisation de l'attribut _floors
  }

  // Getter pour sqft
  get sqft() {
    return this._sqft;
  }

  // Getter pour floors
  get floors() {
    return this._floors;
  }

  // Surcharge de la méthode evacuationWarningMessage
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}

export default SkyHighBuilding;
