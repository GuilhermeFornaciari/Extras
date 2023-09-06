using ConsoleApp1.Entities;
using System;   
namespace ConsoleApp1 // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Order order = new Order();


            order.Client = new Client("Guilherme", "fornaciari049@gmail.com", DateOnly.Parse("2005-08-23"));
            order.orderItem.Add(new OrderItem("Sabão em pó", 25.0f, 4.0f));
            order.orderItem.Add(new OrderItem("Feijão", 15.0d, 2.0f));

            order.Total();
            


            

            /*
            Console.WriteLine("Olá, qual é o nome do cliente?");
            string clientName = Console.ReadLine();

            Console.WriteLine("Qual é o email do cliente?");
            string clientEmail = Console.ReadLine();

            Console.WriteLine("Qual é a data de nascimento do cliente?");
            DateOnly birthDate = DateOnly.Parse(Console.ReadLine());

            Client client = new Client(clientName,clientEmail,birthDate)
            */

            /*
            Console.WriteLine("Quantos items você irá comprar?");
            int itens = int.Parse(Console.ReadLine());

            for (int i = 0; i < itens; i++)
            {
                Console.WriteLine($"Digite os dados do {i+1}° item");
                order.AddOrder();
            }
            */



        }
    }
}