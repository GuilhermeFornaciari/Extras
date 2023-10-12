import Person from "./Person";
import Book from "./Book";
import Repository from "./Repository";

const repository = new Repository<Person>()

let pessoa = new Person("Guilherme",18)

repository.add(pessoa)

console.log(repository);
