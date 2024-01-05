import {
  ChangeDetectorRef,
  Component,
  OnDestroy,
  OnInit,
  ViewEncapsulation,
  ElementRef,
  AfterViewInit,
  ViewChild
} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {untilDestroyed, UntilDestroy} from '@ngneat/until-destroy';
import {PlayersService} from '../_services/players.service';
import {range} from 'rxjs';
import {concatMap, toArray} from 'rxjs/operators';
import {Game, Player, Team, Shot} from './player.models';


@UntilDestroy()
@Component({
  selector: 'player-summary-component',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class PlayerSummaryComponent implements OnInit, OnDestroy, AfterViewInit {
  @ViewChild('courtSvg', {static: false}) courtSvg: ElementRef<SVGElement>;
  imageWidth: number;
  imageHeight: number;
  playerList: any[] = [];
  selectedPlayer: Player;
  relatedGames: Game[]; // related to selectedPlayer
  selectedGame: Game;
  selectedShot: Shot[]; // related to selectedGame
  imgWidth = 1455;
  imgHeight = 1365;
  basketCenterX = 730;
  basketCenterY = 1207;
  threePointLineEndX = 1360;
  scaleX = Math.abs(this.threePointLineEndX - this.basketCenterX) / 22;
  threePointArcEndY = 520;
  scaleY = Math.abs(this.basketCenterY - this.threePointArcEndY) / 23.75;

  constructor(
    protected activatedRoute: ActivatedRoute,
    protected cdr: ChangeDetectorRef,
    protected playersService: PlayersService,
  ) {
  }

  ngOnInit(): void {
    this.loadAllPlayers();
  }

  ngAfterViewInit(): void {
  }

  loadAllPlayers(): void {
    range(1, 31)
      .pipe(
        concatMap(id => this.playersService.getPlayerSummary(id)),
        toArray()
      )
      .subscribe(results => {
        this.playerList = results.map(result => result.apiResponse);
        console.log(this.playerList);
      });
  }

  onPlayerChange() {
    console.log('Player changed:', this.selectedPlayer);
    this.relatedGames = this.selectedPlayer.games;
    console.log('Related games:', this.relatedGames);
  }

  onGameChange(game: Game): void {
    if (this.selectedGame) {
      console.log('Game changed:', game);
      this.drawShotsOnCourt(game.shots);
      console.log('Related shots:', game.shots);
    }
  }

  getSelectedGameShots() {
    if (this.selectedGame) {
      this.selectedShot = this.selectedGame.shots;
      console.log('Selected shots:', this.selectedShot);
      return this.selectedShot;
    }
    return [];
  }

  getShotPixelCoordinates(shot: Shot): { x: number, y: number } {
    return {
      x: this.basketCenterX + shot.locationX * this.scaleX,
      y: this.basketCenterY - shot.locationY * this.scaleY
    };
  }

  drawShotsOnCourt(shots: Shot[]): void {
    const svg: SVGElement = this.courtSvg.nativeElement;

    // clear all existing shot dots
    const shotDots = svg.querySelectorAll(".shot-dot");
    shotDots.forEach(dot => dot.remove());

    shots.forEach(shot => {
      const coords = this.getShotPixelCoordinates(shot);

      const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      circle.setAttribute("cx", coords.x.toString());
      circle.setAttribute("cy", coords.y.toString());
      circle.setAttribute("r", "10");
      circle.setAttribute("fill", shot.isMake ? "green" : "red");
      circle.classList.add("shot-dot");

      svg.appendChild(circle);
    });
  }


  onImageLoad(): void {
    const img = document.getElementById('courtImage') as HTMLImageElement;
    this.imageWidth = img.width;
    this.imageHeight = img.height;
  }

  ngOnDestroy() {
  }

}
