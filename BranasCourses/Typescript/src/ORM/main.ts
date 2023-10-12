import { ParameterizedQuery } from "pg-promise";
import {postgreSQLConnection, Connection} from "./connections";
import { Book, Entity, column } from "./Entities/Entity";

class ORM {
    constructor(readonly connection:Connection){
    }
    async save(entity:Entity):Promise<void>{
        let columns =  entity.columns.map((column)=> column.column).join(",")
        let values = entity.columns.map((column:column)=> entity[column.property])
        let params = entity.columns.map((column,i)=> "$"+ (++i)).join(",")
        this.connection.query(`insert into ${entity.schema}.${entity.table}(${columns}) values( ${params})`,values)
    }
    async list(entity:Function){
        return this.connection.query(`select * from ${entity.prototype.schema}.${entity.prototype.table}`, [])
    }
}
async function init() {
    const connection = new postgreSQLConnection()
    const orm = new ORM(connection);
    const book = new Book("Clean code", "Robert Martin");

    await orm.save(book);

    const books = await orm.list(Book)
    console.log(books);
    await connection.close()   
}

init()
    