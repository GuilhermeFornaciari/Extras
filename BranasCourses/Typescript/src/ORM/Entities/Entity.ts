function entity(config:{schema:string, table:string}){
    return (constructor:Function)=>{
        constructor.prototype.schema = config.schema;
        constructor.prototype.table = config.table;
        
    }
}
function column(config: {name:string}){
    return (target:Entity,propertyKey:string) =>{
        target.columns = target.columns || [];
        target.columns.push({ property:propertyKey, column:config.name})
    }
}
export type column = {property:string,column:string}

@entity({schema:"fornaciari",table:"book"})
export abstract class Entity{
    declare schema:string;
    declare table:string;
    declare columns: column[]
    [key:string]:any 
}

export class Book extends Entity{
    @column({name:"title"})
    title:string;
    @column({name:"author"})
    author:string;
    constructor(title:string,author:string){
        super();
        this.title = title;
        this.author = author;
    }
}