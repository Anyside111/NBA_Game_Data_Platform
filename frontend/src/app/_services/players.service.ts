import {HttpClient, HttpParams} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable, BehaviorSubject} from 'rxjs';
import {map, tap} from 'rxjs/operators';
// import {plainToClass} from 'class-transformer';

import {BaseService} from './base.service';
import {Game, Player, Team, Shot} from '../player-summary/player.models';

@Injectable({
    providedIn: 'root'
})
export class PlayersService extends BaseService {
    constructor(protected http: HttpClient) {
        super(http);
    }

    getPlayerSummary(playerID: number): Observable<any> {
        const endpoint = `${this.baseUrl}/playerSummary/${playerID}`;

        return this.get(endpoint).pipe(map(
            (data: Object) => {
                return {
                    endpoint: endpoint,
                    apiResponse: data
                };
            },
            error => {
                return error;
            }
        ));
    }
}

