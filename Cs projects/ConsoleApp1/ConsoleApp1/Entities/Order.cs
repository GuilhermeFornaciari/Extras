using ConsoleApp1.Entities.Enums;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace ConsoleApp1.Entities
{
    internal class Order
    {
        public DateTime Moment { get; set; }
        public OrderStatus orderStatus { get; set; }

        public List<OrderItem> orderItem { get; set; }

        public Client Client { get; set; }

        public Order()
        {
            OrderStatus orderStatus = OrderStatus.Proccessing;
            DateTime Moment = DateTime.Now;

            orderItem = new List<OrderItem>();


        }

        public void AddOrder()
        {
            Console.WriteLine("Qual é o nome do produto?");
            string name = Console.ReadLine();

            Console.WriteLine("Quantos deste item você irá comprar?");
            float quantity = float.Parse(Console.ReadLine());

            Console.WriteLine("Qual é o preço unitário deste item?");
            double price = double.Parse(Console.ReadLine());

            orderItem.Add(new OrderItem(name, price, quantity));
        }

        public void RemoveOrder()
        {
            Console.WriteLine("Qual produto você deseja remover? digite o N° do produto correspondente: ");
            for (int i = 0; i < orderItem.Count; i++) 
            {
                Console.Write(i +": "+ orderItem[i].Product.Name+ ", ");
            }
            int remove = int.Parse(Console.ReadLine());

            orderItem.RemoveAt(remove);
        }

        public void Total()
        {
            Console.WriteLine("SUMMARIO:");
            Console.WriteLine("Momento da compra: " + Moment);
            Console.WriteLine("Status do pedido: " + orderStatus);
            Console.WriteLine();
            Console.WriteLine($"Nome do cliente: {Client.Name} ({Client.BirthDate}) - {Client.Email}");
            Console.WriteLine("Itens do pedido");
            double totalPrice = 0.0d;
            for (int i = 0; i < orderItem.Count; i++)
            {
                totalPrice += orderItem[i].Price;
                Console.WriteLine($"{orderItem[i].Product.Name}, R${orderItem[i].Product.Price}, Quantidade: {orderItem[i].Quantity}, subtotal: {orderItem[i].Price}");
            }
            Console.WriteLine("Total da venda:");
            Console.WriteLine(totalPrice);
        }
    }
}
