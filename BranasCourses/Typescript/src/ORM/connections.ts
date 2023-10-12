import pgp from "pg-promise"

export interface Connection{
    query(statement:string,params:any):Promise<any>
    close():Promise<void>
}

export class postgreSQLConnection implements Connection{
    private pgp:any;
    constructor(){
        this.pgp = pgp()("postgres://postgres:root@localhost:5432/fornaciari")
    }
    query(statement: string, params: any): Promise<any> {
        return this.pgp.query(statement,params)
    }
    close(): Promise<void> {
        return this.pgp.$pool.end()
    }
}