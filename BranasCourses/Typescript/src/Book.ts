import Entity from "./Entity";

export default class Book extends Entity{
    constructor(readonly title:string){
        super(100)
    }
}