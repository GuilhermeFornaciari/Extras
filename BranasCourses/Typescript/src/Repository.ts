import Entity from "./Entity";

export default class Repository<T extends Entity>{
    list: T[];
    constructor(){
        this.list = []
    }
    add (element:T){
        this.list.push(element)
    }
}