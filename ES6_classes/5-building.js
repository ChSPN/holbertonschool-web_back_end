class Building {
	constructor(sqft) {
		if (new.target === Building) {
			throw new TypeError('Cannot construct Building instances directly');
		}
		if (this.evacuationWarningMessage === undefined) {
			throw new TypeError('Class extending Building must override evacuationWarningMessage');
		}
		this._sqft = sqft;
	}

	get sqft() {
		return this._sqft;
	}

	evacuationWarningMessage() {
		throw new Error('You need to implement evacuationWarningMessage in your class');
	}
}
