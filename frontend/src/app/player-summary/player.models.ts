// player.models.ts

export interface Player {
    id: number;
    name: string;
    team: Team;
    games: Game[];
}

export interface Team {
    id: number;
    name: string;
}

export interface Shot {
  isMake: boolean;
  locationX: number;
  locationY: number;
}

export interface Game {
  team: string;
  id: number;
  date: string;
  isStarter: boolean;
  minutes: number;
  points: number;
  assists: number;
  offensiveRebounds: number;
  defensiveRebounds: number;
  // steals: number;
  // blocks: number;
  // turnovers: number;
  // defensiveFouls: number;
  // offensiveFouls: number;
  // freeThrowsMade: number;
  // freeThrowsAttempted: number;
  // twoPointersMade: number;
  // twoPointersAttempted: number;
  // threePointersMade: number;
  // threePointersAttempted: number;
  shots: Shot[];
}


