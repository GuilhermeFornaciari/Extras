import Entity from "./Entity";
export default class Person extends Entity{
    constructor(public readonly name:string,public readonly age:number){
        super(100);
    }
}