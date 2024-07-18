import ClassRoom from './0-classroom'; // Suppression de .js

function initializeRooms() {
  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ]; // Ajout d'une virgule finale
}

export default initializeRooms;
